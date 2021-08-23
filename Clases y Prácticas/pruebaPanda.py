import json
import pandas as pd 
from sqlalchemy import create_engine
import pymysql

# SERVIDOR_PRODUCTOS = "http://pad19.com:3030"
# ENDPOINT_PRODUCTOS = "productos/10"
# ENDPOINT_PEDIDOS = "pedidos/10"
# ENDPOINT_CONSULTA_PEDIDOS = "pedidos/"
# TOKEN_PRODUCTOS = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUiLCJub21icmUiOiJBZ3VzdGluYSBEaWF6In0.GyeVZLQEwb9G6s586a-HqVEAZmNSWUMoDTV2ZVuzULU"
# #URL_CONSULTA_PRODUCTO = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?token={TOKEN}"

MYSQL_SERVIDOR = "productos/10"
MYSQL_USUARIO = "3030"
MYSQL_CLAVE = "pad19.com:3030"


def conectarMysql():
	motorMysql = create_engine(f"mysql+pymysql://{MYSQL_USUARIO}:{MYSQL_CLAVE}@{MYSQL_SERVIDOR}/token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUiLCJub21icmUiOiJBZ3VzdGluYSBEaWF6In0.GyeVZLQEwb9G6s586a-HqVEAZmNSWUMoDTV2ZVuzULU", pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False

def main():
	conn = conectarMysql()
	if (conn):
		dataframe = pd.read_sql("SELECT * FROM clasificacion_f1", conn)
		print(dataframe)


if (__name__ == "__main__"):
	main()