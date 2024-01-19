# db_connection.py

import pymysql
from db_config import db_config

def create_connection():
    connection = pymysql.connect(
        host=db_config['localhost'],
        user=db_config['root'],
        password=db_config['****'],
        database=db_config['ds-proj']
    )
    return connection
