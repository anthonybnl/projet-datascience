FROM python:3.13.12-trixie
WORKDIR /app

# pip requirements

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# models

COPY ./models/supervise.pkl ./models/supervise.pkl
COPY ./models/non_supervise.pkl ./models/non_supervise.pkl

# source

COPY ./api.py .

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
