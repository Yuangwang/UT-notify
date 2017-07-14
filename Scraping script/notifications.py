import psycopg2


def notify_user():
    # opens connection and cursor for future use
    con = psycopg2.connect("dbname='myBot' user='postgres' host='localhost' password='29900770wei'")
    cur = con.cursor()

    # pending_notifs is a list of duples in the format ('phonenumber', uniquenumber)
    cur.execute("SELECT * FROM userinfo")
    pending_notifs = cur.fetchall()

    for notif in pending_notifs:
        cur.execute("SELECT name FROM course WHERE id =%s", (notif[1], ))
        print(cur.fetchall())

    con.close()
    cur.close()

