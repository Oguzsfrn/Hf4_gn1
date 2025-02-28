import os
print("Aktif Klasorler:", os.getcwd())
liste = os.listdir()
for x in liste:
    if os.path.isfile(x)==True: durum ="Dosya"
    else: durum = "Klasor"
    print(f"{x}\t{durum}")