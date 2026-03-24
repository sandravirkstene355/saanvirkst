import re
with open("klienti.txt","r",encoding="utf-8")as fails:
   dati=fails.read()#virkne

epasti=re.findall(r"\w+@\w+\.\w+",dati)
#epasti=re.findall(r".+@.+\..",dati)
print(epasti)#saraksts
print(len(epasti))

telefoni=re.findall(r"\d{8}",dati)
#telefoni=re.findall(r"\b\d{8}\b",dati)
print(telefoni)#saraksts

aizvietots=re.sub(r"\d{8}","📱",dati)
print(aizvietots)#virkne

datne=open("klienti_anon.txt","w",encoding="utf-8")
datne.write(aizvietots)
datne.close()

