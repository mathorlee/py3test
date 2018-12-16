from pyhive import hive

config = {
    'host': 'localhost',
    'port': 10000,
    'username': 'opt',
    'database': 'tmp'
}

connection = hive.connect(**config)
cursor = connection.cursor()
sql = 'select count(*) from employee'
cursor.execute(sql, async=True)
rows = cursor.fetchall()

def e(sql):
    cursor.execute(sql)
    return cursor.fetchall()



'select count(*) from employee'