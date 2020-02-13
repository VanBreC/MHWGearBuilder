import requests
from bs4 import BeautifulSoup

def scrape_charms(URL, filename):

    #Open file
    csv = open(filename,'w')

    #Get the html using the URL
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')

    #Select the table and then the individual rows of the table
    table = soup.find('table', class_='table table-sm')
    rows = table.find_all('tr')

    #Iterate through each row
    for row in rows:
        columns = row.find_all('td')

        #Name
        name = columns[0].text

        #Rarity
        rarity = columns[1].text

        #Skills
        divs = columns[2].find_all('div') #Skill name is stored in <div></div>
        skill_list = []
        for div in divs:
            skill = div.text
            s = skill.replace(' Lv','')
            skill_list = skill_list + [s.strip()]

        #Write Charm name, rarity, and skills to csv
        if len(skill_list) == 2:
            csv.write(name.strip() + "," + rarity.strip() + ","+ skill_list[0] +","+ skill_list[1]+"\n")
            #print(name.strip() + "," + rarity.strip() + ","+ skill_list[0] +","+ skill_list[1])
        if len(skill_list) == 1:
            csv.write(name.strip() + "," + rarity.strip() + "," + skill_list[0]+",None\n")
            #print(name.strip() + "," + rarity.strip() + "," + skill_list[0]+",None")
    
    csv.close()

#Run
URL = 'https://mhworld.kiranico.com/armorseries'
filename = 'Charms.csv'
scrape_charms(URL,filename)