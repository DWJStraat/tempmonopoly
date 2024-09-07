from flask import Flask
from database import DB
app = Flask(__name__)

@app.route('/')
def main():
    return 'Wrong page, bucko'

@app.route('/user/<id>')
def hello_world(id):  # put application's code here
    if DB().check_exists(id):
        DB().add(id)
        return 'added 100 moneys!'
    else:
        return 'account does not exist, contact Mang'


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
