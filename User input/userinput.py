import psycopg2


# stores user phone number and user classes to watch into database
def main():

    con = psycopg2.connect("dbname='myBot' user='postgres' host='localhost' password='29900770wei'")
    cur = con.cursor()

    phone = input("Phone Number in the format +1xxxxxxxxxx:")

    classes = input("How many classes would you like to watch?")
    courses = int(classes)

    for course in range(courses):
        unique = input("Unique Number:")
        status = input("Watch for open or waitlisted?")
        cur.execute("INSERT INTO userinfo (phone, classunique, status) values(%s, %s, %s)", (phone, unique, status))
        status += "; restricted"
        cur.execute("INSERT INTO userinfo (phone, classunique, status) values(%s, %s, %s)", (phone, unique, status))

    con.commit()
    con.close()
    cur.close()


if __name__ == "__main__":
    main()