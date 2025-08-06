#LUAS
def hitung_luas_jajar_genjang(a, t):
  return a*t

def luas ():
  a = int(input("Masukkan panjang alas: "))
  t = int(input("Masukkan tinggi: "))
  luas = hitung_luas_jajar_genjang(a, t)
  print(f"Luas jajar genjang adalah: {luas}")
  
if __name__ == "__main__":
  luas()
  
#KELILING
def hitung_keliling_jajar_genjang(a, b, c, d):
  return a + b + c + d

def keliling ():
  a = int(input("Masukkan panjang sisi ke 1: "))
  b = int(input("Masukkan panjang sisi ke 2: "))
  c = int(input("Masukkan panjang sisi ke 3: "))
  d = int(input("Masukkan panjang sisi ke 4: "))
  keliling = hitung_keliling_jajar_genjang(a, b, c, d)
  print(f"Keliling jajar genjang adalah: {keliling}")
  
if __name__ == "__main__":
  keliling()