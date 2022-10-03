import asyncpg
import os
import json

#Pola singleton adalah pola desain yang membatasi 
# instantiation kelas ke satu objek.
class Connection:
     
    async def connect():
        path = os.getcwd()
        with open(path+'/'+'src'+'/'+'config.json') as file:
            conf = json.load(file)['postgresql']
        conn = None
        """ Static access method"""
        if conn == None:
            try:
                conn =  await asyncpg.connect(host=conf['host'],
                                            database=conf['db'],
                                            user=conf['user'],
                                            password=conf['pwd'])
                print(f"[INFO] Success connect PostgreSQL .....")
            except:
                print(f"[INFO] Can't connect PostgreSQL .....")
        return conn

    ####### setup connection with Pool #######
    async def connectionPool():
        conn = None
        """ Static access method"""
        if conn == None:
            try:
                conn =  await asyncpg.connect(host=conf['host'],
                                            database=conf['db'],
                                            user=conf['user'],
                                            password=conf['pwd'])
                print(f"[INFO] Success connect PostgreSQL .....")
            except:
                print(f"[INFO] Can't connect PostgreSQL .....")
        return conn


