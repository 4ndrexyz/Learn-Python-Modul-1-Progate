# - Perbedaan Tipe-Tipe Data

# Tipe yang berbeda memiliki sifat yang berbeda.
# Contohnya, print(5 + 7) menghitung penjumlahannya sedangkan print('5' + '7') menggabungkan string.

print(5 + 7)       # kalkulasi numerik
# output = 12

print('5' + '7')   # penggabungan string
# output = 57

# ----------------------------------------------------

# - Konversi Tipe:str()

# tidak bisa menggabungkan tipe string dan integer
price = 3
print('Harga apel' + price + 'dolar')    # string + integer + string
# output = Error!

# ----------------------------------------------------

# - Konversi Tipe:int()

count = '3'
price = 100
total_price - price * int(count)      # ubah ke integer
print(total_price)
# output = 300
