import requests
from bs4 import BeautifulSoup

def scrape_decorations(URL, filename):

    #Open file
    csv = open(filename,'w')

    #Get the html using the URL
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')

    #Select the table and then the individual rows of the table
    table = soup.find('table', class_='table table-sm')
    body = table.find('tbody')
    rows = body.find_all('tr')

    #Iterate through each row
    for row in rows:
        columns = row.find_all('td')

        #Decoration name + size
        name = columns[0].text

        #find the size by splitting the string
        list1 = name.split()
        #Deco size will equal the last element in the list
        size = list1[-1]

        #print(name + "," + size)

        #Skills
        divs = columns[1].find_all('div') #Skill name is stored in <div></div>
        skill_list = []
        for div in divs:
            skill = div.text
            skill_list = skill_list + [skill]
        
        #Write Name, Size, Skill 1, Skill 2 to csv
        if len(skill_list) == 2:
            csv.write(name.strip() + "," + size + ","+ skill_list[0] +","+ skill_list[1]+"\n")

        if len(skill_list) == 1:
            csv.write(name.strip() + "," + size + "," + skill_list[0]+",None\n")
            
    csv.close()
            




    


#Run
URL = 'https://mhworld.kiranico.com/decorations'
filename = 'Decorations.csv'

scrape_decorations(URL,filename)
