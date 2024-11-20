

# kvadriraj
kvadriraj = lambda x: x**2
print("kvadriraj: ", kvadriraj(5))


# zbroji pa kvadriraj
zbroji_pa_kvadriraj = lambda a, b: (a+b)**2
print("zbroji pa kvadriraj: ", zbroji_pa_kvadriraj(2,3))


#kvadriraj duljinu
kvadriraj_duljinu = lambda niz: len(niz)**2
print("kvadriraj duljinu: ", kvadriraj_duljinu([1, 2, 3]))

#pomnozi i potenciraj
pomnozi_i_potenciraj = lambda x, y: (y*5)**x
print("pomnozi i potenciraj: ", pomnozi_i_potenciraj(2, 1))

#paran broj
paran_broj = lambda x: x % 2 == 0 
print("paran_broj: ", paran_broj(3))
