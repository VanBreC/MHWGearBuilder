import requests
from bs4 import BeautifulSoup

def scrape_skills(URL, filename):

    #Open file
    txt_file = open(filename,'w')

    #Get the html using the URL
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')

    #Select the table and then the individual rows of the table
    table = soup.find('table', class_='table table-lightborder table-sm')
    body = table.find('tbody')
    rows = table.find_all('tr')

    for row in rows:
        tds = row.find_all('td')

        td_list = []
        for td in tds:
            td_list = td_list + [td.text]
        
        if len(td_list) == 2:
            #print(td_list[0]+","+td_list[1])
            txt_file.write(td_list[0]+","+td_list[1]+"\n")

        if len(td_list) == 1:
            #print(td_list[0])
            txt_file.write(td_list[0]+"\n")

    txt_file.close()

#Reformat the text file to csv
def format_csv(file1,file2):

    text_file = open(file1,'r')
    csv = open(file2,'w')

    skill = []
    lines = text_file.readlines()
    for line in lines:
        level = 'Lv' in line
        if level == True:
            y = line.split(",")
            del y[0]
            temp = ""
            for i in y:
                    temp = temp + str(i).strip("\n")
            skill = skill + [temp]
            continue
            
        if level == False:
            x = ""
            for i in skill:
                x = (x + str(i) + ",")
            csv.write(x + "\n")
            skill = []
            skill = skill + [line.strip("\n")]
            continue
    
    text_file.close()
    csv.close()



#Run
URL = 'https://mhworld.kiranico.com/skilltrees'
filename = 'skillz.txt'

#scrape_skills(URL,filename)

csv_file = 'Skills.csv'
format_csv(filename,csv_file)