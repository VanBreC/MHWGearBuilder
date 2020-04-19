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
    result6 = db.list_Weapons("Hunting_Horns")
    result7 = db.list_Weapons("Lances")
    result8 = db.list_Weapons("Gun_Lances")
    result9 = db.list_Weapons("Switch_Axes")
    result10 = db.list_Weapons("Charge_Blades")
    result11 = db.list_Weapons("Insect_Glaives")
    return render_template("selectWeapons.htm",Great_Swords = result1,Sword_Shields = result2,Dual_Blades = result3,Long_Swords = result4,Hammers = result5,Hunting_Horns = result6,Lances = result7,Gun_Lances = result8,Switch_Axes = result9,Charge_Blades = result10,Insect_Glaives = result11)

@app.route('/',methods=['POST'])
def showTables():
    #Get current value of each dropdown box
    GSName = re.sub("\d", "", request.form.get('GSName')).replace(',', '')
    SSName = re.sub("\d", "", request.form.get('SSName')).replace(',', '')
    DBName = re.sub("\d", "", request.form.get('DBName')).replace(',', '')
    LSName = re.sub("\d", "", request.form.get('LSName')).replace(',', '')
    HName = re.sub("\d", "", request.form.get('HName')).replace(',', '')
    HHName = re.sub("\d", "", request.form.get('HHName')).replace(',', '')
    LName = re.sub("\d", "", request.form.get('LName')).replace(',', '')
    GLName = re.sub("\d", "", request.form.get('GLName')).replace(',', '')
    SAName = re.sub("\d", "", request.form.get('SAName')).replace(',', '')
    CBName = re.sub("\d", "", request.form.get('CBName')).replace(',', '')
    IGName = re.sub("\d", "", request.form.get('IGName')).replace(',', '')

    #Specify db and query tables for dropdown boxes
    db = Database("Weapons")
    result1 = db.list_Weapons("Great_Swords")
    result2 = db.list_Weapons("Sword_Shields")
    result3 = db.list_Weapons("Dual_Blades")
    result4 = db.list_Weapons("Long_Swords")
    result5 = db.list_Weapons("Hammers")
    result6 = db.list_Weapons("Hunting_Horns")
    result7 = db.list_Weapons("Lances")
    result8 = db.list_Weapons("Gun_Lances")
    result9 = db.list_Weapons("Switch_Axes")
    result10 = db.list_Weapons("Charge_Blades")
    result11 = db.list_Weapons("Insect_Glaives")
    #Select specified armor piece from each table
    details1 = db.piece_detail("Great_Swords",GSName)
    details2 = db.piece_detail("Sword_Shields",SSName)
    details3 = db.piece_detail("Dual_Blades",DBName)
    details4 = db.piece_detail("Long_Swords",LSName)
    details5 = db.piece_detail("Hammers",HName)
    details6 = db.piece_detail("Hunting_Horns",HHName)
    details7 = db.piece_detail("Lances",LName)
    details8 = db.piece_detail("Gun_Lances",GLName)
    details9 = db.piece_detail("Switch_Axes",SAName)
    details10 = db.piece_detail("Charge_Blades",CBName)
    details11 = db.piece_detail("Insect_Glaives",IGName)


    return render_template("selectWeapons.htm",Great_Swords = result1,Sword_Shields = result2,Dual_Blades = result3,Long_Swords = result4,Hammers = result5,Hunting_Horns = result6,Lances = result7,Gun_Lances = result8,Switch_Axes = result9,Charge_Blades = result10,Insect_Glaives = result11,
    SelectedGreatSword = details1,SelectedSwordShield = details2,SelectedDualBlade = details3,SelectedLongSword = details4,SelectedHammer = details5,SelectedHuntingHorn = details6,SelectedLance = details7,SelectedGunLance = details8,SelectedSwitchAxe = details9,SelectedChargeBlade = details10,SelectedInsectGlaive = details11)

