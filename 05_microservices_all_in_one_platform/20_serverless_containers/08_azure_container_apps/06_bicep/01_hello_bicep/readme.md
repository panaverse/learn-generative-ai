# IAC - Using Bicep

Bicep allows you to define your Azure resources in a simple templating language, then deploy those resources across multiple environments and applications. Bicep helps reduce manual deployment operations so you can scale your solutions more easily and with higher quality and consistency.

1. Install Bicep extension for Visual Studio Code
2. Review 00_concepts step before the main.bicep file. 

## Deploy Bicep File

### A. Deploy Using Azure CLI

-> Deployment:

```
az group create --name exampleRG --location eastus

az deployment group create --resource-group exampleRG --template-file main.bicep
```

Cleanup:

```
az group delete --name exampleRG
```

https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/quickstart-create-bicep-use-visual-studio-code?tabs=CLI

https://www.youtube.com/watch?v=6dDJpkLiIFU&list=PLvtybS2EHFJg459xQ6ApYUZrDae3lRfx4&index=1

https://learn.microsoft.com/en-us/training/modules/build-first-bicep-template/3-define-resources

https://learn.microsoft.com/en-us/training/modules/build-first-bicep-template/5-add-flexibility-parameters-variables

https://learn.microsoft.com/en-us/training/modules/build-first-bicep-template/7-group-related-resources-modules