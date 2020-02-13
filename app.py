from flask import Flask, render_template
import pymysql

app = Flask(__name__)

#Database class to open a new DB connection
class Database:
    def __init__(self,data_base):
        #Credentials
        self.db = data_base
        host = "192.168.56.117"
        user = "remjamd"
        password = "password1"
        #Connect
        self.con = pymysql.connect(host=host, user=user, password=password, db=self.db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        print("connected to database")
    #class method to query DB table
    def list_armor(self,table):
        self.cur.execute("SELECT * FROM "+table)
        result = self.cur.fetchall()
        return result

@app.route('/')
def main():
    db = Database("armor")
    pieces = db.list_armor("head")
    return render_template('armors.html',result = pieces)

@app.route('/showChestPieces')
def showChestPieces():
    db = Database("armor")
    chests = db.list_armor("chest")
    return render_template("chestPieces.html",result = chests)

if __name__ == "__main__":
    app.run()