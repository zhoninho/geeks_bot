import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def create_tables():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_store_details)
    cursor.execute(queries.CREATE_TABLE_collection)


async def sql_insert_store(name_product, price, size, product_id, photo):
    cursor.execute(queries.INSERT_store_query,
                   (name_product, price, size, product_id, photo))
    db.commit()


async def sql_insert_store_details(category, infoproduct, product_id):
    cursor.execute(queries.INSERT_store_details_query,
                   (category, infoproduct, product_id))
    db.commit()


async def sql_insert_collection(product_id, collection):
    cursor.execute(queries.INSERT_collection_query,
                   (product_id, collection))


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    select * from store s
    INNER JOIN store_details sd on s.product_id = sd.product_id
    """).fetchall()
    conn.close()
    return products