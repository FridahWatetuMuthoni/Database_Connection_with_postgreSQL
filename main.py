import psycopg2
import psycopg2.extras


hostname = "localhost"
database = "test"
username = "postgres"
pwd = "7040"
port_id = 5432
conn = None

###############################Connect to the postgresql database ########################################

try:
    conn = psycopg2.connect(
        host = hostname,
        database = database,
        user = username,
        password = pwd,
        port = port_id
    )
    print("Connection Successfull")
    
    ########################-create table in postgress database-############################
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("DROP TABLE IF EXISTS IG_python")
    create_script = """
            CREATE TABLE IF NOT EXISTS IG_python(
                id INT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                followers INT,
                post_num INT
            )
    """
    cur.execute(create_script)
    
    ########################-insert data into the postgress database-############################
    insert_script = "INSERT INTO IG_python(id, name, followers, post_num) values (%s, %s, %s, %s)"
    insert_values = [(1, "@_python.py_",19100,210),(2, "_python.py_",19,0),]
    for insert_value in insert_values:
        cur.execute(insert_script, insert_value)

    ########################-select data from IG_python table-############################
    cur.execute("SELECT * FROM IG_python")
    records = cur.fetchall()
    print("select data is: \n ",)
    for record in records:
        print(record)
    print()
    
    ########################-insert data into the postgress database-############################
    update_script = "UPDATE IG_python SET followers = followers * 2"
    cur.execute(update_script)
    conn.commit()
    
    ########################-select data after update-############################
    cur.execute("SELECT * FROM IG_python")
    records = cur.fetchall()
    print("select after update data is: " ,end="\n",)
    for record in records:
        print(record)
    print()
    conn.commit()
    
    ########################-delete some data from IG_python table-############################
    delete_script = "DELETE FROM IG_python WHERE name = %s"
    delete_id = ('_python.py_',)
    cur.execute(delete_script, delete_id)
    
    ########################-select data after update-############################
    cur.execute('SELECT * FROM IG_python')
    records = cur.fetchall()
    print("Select data after delete: \n ",)
    for record in records:
        print(record)
    print()
    
except Exception as error:
    print(f"Error Message: {error}")

finally:
    if conn is not None or cur is not None:
        conn.close()
        cur.close()