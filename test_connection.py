import pymysql

# Manual connection test to MySQL
try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="bhavani09@",
        database="moviesdb",
        port=3306
    )
    print("✅ Connected successfully!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
