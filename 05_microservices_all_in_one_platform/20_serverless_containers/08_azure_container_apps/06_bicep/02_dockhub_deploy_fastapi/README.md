# Build & Deploy FastAPI Image using Bicep

Here's what we will do:

1. Build and Push Image to DockerHub

```docker buildx build --platform linux/amd64 -f Dockerfile.prod -t mjunaidca/hello-img:latest --push --rm .```

2. Create resource group if it doesn't exist
```az group create --name exampleRG --location eastus```

3. Deploy Bicep template and pass image name
```az deployment group create --resource-group exampleRG --template-file main.bicep --parameters image=docker.io/mjunaidca/hello-img:latest```

4. Remove all resources

```
az group delete --name exampleRG
```

In main.bicep now we are dynamically taking an environment variable image. Next let's move to Azure ACR register and automate this image registry aspect.