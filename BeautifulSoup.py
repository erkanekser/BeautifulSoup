import requests
from bs4 import BeautifulSoup
Searching=input("The word you want to search: ")

urun_linki=input("Link to the product you want to search: ")

r=requests.get("https://www.n11.com/arama?q="+str(Searching))

soup=BeautifulSoup(r.text,"html.parser")


first_link=soup.find_all("a",attrs={"href":urun_linki}) #html kodunda ürün linki olan kısmı aldık.
first_link2=str(first_link)
if 'data-id' in first_link2:
    result=first_link2.find('data-id')
    urun_id=(first_link2[result+9:result+18]) #Ürün id'si bulundu.

second_link=soup.find_all("div",attrs={"id":("p-"+urun_id)}) #ürün id sinden data-position'a geçmek için bu kod parçasını çektik
second_link2=str(second_link) 

print("---------\n")

if 'data-position' in second_link2:
    result2=second_link2.find('data-position')
    urun_position=(second_link2[result2+15:result2+18])
    print("The product you are looking for is "+urun_position+".") #Ürün pozisyonu bulundu.
