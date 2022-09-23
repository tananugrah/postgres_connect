import asyncio
from connection import Connection

# async def select_data():
#     conn = Connection.connect()
#     record_data = await conn.fetchrow("""SELECT * FROM tb_users """)
#     await Connection.fetchall(record_data())
#     print(record_data)


def main():
    asyncio.run(Connection.connect())
    # s = Connection()
    # print(s)
    # s = asyncio.run(Connection.connect())
    # print(s)
    # d = asyncio.run(Connection.connect())
    # print(d)
    s = Connection()
    print(s)
    t = Connection()
    print(t)


if __name__ == '__main__':
    main()