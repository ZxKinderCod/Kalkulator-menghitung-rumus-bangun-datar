def hitung_luas_lingkaran(r):
    return 3.14 * r * r
  
def start():
      r = float(input("Masukkan jari-jari lingkaran: "))
      luas = hitung_luas_lingkaran(r)
      print(f"Luas lingkaran dengan jari-jari {r} adalah {luas}")
      
if __name__ == "__main__":
  start()
