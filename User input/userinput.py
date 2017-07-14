import psycopg2


# stores user phone number and user classes to watch into database
def main():

    con = psycopg2.connect("dbname='myBot' user='postgres' host='localhost' password='example'")
    cur = con.cursor()

    phone = input("Phone Number in the format +xxxxxxxxxx:")

    classes = input("How many classes would you like to watch?")
    courses = int(classes)

    for course in range(courses):
        unique = input("Unique Number:")
        cur.execute("INSERT INTO userinfo (phone, classunique) values(%s, %s)", (phone, unique))

    con.commit()
    con.close()
    cur.close()


if __name__ == "__main__":
    main()