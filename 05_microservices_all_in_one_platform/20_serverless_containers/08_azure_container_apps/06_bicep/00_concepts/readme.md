# IAC - Using Bicep

Bicep allows you to define your Azure resources in a simple templating language, then deploy those resources across multiple environments and applications. Bicep helps reduce manual deployment operations so you can scale your solutions more easily and with higher quality and consistency.

1. [Install Bicep extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep)


2. Understand Basic Concepts for Bicep File Syntax

- ### Variables
    - Purpose: Used to define variables within the Bicep template. Variables hold values that are computed or derived from parameters or other expressions within the template.
    
    - Usage: Ideal for values that are calculated based on other parameters or variables, or for simplifying complex expressions by breaking them down into simpler components.
    
    - Syntax:
    ```bicep
    var <name> = <expression>
    ```
    
    Example:
    ```bicep
    var storageAccountName = 'mystorageaccount${uniqueString(resourceGroup().id)}'
    var vmAdminUsername = 'adminUser'
    ```
    Learn more: [Azure Resource Manager - Bicep Variables](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables)
    
- ### Params
    - Purpose: Used to define parameters that are passed into the Bicep template. Parameters allow you to customize the deployment by providing values at runtime.
    
    - Usage: Ideal for values that are likely to change or need to be provided externally when deploying the template.
    
    - Syntax:
    ```bicep
    param <name> <type> = <default_value>
    ```
    
    - Example:
    ```bicep
    param location string = 'eastus'
    param vmSize string
    ```
    Learn more: 
    - [Azure Resource Manager - Bicep Parameters](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters)
    - [Build your first Bicep template - Add flexibility with parameters and variables](https://learn.microsoft.com/en-us/training/modules/build-first-bicep-template/5-add-flexibility-parameters-variables)
    
- ### Resources
    
    The main thing you'll do with Bicep templates is define your Azure resources. Here's an example of what a typical resource definition looks like in Bicep. This example creates a storage account named toylaunchstorage.

    ```bicep
    resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
        name: 'toylaunchstorage'
        location: 'westus3'
        sku: {
        name: 'Standard_LRS'
        }
        kind: 'StorageV2'
        properties: {
        accessTier: 'Hot'
        }
    }
    ```

    Let's look closely at some key parts of this resource definition:

    - The resource keyword at the start tells Bicep that you're about to define a resource.
    - Next, you give the resource a symbolic name. In the example, the resource's symbolic name is storageAccount. Symbolic names are used within Bicep to refer to the resource, but they won't ever show up in Azure.
    - Microsoft.Storage/storageAccounts@2022-09-01 is the resource type and API version of the resource. Microsoft.Storage/storageAccounts tells Bicep that you're declaring an Azure storage account. The date 2022-09-01 is the version of the Azure Storage API that Bicep uses when it creates the resource.

    Learn more: [Build your first Bicep template - Define resources](https://learn.microsoft.com/en-us/training/modules/build-first-bicep-template/3-define-resources), 
    

