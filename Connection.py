import psycopg2
from Config import host, db_name, user, password


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
            print("[INFO] PostgreSQL connection close")


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
                for j in range(len(x[i])):
                    if entry_login == x[i][j]:
                        entry_login = True
                        if entry_password == x[i][j + 1]:
                            entry_password = True
                            return entry_login, entry_password
                        else:
                            pass
                    else:
                        pass
            return entry_login, entry_password



    except Exception as _ex:
        print("INFO[Error] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection close")


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


    except Exception as _ex:
        print("INFO[Error] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection close")


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
            print(f'[INFO] Success delete from {in_entry} item {delete_var}')

    except Exception as _ex:
        print("INFO[Error] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection close")


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
            print(f'[INFO] Success add data in {in_entry} item {add_var}')

    except Exception as _ex:
        print("INFO[Error] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection close")
