from flask import Flask, render_template, request
import pymysql
import re

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Database class to open a new DB connection
class Database:
    def __init__(self,data_base):
        #Credentials
        self.db = data_base
        host = "192.168.56.132"
        user = "brendan"
        password = "1234"
        #Connect
        self.con = pymysql.connect(host=host, user=user, password=password, db=self.db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        print("connected to database")

    #class method to query DB table
    #tables are: Great_Swords, Sword_Shields, Dual_Blades, Long_Swords, Hammers
    #list_armor
    def list_Weapons(self,table):
        self.cur.execute("SELECT * FROM "+table)
        result = self.cur.fetchall()
        return result
    

    def piece_detail(self,table,Name):
        self.cur.execute("SELECT * FROM "+table+" WHERE Name = '"+Name+"'")
        result = self.cur.fetchall()
        return result


#Pages
#Homepage
@app.route('/')
def main():
    db = Database("Weapons")
    result1 = db.list_Weapons("Great_Swords")
    result2 = db.list_Weapons("Sword_Shields")
    result3 = db.list_Weapons("Dual_Blades")
    result4 = db.list_Weapons("Long_Swords")
    result5 = db.list_Weapons("Hammers")
    return render_template("selectWeapons.htm",Great_Swords = result1,Sword_Shields = result2,Dual_Blades = result3,Long_Swords = result4,Hammers = result5)

@app.route('/',methods=['POST'])
def showTables():
    #Get current value of each dropdown box
    GSName = re.sub("\d", "", request.form.get('GSName')).replace(',', '')
    SSName = re.sub("\d", "", request.form.get('SSName')).replace(',', '')
    DBName = re.sub("\d", "", request.form.get('DBName')).replace(',', '')
    LSName = re.sub("\d", "", request.form.get('LSName')).replace(',', '')
    HName = re.sub("\d", "", request.form.get('HName')).replace(',', '')

    #Specify db and query tables for dropdown boxes
    db = Database("Weapons")
    result1 = db.list_Weapons("Great_Swords")
    result2 = db.list_Weapons("Sword_Shields")
    result3 = db.list_Weapons("Dual_Blades")
    result4 = db.list_Weapons("Long_Swords")
    result5 = db.list_Weapons("Hammers")
    #Select specified armor piece from each table
    details1 = db.piece_detail("Great_Swords",GSName)
    details2 = db.piece_detail("Sword_Shields",SSName)
    details3 = db.piece_detail("Dual_Blades",DBName)
    details4 = db.piece_detail("Long_Swords",LSName)
    details5 = db.piece_detail("Hammers",HName)


    return render_template("selectWeapons.htm",Great_Swords = result1,Sword_Shields = result2,Dual_Blades = result3,Long_Swords = result4,Hammers = result5,
    SelectedGreatSword = details1,SelectedSwordShield = details2,SelectedDualBlade = details3,SelectedLongSword = details4,SelectedHammer = details5)

#Great Sword table
@app.route('/Great-Swords')
def showGreatSwords():
    db = Database("Weapons")
    pieces = db.list_Weapons("Great_Swords")
    return render_template('Weapon-Great-Sword.htm',result = pieces)

#Sword & Shield table
@app.route('/Sword-Shields')
def showSwordShields():
    db = Database("Weapons")
    pieces = db.list_Weapons("Sword_Shields")
    return render_template('Weapon-Sword-Shield.htm',result = pieces)

#Arm pieces table
@app.route('/Dual-Blades')
def showDualBlades():
    db = Database("Weapons")
    pieces = db.list_Weapons("Dual_Blades")
    return render_template('Weapon-Dual-Blade.htm',result = pieces)

#Waist pieces table
@app.route('/Long-Swords')
def showLongSwords():
    db = Database("Weapons")
    pieces = db.list_Weapons("Long_Swords")
    return render_template('Weapon-Long-Sword.htm',result = pieces)

#Leg pieces table
@app.route('/Hammers')
def showHammers():
    db = Database("Weapons")
    pieces = db.list_Weapons("Hammers")
    return render_template('Weapon-Hammer.htm',result = pieces)

if __name__ == "__main__":
    app.run()