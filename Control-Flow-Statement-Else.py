# Else 

#Dengan menggunakan pernyataan else, Anda dapat menambahkan code yang ingin Anda jalankan jika kondisi statement if adalah False.

score = 50
if score == 100:
  ... print('Bagus!)
else:
  print('Belajar Lebih Baik!')       # <- dijalankan jika conditional expression bernilai False
# output = Belajar Lebih Baik!

# ----------------------------------

# Elif (1)

score = 70
if score == 100:
  print('Bagus!')
elif score >= 60:
  print('Tidak Buruk..')     # <- code ini di jalankan
else:
  print('Belajar Lebih Baik!')
# output = Tidak Buruk..

# ----------------------------------

# Elif (2)

# Anda dapat menambah elif sebanyak yang Anda inginkan.
# Akan tetapi, hanya code pada kondisi pertama yang dipenuhi yang akan dijalankan.

score = 100
if score == 100:           # Control Flow berhenti ketika kondisi bernilai True
  print('Bagus!')
elif score >= 60:
  print('Tidak Buruk')     # <- ini tidak akan di jalankan walaupun kondisinya true
elif score > 40:
  .
  .
else:
  .
  .
# output = Bagus!  

# ----------------------------------

# and

# Anda dapat menggunakan operator and untuk menggabungkan kondisi. 
# Sebagai contoh, Kondisi1 and Kondisi2 akan menampilkan True ketika kedua kondisi terpenuhi.

# True and True   = True
# True and False  = False
# False and True  = False
# False and False = False

hour = 7
if hour > 6 and hour < 8:      # (hour > 6) True dan (hour < 8) True
  print('Pagi!')
# output = Pagi!

# ----------------------------------

# or

# Anda dapat menggunakan operator or pada cara yang sama.
# Kondisi1 or Kondisi2 akan menampilkan True jika salah satu Kondisi1 atau Kondisi2 benar.
# Ini berarti kondisi gabungan akan menampilkan True jika setidaknya satu conditional expression True.

# True or True   = True
# True or False  = True
# False or True  = True
# False or False = False

hour = 12
if hour == 11 or hour == 12:
  print('Makan!')
# output = Makan!

# ----------------------------------

# not

# Dengan menggunakan not, Anda dapat menegaskan suatu kondisi.
# Ini artinya False akan muncul jika conditional expression benar dan True akan muncul jika salah.

hour = 9
if not hour == 12:
  print('Bukan siang')
# output = Bukan siang

# ----------------------------------

# Merantai Operator Perbandingan

# Anda dapat menulis ulang kondisi and yang menggunakan variable yang sama! 
# Hal ini disebut merantai perbandingan operator. 

hour = 7
if hour > 6 and hour < 8:     # <- True
  print('Pagi!')
# output = Pagi!


hour = 7
if 6 < hour < 8:              # <- dapat merantai operator tanpa menggunakan and
   print('Pagi!')
# output = Pagi!   
 





