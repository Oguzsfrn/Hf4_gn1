ds = open("rehber.txt", "a")
ad = input("Adınızı girin:\t")
no = input("Numaranızı:\n")

ds.write(f"{ad}: {no}\n")