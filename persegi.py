#LUAS
def hitung_luas_persegi(s):
    return s * s
def luas():
        s = float(input("Masukkan panjang sisi persegi: "))
        luas = hitung_luas_persegi(s)
        print(f"Luas persegi dengan sisi {s} adalah {luas}")
if __name__ == "__main__":
    luas()
    
    
#KELILING
def hitung_keliling_persegi(s):
    return s*4
def keliling():
    s = float(input("Masukkan panjang sisi persegi: "))
    keliling = hitung_keliling_persegi(s)
    print(f"Keliling persegi dengan sisi {s} adalah {keliling}")
if __name__ == "__main__":
    keliling()