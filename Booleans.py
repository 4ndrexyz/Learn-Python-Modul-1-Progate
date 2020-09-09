# 1. True dan False

score = 100
if score == 100:
  print('Bagus!')
# output = Bagus!

  
score = 100
print(score == 100)
# output = True

# ----------------------------

# 2. Booleans

# True adalah nilai tipe data boolean.
# Tipe data boolean hanya mempunyai dua nilai, True dan False. 
# True akan muncul jika kondisi dipenuhi, dan False jika tidak.
# Perlu diingat bahwa Anda harus menulis huruf pertama True dan False dalam huruf kapital.

print(3 == 3)  # output = True
print(3 == 5)  # output = False

# ----------------------------

# 3. Statement If dan Nilai Boolean

# Code statement if dapat dijalankan apabila memenuhi kondisi True, dan tidak dapat dijalankan apabila memenuhi kondisi False.

score = 100
if score == 100:    # True
  print('Bagus!')
# output = Bagus!


score == 50
if score == 100:
  print('Bagus!')
# output = (kosong)     # <- karena kondisinya false, code di dalam If TIDAK di jalankan  

# ----------------------------

# Operator Perbandingan (<, <=, >, >=)

# Ada operator-operator lain yang dapat digunakan untuk membandingkan nilai. 
# Seperti dalam matematika, Anda dapat menggunakan < dan > untuk membandingkan angka.
# Anda juga dapat menggunakan >= dan <= jika perbandingannya inklusif. 

x < y     # True jika x lebih kecil dari y
x <= y    # True jika x lebih kecil dari atau sama dengan y
x > y     # True jika x lebih besar dari y
x >= y    # True jika x lebih besar dari atau sama dengan y

2 > 6         # ... False
4 + 2 >= 6    # ... True
8 / 4 < 5     # ... True 
2 * 5 <= 9    # ... False

# ----------------------------

# 4. Ringkasan Operator Perbandingan

==   # True jika nilai di kiri dan kanan adalah setara
!=   # True jika TIDAK setara
<    # True jika nilai di kanan lebih besar dari nilai di kiri
<=   # True jika nilai di kanan lebih besar dari atau sama dengan nilai di kiri
>    # True jika nilai di kanan lebih kecil dari nilai di nilai
>=   # True jika nilai di kanan lebih kecil dari atau sama dengan nilai di kiri
