import asyncpg
import asyncio

#Pola singleton adalah pola desain yang membatasi 
# instantiation kelas ke satu objek.
class Connection:
    conn = None # Connection instance (class atribut)
    async def connect():
        """ Static access method"""
        if Connection.conn == None:
            try:
                conn =  await asyncpg.connect('postgresql://postgres:postgres@192.168.64.15:5432/digitalskola')
                print(f"[INFO] Success connect PostgreSQL .....")
            except:
                print(f"[INFO] Can't connect PostgreSQL .....")
        return Connection.conn
    
    # def __init__(self):
    #     """ Virtually private constructor"""
    #     if Connection.conn != None:
    #         #choose to throw an exception if a condition occurs
    #         raise Exception("This Class is singleton") 
    #     else:
    #         Connection.conn = self
    def main():
        asyncio.run(Connection.connect()) 
        '''cek Jumlah instance yang dibuat sama dan 
        ada atau tidak ada perbedaan dalam objek yang tercantum dalam output.'''
        # s = Connection()
        # print(s)
        # s = asyncio.run(Connection.connect())
        # print(s)
        # d = asyncio.run(Connection.connect())
        # print(d)
        # s = Connection.connect()
        # print(s)

        connect = Connection()
        new_connect = Connection()

        print(connect is new_connect)

        # connect = asyncio.run(Connection.connect())
        # print(new_connect)

if __name__ == '__main__':
    Connection.main()

   

