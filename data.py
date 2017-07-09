import psycopg2

'''All functions in this file contribute to interacting with the database'''


# goes into courses database and returns a set of the uniques that are in it
def current_unique_data():
    # goto database and get the unique number
    con = psycopg2.connect("dbname='myBot' user='postgres' host='localhost' password='29900770wei'")
    cur = con.cursor()
    cur.execute("SELECT id FROM course")
    db = cur.fetchall()

    # convert the unique values into a set and returns
    db_unique = []
    for unique in db:
        db_unique.append(unique[0])
    return set(db_unique)