import psycopg2
from time import gmtime, strftime
from Config import host, db_name, user, password

g = strftime("%Y-%m-%d %H:%M:%S", gmtime())


# CONNECT TO EXIST DB FROM USER
def connection(out_name):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            database=db_name,
            password=password
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT column_name 
                FROM information_schema.columns
                WHERE  table_name = '{}'
                ORDER  BY ordinal_position;""".format(out_name)
            )
            x = []
            for cur in cursor:
                x.append(cur)
            cursor.execute(
                """SELECT * FROM {};""".format(out_name)
            )
            for cur in cursor:
                x.append(cur)

            return x
    except Exception as _ex:
        print("INFO[Error] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print(f"[INFO ({g})] PostgreSQL connection close")


# ATTEMPTING TO SING IN TO YOUR ACCOUNT
def check(entry_login, entry_password):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            database=db_name,
            password=password
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM users;"""
            )
            x = []
            for i in cursor:
                x.append(i)

            for i in range(len(x)):
                print(i, x[i])
                for j in range(len(x[i])):
                    print(j, x[i][j])
                    if entry_login == x[i][j]:
                        entry_login = True
                        print(entry_login, ' - ')
                        if entry_password == x[i][j + 1]:
                            entry_password = True
                            print(entry_password, '-')
                            return entry_login, entry_password
                        else:
                            pass
                    else:
                        pass
            return entry_login, entry_password
    finally:
        if connection:
            connection.close()
            print(f"[INFO ({g})] PostgreSQL connection close")


# ATTEMPTING TO CREATE A NEW ACCOUNT
def create_ac(new_login, new_password):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            database=db_name,
            password=password
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO users VALUES
                (default, '{}', '{}');""".format(new_login, new_password)
            )
            x = []
    finally:
        if connection:
            connection.close()
            print(f"[INFO ({g})] PostgreSQL connection close")


# ATTEMPTING TO CREATE A NEW ACCOUNT
def delete_data(delete_var, in_entry):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            database=db_name,
            password=password
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """DELETE FROM {}
                WHERE id={};""".format(delete_var, in_entry)
            )
            print(f'[INFO ({g})] Success delete from {in_entry} item {delete_var}')
    finally:
        if connection:
            connection.close()
            print(f"[INFO ({g})] PostgreSQL connection close")


def add_data(in_entry, add_var):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            database=db_name,
            password=password
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO {} VALUES
                (default, {})""".format(add_var, in_entry)
            )
            print(f'[INFO ({g})] Success add data in {in_entry} item {add_var}')
    finally:
        if connection:
            connection.close()
            print(f"[INFO ({g})] PostgreSQL connection close")


def observation_action_del(name_action, in_num, delete_var):  # new
    connection = psycopg2.connect(
        host=host,
        user=user,
        database=db_name,
        password=password
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO actions VALUES
            (default, '{}', {}, '{}')""".format(name_action, in_num, delete_var)
        )


def observation_action_add(name_action, add_var):  # new
    connection = psycopg2.connect(
        host=host,
        user=user,
        database=db_name,
        password=password
    )
    connection.autocommit = True
    q = f"SELECT id from {add_var} order by id desc limit 1"
    cursor = connection.cursor()
    cursor.execute(q)
    row = cursor.fetchone()
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO actions VALUES
            (default, '{}', {}, '{}')""".format(name_action, row[0], add_var)
        )
