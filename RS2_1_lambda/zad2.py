

# 1_map
nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda niz: len(niz) ** 2, nizovi))
print("kvadrirane_duljine: ",kvadrirane_duljine)


#2_filter
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = list(filter(lambda br: br > 5, brojevi))
print("veci od 5: ",veci_od_5) 


#3_dict transform kvadrat
brojevi = [10, 5, 12, 15, 20]
transform = dict(map(lambda br: (br, br ** 2), brojevi))
print("dict transform kvadrat:\n",transform)


#4_punoljetni
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda x: x["godine"] >= 18, studenti))
print("svi studenti punoljetni: ",svi_punoljetni) # False


#5_min

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
# min_duljina = 7
duge_rijeci = list(filter(lambda x: len(x) > min_duljina, rijeci))
# print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']
print(duge_rijeci)