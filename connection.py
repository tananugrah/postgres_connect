import asyncpg

#Pola singleton adalah pola desain yang membatasi 
# instantiation kelas ke satu objek.
class Connection:
     
    async def connect():
        conn = None
        """ Static access method"""
        if conn == None:
            try:
                conn =  await asyncpg.connect('postgresql://postgres:postgres@192.168.64.15:5432/digitalskola')
                print(f"[INFO] Success connect PostgreSQL .....")
            except:
                print(f"[INFO] Can't connect PostgreSQL .....")
        return conn
    

