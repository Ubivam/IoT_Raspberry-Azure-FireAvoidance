from azure import *
from azure.cosmosdb.table.tableservice import *
from azure.cosmosdb import *
import time
import os
table_service = TableService(account_name='hakastorage', account_key='zASnIm4Sae2wNGvPwwpk8X01xRW2pcG8hFfjZK8bisPRDxLfzKYRag+60FTnWbtHOcjAIKpXC5j6Bb/jBN/qhw==')
i=0

next_rk = None
f = open("ivana_mi_te_volimo.txt", "w").close()
f = open("ivana_mi_te_volimo.txt", "a")
rows = table_service.query_entities(
    'HakaTable', "PartitionKey eq 'Boban'", next_rk)
while True:
    for item in rows.items:
        word= str(item)
        year= word.find("datetime(",0,len(word)-1)
        hum= word.find("humidity",0,len(word)-1)
        temp= word.find("temperature",0,len(word)-1)
        etag= word.find("etag",0,len(word)-1)
        tzinfo= word.find("tzinfo",0,len(word)-1)
        #print(word)
        txt = word.split()
        godina = txt[5].find('(')
        str_godina = txt[5][godina+1:godina+5]
        str_mesec = txt[6].replace(",","")
        str_dan = txt[7].replace(",", "")
        str_sat = txt[8].replace(",", "")
        str_minut = txt[9].replace(",", "")
        str_sekund = txt[10].replace(",", "")
        str_pritisak = txt[40].replace(",", "")
        str_temperatura = txt[42].replace(",", "")
        ivana = str_godina + "/" + str_mesec + "/" + str_dan + " " + str_sat + ":" + str_minut + ":" + str_sekund + " " + str_pritisak + " " + str_temperatura + '\n'
        strahinja = str_sat + ":" + str_minut + ":" + str_sekund + ", " + str_temperatura + '\n'
        print(ivana)
        f.write(strahinja)
        f.flush()
        os.fsync(f)
        time.sleep(0.6)
    if hasattr(rows, 'x_ms_continuation'):
        x_ms_continuation = getattr(rows, 'x_ms_continuation')
        next_rk = x_ms_continuation['nextrowkey']

f.close()

#next_pk = None
#next_rk = None
#while True:
#    entities=table_service.query_entities(table_name='haka-table', num_results=1000, next_partition_key = next_pk, next_row_key = next_rk )
#    i+=1
#    for entity in entities:
#        print(entity.AddressLine1)
#    if hasattr(entities, 'x_ms_continuation'):
#        x_ms_continuation = getattr(entities, 'x_ms_continuation')
#        next_pk = x_ms_continuation['nextpartitionkey']
#        next_rk = x_ms_continuation['nextrowkey']
#    else:
#        break;