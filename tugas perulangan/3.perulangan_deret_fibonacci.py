# input jumlah deret
n = 10

# inisialisasi dua angka pertama
a = 1
b = 1


print(a,end='') # cetak angka pertama 
print(a,end='') # cetak angka kedua

# proses fibonacci
for i in range(2,n): # range(2,10) karena dua angka sudah dicetak
    c=a + b # angka selanjutnya adalah penjumlahan 2 angka sebelumnya
    print(c,end='')
    # ufdate nilai untuk literasi selanjutnya
    a=b
    b=c