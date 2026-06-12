import psycopg

conn = psycopg.connect("postgresql://rag:rag@localhost:5432/rag")

cur = conn.execute("SELECT 1")
print(f"Postress connected:{cur.fetchone()}")

cur = conn.execute("SELECT extversion from Pg_extension where extname = 'vector'")
print(f"pgvector versoin: {cur.fetchone()[0]}")

conn.close()
print("all done")
