import csv
import os

table_name = "client_addresses"
dir_path = 'csvs'

for path in os.listdir(dir_path):
    if not path.startswith("."):
        openFile = open('csvs/'+path, 'r')
        csvFile = csv.reader(openFile)
        header = next(csvFile)
        headers = map((lambda x: '`'+x+'`'), header)
        insert = 'INSERT INTO '+table_name+' (' + ", ".join(headers) + ") VALUES "
        result_text = ""
        for row in csvFile:
            values = map((lambda x: '"'+x+'"'), row)
            result_text += insert +"("+ ", ".join(values) +");\n" 
        openFile.close()

        with open('sqls/'+path[:-4]+'.sql', 'w') as f:
            f.write(result_text)

