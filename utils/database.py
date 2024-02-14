import sqlite3


class DataBase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def add_new_user(self, tg_id, username, f_name, l_name):
        self.cursor.execute(f"INSERT INTO users (tg_username, tg_firstname, tg_lastname, tg_id)"
                            f"VALUES (?,?,?,?);", (username, f_name, l_name, tg_id))
        self.connection.commit()

    def update_user(self, tg_id, full_name, phone):
        self.cursor.execute(f"UPDATE users SET full_name=?, tg_phone=?"
                            f"WHERE tg_id=?;", (full_name, phone, tg_id))
        self.connection.commit()

    def get_user(self, tg_id):
        users = self.cursor.execute(f"SELECT * FROM users WHERE tg_id=?;", (tg_id, ))
        return users.fetchone()

    def get_user_by_username(self, user_name):
        users = self.cursor.execute(f"SELECT * FROM users WHERE tg_username=?;", (user_name, ))
        return users.fetchone()


    def __del__(self):
        self.cursor.close()
        self.connection.close()