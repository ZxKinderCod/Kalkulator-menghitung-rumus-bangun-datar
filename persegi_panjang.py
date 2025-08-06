def hitung_keliling_persegi_panjang(P, L):
  return 2*(P+L)
def keliling ():
  P = float(input("Masukkan Panjang sisi persegi: "))
  L = float(input("Masukkan Lebar sisi persegi: "))
  keliling = hitung_keliling_persegi_panjang(P, L)
  print(f"Keliling persegi adalah {keliling}")

if __name__ == "__main__":
  keliling()

def hitung_luas_persegi_panjang(P, L):
  return P*L
def luas ():
  P = float(input("Masukkan Panjang sisi persegi: "))
  L = float(input("Masukkan Lebar sisi persegi: "))
  luas = hitung_luas_persegi_panjang(P, L)
  print(f"Luas persegi adalah {luas}")

if __name__ == "__main__":
  luas()