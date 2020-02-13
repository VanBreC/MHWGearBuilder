import requests
from bs4 import BeautifulSoup

def scrape_armor(URL,filename):

    csv = open(filename,'w')
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')

    #Selecting the armor html table
    table = soup.find('table', class_='wiki_table sortable')
    #Making each row of the table it's own object
    rows = table.find_all('tr')

    #Iterate through each row and extract the needed data (Armor Name, Rarity, Skills, Defense, Slots, Elemental Defenses)
    for row in rows:
        columns = row.find_all('td')

        #Armor name
        armor = columns[0].find('a', class_="wiki_link")
        if armor == None or armor.text == "": #if the selected value is null or a empty string list the armor as "Null"
            armor_name = "Null"
        else:
            armor_name = armor.text
        
        #Rarity
        rarity = columns[1].text

        #Skills
        skills = columns[2].text

        #Defense
        defense = columns[3].text

        #Decoration Slots
        slots = columns[4].find_all('img')

        slots_list = []
        #Generate a list of the armor piece's decoration slots based on the value of 'src'
        for slot in slots:
            link = slot['src']
            if link == '/file/Monster-Hunter-World/decoration_level_4_mhw_wiki.png':
                slots_list = slots_list + ['Level 4']
            if link == '/file/Monster-Hunter-World/gem_level_3.png':
                slots_list = slots_list + ['Level 3']
            if link == '/file/Monster-Hunter-World/gem_level_2.png':
                slots_list = slots_list + ['Level 2']
            if link == '/file/Monster-Hunter-World/gem_level_1.png':
                slots_list = slots_list + ['Level 1']
            
        #Fill out blank spots (Each armor piece can have up to 3 decoration slots)
        if len(slots_list) == 2:
            slots_list = slots_list + ['None']
        if len(slots_list) == 1:
            slots_list = slots_list + ['None']
            slots_list = slots_list + ['None']
        if len(slots_list) == 0:
            slots_list = slots_list + ['None']
            slots_list = slots_list + ['None']
            slots_list = slots_list + ['None']

        slot1 = slots_list[0]
        slot2 = slots_list[1]
        slot3 = slots_list[2]

        #Elemental Defense
        fire_def = columns[5].text
        water_def = columns[6].text
        thunder_def = columns[7].text
        ice_def = columns[8].text
        dragon_def = columns[9].text

        #print(armor_name + ", " + rarity + ", " + skills + ", " + defense + ", " + slot1 + ", " + slot2 + ", " + slot3
        #+ ", " + fire_def + ", " + water_def + ", " + thunder_def + ", " + ice_def + ", " + dragon_def)

        csv.write(armor_name + "," + rarity + "," + skills + "," + defense + "," + slot1 + "," + slot2 + "," + slot3
        + "," + fire_def + "," + water_def + "," + thunder_def + "," + ice_def + "," + dragon_def + "\n")

    csv.close()

#Run
# Head    
#URL = 'https://monsterhunterworld.wiki.fextralife.com/Master+Rank+Head+Armor'
#filename = 'Head_Pieces.csv'

#Chest
#URL = 'https://monsterhunterworld.wiki.fextralife.com/Master+Rank+Chest+Armor'
#filename = 'Chest_Pieces.csv'
#scrape_armor(URL,filename)

#Arms
#URL = 'https://monsterhunterworld.wiki.fextralife.com/Master+Rank+Arms+Armor'
#filename = 'Arm_Pieces.csv'
#scrape_armor(URL,filename)

#Waist
#URL = 'https://monsterhunterworld.wiki.fextralife.com/Master+Rank+Waist+Armor'
#filename = 'Waist_Pieces.csv'
#scrape_armor(URL,filename)

#Legs
#URL = 'https://monsterhunterworld.wiki.fextralife.com/Master+Rank+Leg+Armor'
#filename = 'Leg_Pieces.csv'
#scrape_armor(URL,filename)
