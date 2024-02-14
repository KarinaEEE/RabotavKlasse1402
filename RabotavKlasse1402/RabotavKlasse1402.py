#rabota v klasse 14.02

from random import *
from string import *
# while True:
#     try:
#         N=int(input("Mitu rida loome? "))
#         break
#     except:
#         print("Vale tüüp")
# while True:
#     try:
#         S=input("Mis sümbol korrutame? ")
#         if S in punctuation:
#             break
#         else:
#             print("Vale sümbol")
#     except:
#         print("Vale sümbol")
# for i in range(N):
#     print(randint(1,25)*S)
 
#1
# Indeksid=["Tallinn","Narva","Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa","Läane-Virumaa","Jõegevamaa","Tartu","Põlvamaa","Võrumaa","Valgamaa","Harjumaa","Hiiumaa","Saaremaa"]
# while True:
#     indeks=input("Indeks: ")
#     if len(indeks)==5 and indeks.isdigit() and indeks[0]!="0":
#         print("Sa elad piirkonnas",Indeksid[int(indeks[0])-1])
#         if indeks[0]=="1" or indeks[0]=="2" or indeks[0]=="3":
#             print("Kodus")
#         else:
#             print("Maskid")
#     else:
#         print("Sisesta indeks uuesti: ")

# #5

# rida=[] 
# N=randint(2,25)
# for i in range(N):
#     rida.append(choice(ascii_uppercase))
# print(rida)
# n=int(input("Mitu paari vahetada? "))
# if len(rida)//2>=n:
#     for i in range(n):
#         abi=rida[1]
#         rida[i]=rida[len(rida)-1-i]

        
       
#6

# arvud= [1,2,3,4,5,6,122,44,5]
# print(arvud)
# max_=max(arvud)
# indeks=arvud.index(max_)
# max_=int(max_/len(arvud))
# arvud[indeks]=max_ 
# print(arvud)



#7 самостоятельно

# numbrid = [5, -3, 8, -2, 0, -10]

# sorted_asc= sorted(numbrid,key=abs)
# sorted_desc= sorted(numbrid,key=abs, reverse=True)

# print("Algne numbriloend:", numbrid)
# print("Sorteeritud kasvavalt absoluutväärtuse järgi:", sorted_asc)
# print("Sorteeritud kahanevalt absoluutväärtuse järgi:", sorted_desc)











#9 самостоятельно

# nimi = input("Sisestage oma nimi: ")

# if not nimi.isalpha():
#     print("Nimes võivad olla ainult tähed.")
#     exit()
# print("Tere,", nimi.capitalize(), "!")
# kogu_tähemärke = len(nimi)
# vokaalid = 0
# kaashäälikud = 0
# for täht in nimi:
#     if täht.lower() in "aeiouäöü":
#         vokaalid += 1
#     else:
#         kaashäälikud += 1

# print("Tähemärkide arv nimis:", kogu_tähemärke)
# print("Vokaalide arv nimis:", vokaalid)
# print("Kaashäälikute arv nimis:", kaashäälikud)

# sorteeritud_tähemärgid = sorted(set(nimi.lower()))
# print("Nimis olevad tähed tähestikulises järjekorras:", ", ".join(sorteeritud_tähemärgid))

#12 самостоятельно

# import random

# numbers=[random.randint(1, 100) 
# for i in range(10)]

# print("Alguses loend:",numbers)

# min_index=numbers.index(min(numbers))
# max_index=numbers.index(max(numbers))

# numbers[min_index],numbers[max_index]=numbers[max_index],numbers[min_index]

# print("Pärast vahetust:", numbers)


# import random

# numbers=[random.randint(1, 100) 
#          for i in range(10)]

# print("Alguses loend:", numbers)

# while True:
#     min_index=numbers.index(min(numbers))
#     max_index=numbers.index(max(numbers))
    
#     numbers[min_index],numbers[max_index]=numbers[max_index],numbers[min_index]
    
#     if min(numbers)!= max(numbers):
#         break

# print("Pärast vahetust:", numbers)


