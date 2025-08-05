def hitung_luas_persegi(s):
    return s * s
def start():
        s = float(input("Masukkan panjang sisi persegi: "))
        luas = hitung_luas_persegi(s)
        print(f"Luas persegi dengan sisi {s} adalah {luas}")

if __name__ == "__main__":
    start()