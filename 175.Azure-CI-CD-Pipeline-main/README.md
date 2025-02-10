# AZURE-CICD-Deployment-with-Github-Actions


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 


## Save pass:

Registry name: flasksampleapp

Login server: flasksampleapp.azurecr.io

username: flasksampleapp

password :LSBP7AutwA5xC4L6O5GncjCOsteLE+iH/+QAL5TiUI+ACRDuZ0EP

## Run from terminal: to built a docker image and push it into an container registory

docker build -t flasksampleapp.azurecr.io/mltest:latest .

docker login flasksampleapp.azurecr.io

docker push flasksampleapp.azurecr.io/mltest:latest

## Open Web app Server in azure and fill the details

Note : Choose github account and choost container reg.

Pull the docker image from the container reg to web app

Choose the github actions and check in gituhub actions.

Automatically the github/workflow will get create.