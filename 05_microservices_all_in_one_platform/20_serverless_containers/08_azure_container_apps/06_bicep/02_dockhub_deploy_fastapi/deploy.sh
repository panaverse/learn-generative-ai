#!/bin/bash

# Set variables
RESOURCE_GROUP="exampleRG"
LOCATION="eastus"
TEMPLATE_FILE="main.bicep"
DOCKER_IMAGE_NAME="mjunaidca/hello-img:latest"
DOCKERFILE="Dockerfile.prod"

# Build and push Docker image with --rm flag to remove intermediate containers
echo "Building and pushing Docker image..."
docker buildx build --platform linux/amd64 -f $DOCKERFILE -t $mjunaidca/hello-img:latest --push --rm .

# Remove the existing image from local Docker to free up space (optional)
echo "Removing local Docker image..."
docker rmi $DOCKER_IMAGE_NAME

# Create resource group if it doesn't exist
echo "Creating resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# Deploy Bicep template
echo "Deploying Bicep template..."
az deployment group create --resource-group $RESOURCE_GROUP --template-file $TEMPLATE_FILE --parameters image=$DOCKER_IMAGE_NAME

echo "Deployment completed."
