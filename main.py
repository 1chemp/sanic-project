import asyncio
import json as js
import sys

# Для тестов на время
import timeit

from sanic import Sanic
from sanic.response import json

from for_db import get_data_products, get_data_news, \
    add_new_contacts, add_new_orders, test_select

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = Sanic(__name__)


@app.route('/hi')
async def hello(request):
    for_son = await test_select()
    return json(for_son)


@app.get('/api/v1/news')
async def get_current_news(request):
    for_json = await get_data_news()
    return json(for_json)


@app.get('/api/v1/products')
async def get_current_products(request):
    for_json = await get_data_products()
    return json(for_json)


@app.route("/api/v1/contacts", methods=["POST", ])
async def insert_and_get_data_from_contacts(request):
    preparing_data = request.body.decode()
    data = js.loads(preparing_data)

    for_json = await add_new_contacts(data)
    return json(for_json)


@app.route("/api/v1/orders", methods=["POST", ])
async def insert_and_get_data_from_orders(request):
    preparing_data = request.body.decode()
    data = js.loads(preparing_data)

    for_json = await add_new_orders(data)
    return json(for_json)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
