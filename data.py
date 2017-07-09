import psycopg2

'''All functions in this file contribute to interacting with the database'''


# goes into courses database and returns a set of the uniques that are in it
def current_unique_data(cur):
    # goto database and get the unique number
    cur.execute("SELECT id FROM course")
    db = cur.fetchall()

    # convert the unique values into a set and returns
    db_unique = []
    for unique in db:
        db_unique.append(unique[0])
    return set(db_unique)


# updates the existing class
# TODO needs more testing still
def update_class(course, cur, con):
    cur.execute("UPDATE course SET day=%s, hour=%s, room=%s, professor=%s, status=%s, name=%s "
                "WHERE id=(%s)",
                (course.day, course.hour, course.room, course.professor, course.status, course.name, course.unique_num))
    con.commit()


# inserts new class
def insert_class(course, cur, con):
    cur.execute("INSERT INTO course (id, day, hour, room, professor, status, name) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (course.unique_num, course.day, course.hour, course.room, course.professor, course.status, course.name))
    con.commit()
