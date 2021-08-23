# pip3 install pymysql o python -m pip install pymysql
# pip3 install sqlalchemy o python -m pip install sqlalchemy

# Librerías
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv.main import load_dotenv
load_dotenv()


# Definiciones
SERVIDOR = os.getenv("SERVIDOR")
USUARIO = os.getenv("USUARIO")
CLAVE = os.getenv("CLAVE")
BBDD = os.getenv("BBDD")


# Funciones 
def conectarMysql():
	motorMysql = create_engine(f"mysql+pymysql://{USUARIO}:{CLAVE}@{SERVIDOR}/{BBDD}", pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False


# Main
if (__name__ == "__main__"):
	resultado = conectarMysql()

	if (resultado):
		print("Conectado a la bbdd, listo para consultas")
	else:
		print("Error al conectar con la bbdd")