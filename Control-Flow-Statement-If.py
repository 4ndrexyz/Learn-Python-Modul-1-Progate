# Statement If

# Dengan menggunakan statement if, Anda dapat menulis code yang dapat dijalankan hanya jika kondisi dipenuhi.
# Anda dapat membuat statement if dengan menulis if, diikuti conditional expression dan tanda titik dua :.
# Code di baris berikutnya akan berjalan jika kondisi benar.

score = 100
if score == 100:      #  <- jika kondisinya adalah true dan jangan lupa gunakan titik dua (:) 
  print('Bagus!')     #  <- jalan kan kode ini
# output = Bagus!        <- karena kodisi adalah True, pesan ini dicetak

# ---------------------------------------

# Statement If (Conditional Expression)

# Ada banyak operator untuk membuat conditional expression.
# Mari kita lihat operator perbandingan, yang dapat digunakan untuk membandingkan kesetaraan kedua nilai.
# Kita dapat menggunakan == untuk mengetahui jika kedua nilai sama, dan != untuk mengetahui jika kedua nilai tidak sama.

# Operator Perbandingan 
x == y ...           # True jika nilai di kiri dan kanan setara
x != y ...           # True jika nilai di kiri dan kanan tidak setara

score = 100
if score == 100:     # (score == 100:) adalah conditional expression, (==) membandingkan dua nilai
  .
  .
  .
  
# ---------------------------------------

# Statement If (Identasi)

# Anda harus mengindentasi code Anda jika menulis statement if.
# Code yang diindentasi di bawah statement if hanya akan berjalan jika kondisi benar. 
# Bagian yang tidak diindentasi akan berjalan tidak peduli kondisi benar atau tidak.
# identasikan code secara konsisten (4 spasi atau 1 tab)

score = 50
if score == 100:
  ... print('Bagus!')                             # di masukkan kedalam statement if
  ... print('Petahankan pekerjaan yang baik')     # di masukkan kedalam statement if  
# output = (kosong)   <-  kerena kondisinya false, tidak ada yang di cetak.


score = 50
if score == 100:
  ... print('Bagus!')                             # di masukkan kedalam statement if
print('Petahankan pekerjaan yang baik')           # tidak di masukkan kedalam statement if
# output = Petahankan pekerjaan yang baik   <- ini akan selalu di cetak.






