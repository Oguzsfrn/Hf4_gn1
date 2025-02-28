ds = open("rehber.txt", "a")
ad = input("Adınızı girin:\n")
no = input("Numaranızı:\n")

ds.write(f"{ad}: {no}\n")