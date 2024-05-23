# Tennis_Match_Prediction_Run
## Overview
This is an end-to-end project built by [Runhouse](https://www.run.house) that orchestrates a seamless pipeline from data fetching and preprocessing to model training and deployment. The model is a random forest model predicting tennis matches, it is eventually deployed on AWS EKS with Seldon as API service.

## Descriprion
There are two main Python scripts in this repository:
1. runhouse_init.py
This Python script creates a Runhouse cluster and environment that allow functions to run on it. Once created, the cluster and all functions will be stored in Den, which is a cloud platform provided by Runhouse.
![](/images/den.png)

2. model_deployment.py
This script pulls functions from Den and runs the data/training pipeline, eventually deploying the model with Seldon, as well as storing the artifacts on AWS.

## How to run
1. Login to Runhouse by command line
```
runhouse login
```
2. Run runhouse_init.py file, this should only do once
```
python runhouse_init.py
```
3. Run pipeline
```
python model_deployment.py
```