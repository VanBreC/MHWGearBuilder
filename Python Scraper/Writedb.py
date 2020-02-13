import pymysql

def insert_armor(db,table,filename):

    #Set up DB connection
    host = "192.168.56.117"
    user = "remjamd"
    password = "password1"
    database = db

    connection = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    #Read lines from csv
    csv = open(filename,'r')
    lines = csv.readlines()

    #Insert each line to DB table
    for line in lines:
        column = line.split(",")
        query = ("INSERT INTO " + table + " (name,rarity,skill1,skill2,defense,slot1,slot2,slot3,firedef,waterdef,thunderdef,icedef,dragondef)" 
        + " VALUES('"
        + column[0] + "'," + (column[1]) + ",'" + (column[2]) + "','" + column[3] + "'," + column[4] + ",'" + column[5] + "','" 
        + column[6] + "','"+ column[7] + "','"+ column[8] + "',"+ column[9] + ","+ column[10] + ","+ column[11] + ","+ column[12] 
        + ")")
    
        cur.execute(query)

    connection.commit()
    connection.close()

    csv.close()


#Run
db = "armor"
#table = "head"
#filename = "Head_Pieces.csv"

#insert_armor(db,table,filename)

table = "chest"
filename = "Chest_Pieces.csv"
#insert_armor(db,table,filename)

table = "arms"
filename = "Arm_Pieces.csv"
#insert_armor(db,table,filename)

table = "waist"
filename = "Waist_Pieces.csv"
insert_armor(db,table,filename)

table = "legs"
filename = "Leg_Pieces.csv"
insert_armor(db,table,filename)
