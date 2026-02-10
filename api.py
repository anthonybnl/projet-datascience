from typing import Literal, Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel
from pathlib import Path
import pandas as pd
import joblib

pipeline_modele_supervise = joblib.load(Path("models") / "supervise.pkl")
pipeline_modele_non_supervise = joblib.load(Path("models") / "non_supervise.pkl")

description = """
# API segmentation SmartSegment Auto

Cette API permet de faire appel aux modèles non supervisé et supervisé.

Le modèle supervisé permet de prédire le segment d'un client à partir de ses caractéristiques. Le modèle non supervisé permet de faire du clustering sur les données des clients.
"""

app = FastAPI(description=description)

Type_profession = Literal[
    "Healthcare",
    "Engineer",
    "Lawyer",
    "Entertainment",
    "Artist",
    "Executive",
    "Doctor",
    "Homemaker",
    "Marketing",
]

Type_anonymized_var = Literal[
    "Cat_1",
    "Cat_2",
    "Cat_3",
    "Cat_4",
    "Cat_5",
    "Cat_6",
]

Type_modele_supervise_output = Literal["A", "B", "C", "D"]


class DataFeatures(BaseModel):
    age: int
    work_experience: float
    family_size: float
    gender: Literal["Male", "Female"]
    ever_married: Literal["Yes", "No"]
    graduated: Literal["Yes", "No"]
    profession: Type_profession
    spending_score: Literal["Low", "Average", "High"]
    var_1: Type_anonymized_var


@app.post("/models/supervise")
def model_supervise(
    input: Annotated[DataFeatures, Query()],
) -> Type_modele_supervise_output:
    """Permet de faire appel au modèle supervisé. Retourne le segment prédit pour un client donné."""

    input_df = pd.DataFrame([input.model_dump()])
    input_df.loc[:, "age"] = input_df.loc[:, "age"].astype(float)

    predicted = pipeline_modele_supervise.predict(input_df)[0]

    print(predicted)

    return predicted


@app.post("/models/non_supervise")
def model_non_supervise(
    input: Annotated[DataFeatures, Query()],
) -> int:
    """Permet de faire appel au modèle non supervisé. Retourne le cluster prédit pour un client donné."""

    input_df = pd.DataFrame([input.model_dump()])
    input_df.loc[:, "age"] = input_df.loc[:, "age"].astype(float)

    predicted = pipeline_modele_non_supervise.predict(input_df)[0]

    print(predicted)

    return predicted
