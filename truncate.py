import psycopg2

conn = psycopg2.connect(user = "postgres",password = "rocker12", host = "127.0.0.1", port = "5433", database = "nova")
cursor = conn.cursor()
query = """TRUNCATE TABLE "TWOA" """
cursor.execute(query)
queryy = """TRUNCATE TABLE "INWARD" """
cursor.execute(queryy)
cursor.close()
conn.commit()
conn.close()