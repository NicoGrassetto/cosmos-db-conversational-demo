from azure.cosmos import CosmosClient, PartitionKey
import os


endpoint = "your_cosmos_account_uri"
key = "your_cosmos_account_key"
client = CosmosClient(endpoint, key)


database_name = 'your_database_name'
container_name = 'your_container_name'
partition_key_path = '/your_partition_key'

database = client.create_database_if_not_exists(id=database_name)
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path=partition_key_path),
    offer_throughput=400
)


item = {
    'id': '1',
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

container.upsert_item(item)
