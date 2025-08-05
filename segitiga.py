#LUAS
def hitung_luas_segitiga(a, t):
    return 0.5 * a * t

def luas():
      a = float(input("Masukkan alas segitiga: "))
      t = float(input("Masukkan tinggi segitiga: "))
      luas = hitung_luas_segitiga(a, t)
      print(f"Luas segitiga dengan alas {a} dan tinggi {t} adalah {luas}")
      
if __name__ == "__main__":
  luas()
  
  
  
  
#KELILING
def hitung_keliling_segitiga(a, b, c):
  return a + b + c

def keliling():
  a = float(input("Masukkan sisi 1 segitiga: "))
  b = float(input("Masukkan sisi 2 segitiga: "))
  c = float(input("Masukkan sisi 3 segitiga: "))
  keliling = hitung_keliling_segitiga(a, b, c)
  print(f"Keliling segitiga dengan sisi {a}, {b}, dan {c} adalah {keliling}")
  
if __name__ == "__main__":
  keliling()