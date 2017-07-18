import psycopg2
from twilio.rest import Client


def notify_user():

    # twilio api creds
    account_sid = "AC990926986c47467863661a382f435bb6"
    auth_token = "3d5b69e1002c0a8a95d2d65d7887e22d"

    # opens connection and cursor for future use
    con = psycopg2.connect("dbname='myBot' user='postgres' host='localhost' password='29900770wei'")
    cur = con.cursor()

    # pending_notifs is a list of tuples in the format ('phonenumber', uniquenumber, 'status', 'notified')
    cur.execute("SELECT * FROM userinfo")
    pending_notifs = cur.fetchall()

    for notif in pending_notifs:
        cur.execute("SELECT name, status FROM course WHERE id =%s AND status =%s", (notif[1], notif[2]))

        # current_course is a list with one duple in the format ('name', 'status'), returns [] if no match
        notify_courses = cur.fetchall()

        # only notify user is notify_courses list is not empty and the user hasn't been notified yet
        if notify_courses and not notif[3]:
            client = Client(account_sid, auth_token)
            client.messages.create(
                to=notif[0],
                from_="+15126472269",
                body="your course: " + notify_courses[0][0] + "is now " + notif[2]
            )

            # mark course as notified
            cur.execute("UPDATE userinfo SET notified = TRUE WHERE phone=%s AND status=%s AND classunique=%s",
                        (notif[0], notif[2], notif[1]))
            con.commit()

        # notifies user that the old class is now closed
        if not notify_courses and notif[3]:
            client = Client(account_sid, auth_token)
            client.messages.create(
                to=notif[0],
                from_="+15126472269",
                body="your course: " + notify_courses[0] + "is now closed or waitlisted"
            )

            # mark course as unnotified
            cur.execute("UPDATE userinfo SET notified = FALSE WHERE phone=%s AND status=%s AND classunique=%s",
                        (notif[0], notif[2], notif[1]))
            con.commit()

    con.close()
    cur.close()

