
t = (1234, 'Hello World')
t1 = (1, 2, 3)
t2 = "a", "b", "c"        # Tanpa tanda kurung juga valid
t3 = ()                   # Tuple kosong
t4 = (5,)                 # Tuple satu elemen (perlu koma!)

# membuat tuple singleton 
satu = ('Isi',)
dua = "ini adalah tuple?",

# cek tipe datanya
print(type(satu))
print(type(dua))

# jika tidak pakai koma
satu = ('Isi')
dua = "ini adalah tuple?"

# cek tipe datanya
print(type(satu))
print(type(dua))

# membuat tuple
nama = ('Adam', 'Bachtiar', 'Maulachela')

# mengakses indeks ke 1 dari tuple
print(nama[1])

# membuat tuple
angka = (10, 20, 30, 40)

# Memotong tuple
print(angka[1:3]) 
print(angka[:2])
print(angka[2:])
