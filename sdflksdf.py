import csv

datne=open("kontakti.csv",encoding="utf-8")
saturs=list(csv.reader(datne))
datne.close()
print(saturs)

for cilveks in saturs:
    print(cilveks[0],"\t",cilveks[-1])

galvene=["vārds","uzvārds","telefons","pilsēta"]
with open("k1.csv","w",encoding="utf-8")as fails:
    c=csv.writer(fails, delimiter="\t")#atdala vienu funkciju no otras
    c.writerow(galvene)
    c.writerows(saturs)
