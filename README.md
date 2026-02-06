# TrustNote

Détection de contrefaçon de billet par analyse de données et apprentissage automatique.

dataset : https://www.kaggle.com/datasets/mdladla/fake-currency-data

## Contexte

La contrefaçon de billets représente un enjeu majeur pour les institutions financières, les commerçants et les autorités monétaires. Selon la Banque Centrale Européenne, plus de 500 000 faux billets sont retirés de la circulation chaque année en Europe, entraînant des pertes économiques estimées à plusieurs millions d’euros.

Les billets contrefaits, souvent de qualité croissante, sont difficiles à détecter à l’œil nu, surtout pour les petites dénominations et dans des environnements à fort volume de transactions (caisses enregistreuses, distributeurs automatiques, etc.).

Les méthodes traditionnelles de détection (marqueurs UV, filigranes) sont parfois insuffisantes ou coûteuses à déployer à grande échelle.

Dans ce contexte, les banques, commerces et institutions publiques ont besoin de solutions automatisées, précises et scalables pour identifier les billets suspects en temps réel, sans ralentir les opérations courantes.

L’enjeu est double :

- réduire les pertes financières liées à l’acceptation de faux billets ;
- renforcer la confiance dans les transactions en espèces, encore largement utilisées malgré la digitalisation des paiements.

## Problématique métier

Comment automatiser la détection des billets contrefaits à partir de leurs caractéristiques physiques (poids, dimensions, sécurité) et contextuelles (pays d’origine, dénomination), tout en s’adaptant à la diversité des devises et des montants en circulation ?

## Objectif Data Science

L’objectif de ce projet est de **concevoir un modèle prédictif** capable de :

- classer automatiquement un billet comme authentique ou contrefait (`Counterfeit = 1 ou 0`) à partir de données structurées, en tenant compte du pays et de la dénomination ;
- identifier des profils de contrefaçon (via un modèle non supervisé) pour mieux comprendre les tendances et adapter les mesures de sécurité.
- optimiser la précision et l’interprétabilité du modèle, afin de permettre une intégration opérationnelle (ex : via une API) dans des systèmes existants de vérification.
