# penggabungan tuple
print((1, 2) + (3, 4))

# pengulangan tuple
print(('A',) * 3)

# cek panjang tuple
data = (1, 2, 4, 5)
print(len(data))

# cek keanggotaan tuple
print(3 in data)

t = (1, 2, (3, 4))
print(t[2][0])  # Output: 3

tuple1 = "aku", "mahasiswa", "PTI UNDIKMA"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple

print(tuple3)

# tuple berisi list
t = ([1,2,3,4], True)

print (t)