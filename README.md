# CSV Split and SQL Generator

This project was created with [Python](https://www.python.org/) 


## About this project
This project included CSV splitting and SQL insert script generating feature.

## Hot to build and run?

1) Change "table_name" variable in program_sql.py
2) Change row count in "chunk_size". It is located in program_csv.py
2) open terminal or command prompt

Preparing the project to run:

Better to creat env for development.

```
python3 -m venv envname
```

```
source envname/bin/activate
```

```
pip3 install -r requirements.txt 
```

Running the program:

```
python3 program_csv.py   
```

```
python3 program_sql.py     
```



## Project folder structure

### CSVs and SQLs folders structure.

    ├── filename.csv (This is a CSV file to split and generate SQL)            
    ├── csvs          
        ├── generated-csvs              
    ├── sqls          
        ├── generated-sqls    
