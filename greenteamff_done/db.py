import sqlite3

conn = sqlite3.connect("db.sqlite")

cursor = conn.cursor()
sql_query = """CREATE TABLE "Product" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "price" TEXT NOT NULL,
  "image" TEXT NOT NULL,
  "availabilty" TEXT NOT NULL,
  "categories" TEXT NOT NULL,
  "info" TEXT NOT NULL
);"""
cursor.execute(sql_query)

cursor = conn.cursor()
sql_query = """CREATE TABLE "User" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "fname" TEXT NOT NULL,
  "lname" TEXT NOT NULL,
  "email" TEXT NOT NULL,
  "phone" INTEGER,
  "password" TEXT NOT NULL
);"""
cursor.execute(sql_query)

cursor = conn.cursor()
sql_query = """CREATE TABLE "Order" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER NOT NULL REFERENCES "User" ("id") ON DELETE CASCADE
);



"""
cursor.execute(sql_query)

cursor = conn.cursor()
sql_query = """CREATE INDEX "idx_order__user_id" ON "Order" ("user_id");"""
cursor.execute(sql_query)

cursor = conn.cursor()
sql_query = """CREATE TABLE "Order_product" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "quantity" INTEGER,
  "order_id" INTEGER NOT NULL REFERENCES "Order" ("id") ON DELETE CASCADE,
  "product_id" INTEGER NOT NULL REFERENCES "Product" ("id") ON DELETE CASCADE
);
"""
cursor.execute(sql_query)

cursor = conn.cursor()
sql_query = """CREATE INDEX "idx_order_product__order_id" ON "Order_product" ("order_id");"""
cursor.execute(sql_query)

cursor = conn.cursor()
sql_query = """CREATE INDEX "idx_order_product__product_id" ON "Order_product" ("product_id")"""
cursor.execute(sql_query)
