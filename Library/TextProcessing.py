#REGEX LIBRARY
#Penjelasan: ertama adalah sekumpulan library yang bertujuan untuk melakukan pemrosesan 
# teks dan menyederhanakan serta mempercepat tugas-tugas pemrosesan teks.

import re     # Import modul regex
 
pola= '^a...s$'
string_tes= 'abyss'
hasil= re.match(pola, string_tes)
 
if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.") 
