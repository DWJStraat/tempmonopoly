import sqlite3 as sql


class DB:
    def __init__(self):
        self.con = sql.connect('db.db')

    def execute(self, query):
        cur = self.con.cursor()
        val = cur.execute(query).fetchall()
        self.con.commit()
        cur.close()
        return val

    def build(self):
        self.execute("CREATE TABLE users(id, name, score)")

    def create(self, id, name, money = 1500):
        self.execute(f"INSERT INTO users VALUES ("
                     f"{id},"
                     f"'{name}',"
                     f"{money})")

    def add(self, id, money = 100):
        curr_money = self.execute(f'SELECT score FROM users where id = {id}')[0][0]
        money = curr_money + money
        self.execute(f'UPDATE users SET score = {money} WHERE id = {id}')

    def check_exists(self, id):
        if self.execute(f'SELECT * FROM users where id = {id}') != []:
            return True
        else:
            return False

if __name__ == "__main__":
    db = DB()
    # db.build()
    # db.create(1, 'flipper')
    print(db.execute('SELECT * FROM users'))
