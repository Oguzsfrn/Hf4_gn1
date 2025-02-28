import os, time
for a in range(10): os.mkdir(f"Klasör{a}")
time.sleep(3)
for a in range(10): os.rmdir(f"Klasör{a}")