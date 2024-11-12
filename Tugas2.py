def circle():
  pi = 3.14159
  radius = float(input("Masukkan Jari-jari Lingkaran : "))
  area = pi * (radius)**2
  print("Luas Lingkaran adalah", + area)

def square():
  side = float(input("Masukkan Sisi Persegi : "))
  area = side **2
  print("Luas Persegi adalah", + area)

def triangle():
  i = 0.5
  base = float(input("Masukkan Alas Segitiga : "))
  height = float(input("Masukkan Tinggi Segitiga : "))
  area = i * base * height
  print("Luas Segitiga adalah", + area)

while True :
  print("""
--- Menu ---
1. Hitung Luas Lingkaran
2. Hitung Luas Persegi
3. Hitung Luas Segitiga
4. Keluar
  """)

  select = int(input("Pilih 1/2/3/4 : "))
  if select == 1:
    circle()
  elif select == 2:
    square()
  elif select== 3:
    triangle()
  elif select == 4:
    break
  else:
    print("Tolong Pilih 1/2/3/4")
