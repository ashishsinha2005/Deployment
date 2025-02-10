# End-to-End-Machine-Learning-Project

## Flow of End to End Machine Learning Implementation

1. Github Setup
2. Create an Virtual environment for the project
3. Project Template Creation
4. Project setup
5. Logging, Exception and Utility
6. Notebook Experiment
7. Project workflow
8. Component Implementation
    - Data Ingestion
    - Data Validation
    - Data Transformation
    - Model Training
    - Model Evaluation
9. Training Pipeline
10. Prediction 
11. User Application
12. Dockerization
13. Deployement 

## Pre-requirments

1. Python knowledge
2. Machine Learning algorithms
3. AWS for deployement
4. Github account
5. VS code or any other platform for coding

## 1. Github Setup

- Create a Repository for a project 
- Clone it using a link in your local system

```bash
Git clone "Link of your Github Repository"
```
- You can able to see your project folder.

Note: Command to commit

```bash
git add .
git commit -m "Message for an commit"
git push origin main
```

## 2. Create an Virtual environment for the project

```bash
conda create -n projectname python==3.10 -y
```

```bash
conda activate projectname
```

## 3. Project Template Creation

- Create Project template for creating folders and files.

- Add a Libaries in requirements.txt to install.

- Install it using the below command

```bash
pip install -r requirements.txt
```

## 4. Project setup

- Create a setup.py file and write the necessary code.

## 5. Logging, Exception and Utility

- Create a logging code in src/__init__. (to know the details, time and the folder details.)

- Exception - for exception box is used here

- Utility -  Create common.py in utils( to store the common code like yaml creation, load, json file loading writing etc)

## 6. Notebook Experiment

- Try to do the coding for your data in jupyter notebook. 

## 7. Project workflow

 1. update config.yaml
 2. update schema.yaml
 3. update params.yaml
 4. update the entity
 5. update the configuration manager in src config
 6. update the components
 7. update the pipeline
 8. update the main.py
 9. update the app.py





