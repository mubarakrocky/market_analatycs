import psycopg2



host = 'localhost'
db_name = 'princeses'
user = 'root'
password = 'root'
port = 5432
conn = psycopg2.connect(host=host, port=port, dbname=db_name, user=user, password=password)
