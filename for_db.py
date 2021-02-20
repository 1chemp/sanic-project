import aiopg
# import asyncio

dsn = 'dbname=aquapricedb user=postgres password=53bapisi1 host=127.0.0.1'


async def test_select():
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1")
                ret = []
                async for row in cur:
                    ret.append(row)
                assert ret == [(1,)]
    print("ALL DONE")

    return {"ALL": "DONE"}


async def go():
    conn = await aiopg.connect(database='aquapricedb',
                               user='postgres',
                               password='53bapisi1',
                               host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute("SELECT * FROM newss")
    ret = await cur.fetchall()

    return ret


# GET request
async def get_data_news():
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * FROM newss;")
                news = await cur.fetchall()
    return news


# GET request
async def get_data_products():
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * FROM productss;")
                product = await cur.fetchall()
    return product


# POST request
async def add_new_contacts(input_data):
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(
                        "INSERT INTO contacts (username, phone, status) VALUES (%s, %s, %s);",
                        (input_data["username"],
                         input_data["phone"], input_data["status"])
                    )
                    return {"OK": "Success!"}
                except Exception as e:
                    return {"Error": f"{e}"}


# POST request
async def add_new_orders(input_data):
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(
                        "INSERT INTO orders (name, mail, phone, city, addresspost,"
                        " company, inn, kpp, bik, post, pay, scope, price, datee, status, products) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                        (input_data["name"], input_data["mail"], input_data["phone"], input_data["city"],
                         input_data["addresspost"], input_data["company"], input_data["inn"], input_data["kpp"],
                         input_data["bik"], input_data["post"], input_data["pay"], input_data["scope"], input_data["price"],
                         input_data["datee"], input_data["status"], input_data["products"])
                    )

                    return {"OK": "Success!"}

                except Exception as e:
                    return {"Error": f"{e}"}


# async def get_all_products():
#     query = 'SELECT id, name, image, price, performance, description, category, isonindex FROM productss;'
#     async with aiopg.connect(DB_URL) as conn:
#         async with conn.cursor(cursor_factory=DictCursor) as cur:
#             await cur.execute(query)
#             data = await cur.fetchall()
#             print(data)
#             return [dict(u) for u in data]
