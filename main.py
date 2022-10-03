import time

import asyncio
from src.connection import Connection
from dataExtract1 import dataExtract_base

import os

start_time = time.time()

loop = asyncio.new_event_loop()


def main():
    query = "SELECT * FROM tb_users LIMIT 5"

    r = loop.run_until_complete(Connection.connect())

    s = loop.run_until_complete(dataExtract_base.extract(
                                connection= r, 
                                query= query
                                ) )
    # t = loop.run_until_complete(dataExtract_com.extract(
    #                             connection= r, 
    #                             query= query
    #                             ))
    print(s)
    # print(t)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()