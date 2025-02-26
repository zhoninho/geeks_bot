# queries.py

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    price TEXT,
    size TEXT,
    product_id TEXT,
    photo TEXT
    )
"""

CREATE_TABLE_store_details = """
    CREATE TABLE IF NOT EXISTS store_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    infoproduct TEXT,
    product_id TEXT
    )
"""

CREATE_TABLE_collection = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT ,
    collection TEXT,
    )
"""


INSERT_store_query = """
    INSERT INTO store (name_product, price, size, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""

INSERT_store_details_query = """
    INSERT INTO store_details (category, infoproduct, product_id)
    VALUES (?, ?, ?)
"""

INSERT_collection_query = """
    INSERT INTO collection_products (product_id, collection)
    VALUES (?, ?)
"""

FETCH_ALL_PRODUCTS_QUERY = """
    SELECT s.name_product, s.price, s.size, s.product_id, s.photo,
           sd.category, cp.collection
    FROM store s
    INNER JOIN store_details sd ON s.product_id = sd.product_id
    INNER JOIN collection_products cp ON s.product_id = cp.product_id
"""