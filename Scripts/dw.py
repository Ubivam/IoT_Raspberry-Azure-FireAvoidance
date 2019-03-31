from azure import *
from azure.cosmosdb.table.tableservice import *
from azure.cosmosdb import *

table_service = TableService(account_name='hakastorage', account_key='zASnIm4Sae2wNGvPwwpk8X01xRW2pcG8hFfjZK8bisPRDxLfzKYRag+60FTnWbtHOcjAIKpXC5j6Bb/jBN/qhw==')
i=0
next_pk = None
next_rk = None
while True:
    entities=table_service.query_entities('hakastorage',"PartitionKey eq 'Djura'", next_partition_key = next_pk, next_row_key = next_rk, top=1000)
    i+=1
    for entity in entities:
        print(entity.AddressLine1)
    if hasattr(entities, 'x_ms_continuation'):
        x_ms_continuation = getattr(entities, 'x_ms_continuation')
        next_pk = x_ms_continuation['nextpartitionkey']
        next_rk = x_ms_continuation['nextrowkey']
    else:
        break;
