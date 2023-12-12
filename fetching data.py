import requests
from bs4 import BeautifulSoup

def fetchdata(url,path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

pro = requests.get("https://api.ipify.org?format=json")

url='https://www.scrapethissite.com/'

fetchdata(url,"sample.html")

with open("sample.html",'r') as f:
    html_doc=f.read()
soup = BeautifulSoup(html_doc,'html.parser')

#code
#print(soup.prettify())

#title
print("\nTITLE \t TYPE")
print(soup.title.string,"\t",type(soup.title.string))


#links and texts
l1=[]
l2=[]
for link in soup.find_all('a'):
    l1.append(link.get('href'))
    l2.append(link.get_text())

#link ids
l=[]
for i in soup.find_all('a'):
    l.append(i.get('id'))

print("\nLINKS \t LINK ID\t Text\n")
for i in range(0,len(l)):
    print(l1[i],"\t",l[i],"\t",l2[i])