#Great Sword table
@app.route('/Great-Swords')
def showGreatSwords():
    db = Database("Weapons")
    pieces = db.list_Weapons("Great_Swords")
    return render_template('Weapon-Great-Sword.htm',result = pieces)
@app.route('/Great-Swords',methods=['POST'])
def GSDamage():
    TrueDamage = request.form.get('TD')
    print("True Damage is: " + TrueDamage)
    Sharpness = request.form.get('Sharp')
    print("Sharpness Color is: " + Sharpness)
    AttackValue = request.form.get('AV')
    print("Attack Value is: " + AttackValue)
    MonsterArmor = request.form.get('MA')
    print("Monster Armor is: " + MonsterArmor)
    if Sharpness == "Red":
        Sharpness = 0.5
    elif Sharpness == "Orange":
        Sharpness = 0.75
    elif Sharpness == "Yellow":
        Sharpness = 1
    elif Sharpness == "Green":
        Sharpness = 1.05
    elif Sharpness == "Blue":
        Sharpness = 1.2
    elif Sharpness == "White":
        Sharpness = 1.32
    CalculatedDamage = round(int(TrueDamage)*Sharpness*(int(AttackValue)/100)*(int(MonsterArmor)/100))
    print("Calculated Damage: ", CalculatedDamage)
    db = Database("Weapons")
    pieces = db.list_Weapons("Great_Swords")
    return render_template('Weapon-Great-Sword.htm',result = pieces,DR = CalculatedDamage)


#Sword & Shield table
@app.route('/Sword-Shields')
def showSwordShields():
    db = Database("Weapons")
    pieces = db.list_Weapons("Sword_Shields")
    return render_template('Weapon-Sword-Shield.htm',result = pieces)

#Dual Blades table
@app.route('/Dual-Blades')
def showDualBlades():
    db = Database("Weapons")
    pieces = db.list_Weapons("Dual_Blades")
    return render_template('Weapon-Dual-Blade.htm',result = pieces)

#Long Sword table
@app.route('/Long-Swords')
def showLongSwords():
    db = Database("Weapons")
    pieces = db.list_Weapons("Long_Swords")
    return render_template('Weapon-Long-Sword.htm',result = pieces)

#Hammer table
@app.route('/Hammers')
def showHammers():
    db = Database("Weapons")
    pieces = db.list_Weapons("Hammers")
    return render_template('Weapon-Hammer.htm',result = pieces)

#Hunting Horn table
@app.route('/Hunting-Horns')
def showHuntingHorns():
    db = Database("Weapons")
    pieces = db.list_Weapons("Hunting_Horns")
    return render_template('Weapon-Hunting-Horn.htm',result = pieces)

#Lance table
@app.route('/Lances')
def showLances():
    db = Database("Weapons")
    pieces = db.list_Weapons("Lances")
    return render_template('Weapon-Lance.htm',result = pieces)

#Gun Lance table
@app.route('/Gun-Lances')
def showGunLances():
    db = Database("Weapons")
    pieces = db.list_Weapons("Gun_Lances")
    return render_template('Weapon-Gun-Lance.htm',result = pieces)

#Switch Axe table
@app.route('/Switch-Axes')
def showSwitchAxes():
    db = Database("Weapons")
    pieces = db.list_Weapons("Switch_Axes")
    return render_template('Weapon-Switch-Axe.htm',result = pieces)

#Charge Blade table
@app.route('/Charge-Blades')
def showChargeBlades():
    db = Database("Weapons")
    pieces = db.list_Weapons("Charge_Blades")
    return render_template('Weapon-Charge-Blade.htm',result = pieces)

#Insect Glaive table
@app.route('/Insect-Glaives')
def showInsectGlaives():
    db = Database("Weapons")
    pieces = db.list_Weapons("Insect_Glaives")
    return render_template('Weapon-Insect-Glaive.htm',result = pieces)

if __name__ == "__main__":
    app.run()