#LUAS
def hitung_luas_belah_ketupat(d1, d2):
  return 0.5 * d1 *d2
def luas ():
  print ("Pengertian maksud dari panjang diagonal pertama dan diagonal kedua ")
  print ("Diagonal adalah garis yang menghubungkan dua sudut yang berlawanan pada belah ketupat")
  d1 = float(input("masukkan nilai sisi diagonal pertama: "))
  d2 = float(input("masukkan nilai sisi diagonal kedua: "))
  luas = hitung_luas_belah_ketupat(d1, d2)
  print(f"luas belah ketupat adalah: {luas}")
  
if __name__ == "__main__":
  luas()
  
#KELILING
def hitung_keliling_belah_ketupat(a, b, c, d):
  return a + b + c + d
def keliling ():
  a = float(input("masukkan nilai sisi: "))
  b = float(input("masukkan nilai sisi : "))
  c = float(input("masukkan nilai sisi : "))  
  d = float(input("masukkan nilai sisi : "))
  keliling = hitung_luas_belah_ketupat(a, b, c, d)
  print(f"luas belah ketupat adalah: {keliling}")
  
if __name__ == "__main__":
  keliling()