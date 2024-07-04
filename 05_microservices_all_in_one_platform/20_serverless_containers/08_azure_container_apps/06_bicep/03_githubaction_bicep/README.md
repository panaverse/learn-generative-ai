# Steps to Deploy Azure Container App with GitHub Actions and Bicep

### Prerequisites

Cover step 05_github_actions and deploy your fastapi code using it. We will use it as our Starter Code.

#### 1. **Set Up Azure ResourceGroup**
- **Login and Create Azure Resource Group:**
    ```sh
    az login
    ```

#### 2. **Configure GitHub Secrets**

Go to your GitHub repository.
Navigate to `Settings` > `Secrets and variables` > `Actions`.
Add the following secrets:

- `DOCKER_HUB_USERNAME`: Your Docker Hub username.
- `DOCKER_HUB_ACCESS_TOKEN`: Your Docker Hub access token (You can create an access token from Docker Hub instead of using your password).
- `AZURE_CREDENTIALS`: Your Azure credentials in JSON format:
- `AZURE_RG`: Your Azure Resource Group Name
- `AZURE_SUBSCRIPTION`: Azure Subscription Id

#### 3. Add main.bicep file from last step as same level as pyproject.toml.

#### 4. **Create GitHub Action Workflow**
- In your GitHub repository, create a `.github/workflows/deploy.yml` file with the following content:

    ```yaml
  name: Deploy Bicep file

  on:
    push:
      branches:
        - main

  jobs:
    build-and-deploy:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v3

        - name: Log into Azure
          uses: azure/login@v1
          with:
            creds: ${{ secrets.AZURE_CREDENTIALS }}

        - name: Log in to Docker Hub
          uses: docker/login-action@v2
          with:
            username: ${{ secrets.DOCKER_HUB_USERNAME }}
            password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

        - name: Build and push Docker image
          uses: docker/build-push-action@v4
          with:
            context: .
            push: true
            tags: ${{ secrets.DOCKER_HUB_USERNAME }}/myapp:latest

        - name: Deploy Bicep file
          uses: azure/arm-deploy@v1
          with:
            subscriptionId: ${{ secrets.AZURE_SUBSCRIPTION }}
            resourceGroupName: ${{ secrets.AZURE_RG }}
            template: ./main.bicep
            parameters: image=${{ secrets.DOCKER_HUB_USERNAME }}/myapp:latest
            failOnStdErr: false
    ```

#### 5. **Run GitHub Action**
- Push your code to the `main` branch, and the GitHub Actions workflow will trigger automatically, building and deploying your container app to Azure.

### Additional Tips
- **Testing Locally:** Before deploying, ensure your Docker container works as expected locally.
- **Monitoring:** Use Azure Portal to monitor your container app’s health and logs.

This setup ensures that the names are correctly formatted in lowercase, which should resolve the registry name error.