from flask import Flask, render_template, request
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
    #tables are: head, chest, arms, waist, legs
    def list_armor(self,table):
        self.cur.execute("SELECT * FROM "+table)
        result = self.cur.fetchall()
        return result

    def piece_detail(self,table,name):
        self.cur.execute("SELECT * FROM "+table+" WHERE name = '"+name+"'")
        result = self.cur.fetchall()
        return result


#Pages
#Homepage
@app.route('/')
def main():
    db = Database("armor")
    result1 = db.list_armor("head")
    result2 = db.list_armor("chest")
    result3 = db.list_armor("arms")
    result4 = db.list_armor("waist")
    result5 = db.list_armor("legs")
    return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5)

@app.route('/',methods=['POST'])
def showTables():
    #Get current value of each dropdown box
    headName = request.form.get('headName')
    chestName = request.form.get('chestName')
    armName = request.form.get('armName')
    waistName = request.form.get('waistName')
    legName = request.form.get('legName')

    #Specify db and query tables for dropdown boxes
    db = Database("armor")
    result1 = db.list_armor("head")
    result2 = db.list_armor("chest")
    result3 = db.list_armor("arms")
    result4 = db.list_armor("waist")
    result5 = db.list_armor("legs")
    #Select specified armor piece from each table
    details1 = db.piece_detail("head",headName)
    details2 = db.piece_detail("chest",chestName)
    details3 = db.piece_detail("arms",armName)
    details4 = db.piece_detail("waist",waistName)
    details5 = db.piece_detail("legs",legName)

    #print(details1.skill1)

    return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5,
    headpiece = details1,chestpiece = details2,armpiece = details3,waistpiece = details4,legpiece = details5)

#Head pieces table
@app.route('/head-pieces')
def showHeadPieces():
    db = Database("armor")
    pieces = db.list_armor("head")
    return render_template('headArmor.htm',result = pieces)

#Chest pieces table
@app.route('/chest-pieces')
def showChestPieces():
    db = Database("armor")
    pieces = db.list_armor("chest")
    return render_template('chestArmor.htm',result = pieces)

#Arm pieces table
@app.route('/arm-pieces')
def showArmPieces():
    db = Database("armor")
    pieces = db.list_armor("arms")
    return render_template('armArmor.htm',result = pieces)

#Waist pieces table
@app.route('/waist-pieces')
def showWaistPieces():
    db = Database("armor")
    pieces = db.list_armor("waist")
    return render_template('waistArmor.htm',result = pieces)

#Leg pieces table
@app.route('/leg-pieces')
def showLegPieces():
    db = Database("armor")
    pieces = db.list_armor("legs")
    return render_template('legArmor.htm',result = pieces)

if __name__ == "__main__":
    app.run()