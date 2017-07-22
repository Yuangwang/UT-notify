import psycopg2


# stores user phone number and user classes to watch into database or deletes their info
def main():
    mode = ""

    con = psycopg2.connect("dbname='myBot' user='postgres' host='localhost' password='example'")
    cur = con.cursor()

    while mode != "watch" and mode != "unwatch":
        mode = input("Watch for class or unwatch?")

    if mode == "watch":
        phone = input("Phone Number in the format +1xxxxxxxxxx:")

        classes = input("How many classes would you like to watch?")
        courses = int(classes)

        for course in range(courses):
            unique = input("Unique Number:")
            status = input("Watch for open or waitlisted?")
            cur.execute("INSERT INTO userinfo (phone, classunique, status) values(%s, %s, %s)", (phone, unique, status))
            status += "; restricted"
            cur.execute("INSERT INTO userinfo (phone, classunique, status) values(%s, %s, %s)", (phone, unique, status))

    if mode == "unwatch":
        phone = input("Phone Number in the format +1xxxxxxxxxx:")

        classes = input("How many classes would you like to unwatch?")
        courses = int(classes)

        for course in range(courses):
            unique = input("Unique Number:")
            cur.execute("DELETE FROM userinfo WHERE phone=%s AND classunique=%s",(phone, unique))

    con.commit()
    con.close()
    cur.close()


if __name__ == "__main__":
    main()