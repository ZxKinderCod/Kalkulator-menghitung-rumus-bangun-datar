#LUAS
def hitung_luas_lingkaran(r):
    return 3.14 * r * r
  
def luas():
      r = float(input("Masukkan jari-jari lingkaran: "))
      luas = hitung_luas_lingkaran(r)
      print(f"Luas lingkaran dengan jari-jari {r} adalah {luas}")
  
if __name__ == "__main__":
  luas()



#KELILING
def hitung_keliling_lingkaran(r):
  return 2 * 3.14 * r

def keliling():
  r = float(input("Masukkan jari-jari lingkaran: "))
  keliling = hitung_keliling_lingkaran(r)
  print(f"Keliling lingkaran dengan jari-jari {r} adalah {keliling}")

if __name__ == "__main__":
  keliling()