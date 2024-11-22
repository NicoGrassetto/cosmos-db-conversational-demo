@secure()
param administratorLoginPassword string
param location string
param clusterName string
param coordinatorVCores int = 4
param coordinatorStorageQuotaInMb int = 262144
param coordinatorServerEdition string = 'GeneralPurpose'
param enableShardsOnCoordinator bool = true
param nodeServerEdition string = 'MemoryOptimized'
param nodeVCores int = 4
param nodeStorageQuotaInMb int = 524288
param nodeCount int
param enableHa bool
param coordinatorEnablePublicIpAccess bool = true
param nodeEnablePublicIpAccess bool = true
param availabilityZone string = '1'
param postgresqlVersion string = '15'
param citusVersion string = '12.0'

resource serverName_resource 'Microsoft.DBforPostgreSQL/serverGroupsv2@2022-11-08' = {
  name: clusterName
  location: location
  properties: {
    administratorLoginPassword: administratorLoginPassword
    coordinatorServerEdition: coordinatorServerEdition
    coordinatorVCores: coordinatorVCores
    coordinatorStorageQuotaInMb: coordinatorStorageQuotaInMb
    enableShardsOnCoordinator: enableShardsOnCoordinator
    nodeCount: nodeCount
    nodeServerEdition: nodeServerEdition
    nodeVCores: nodeVCores
    nodeStorageQuotaInMb: nodeStorageQuotaInMb
    enableHa: enableHa
    coordinatorEnablePublicIpAccess: coordinatorEnablePublicIpAccess
    nodeEnablePublicIpAccess: nodeEnablePublicIpAccess
    citusVersion: citusVersion
    postgresqlVersion: postgresqlVersion
    preferredPrimaryZone: availabilityZone
  }
}
