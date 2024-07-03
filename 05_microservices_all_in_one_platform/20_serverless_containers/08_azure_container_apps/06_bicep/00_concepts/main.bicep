// Simple Bicep Example for Beginners
// This example demonstrates basic usage of parameters (param), variables (var), and referencing the resource group.

var hello = 'Hello, Bicep!'

// Define a parameter for the storage account name prefix
@description('The name prefix for the storage account')
param storagePrefix string = 'mystorage'

// Define a parameter for the resource location with a default value
@description('The location to deploy all resources')
param location string = resourceGroup().location

// Define a variable to create a unique storage account name
var storageAccountName = '${storagePrefix}${uniqueString(resourceGroup().id)}'

// Define a resource for a Storage Account
resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
  }
}
