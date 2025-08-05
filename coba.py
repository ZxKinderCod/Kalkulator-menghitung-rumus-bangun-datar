def hitung_luas_persegi(s):
    return s * s

def hitung_luas_lingkaran(r):
    return 3.14 * r * r

def hitung_luas_segitiga(a, t):
    return 0.5 * a * t

print("Pilih rumus yang ingin dihitung:")
print("1. Luas Persegi")
print("2. Luas Lingkaran")
print("3. Luas Segitiga")

pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    s = float(input("Masukkan panjang sisi persegi: "))
    luas = hitung_luas_persegi(s)
    print(f"Luas persegi dengan sisi {s} adalah {luas}")
elif pilihan == "2":
    r = float(input("Masukkan jari-jari lingkaran: "))
    luas = hitung_luas_lingkaran(r)
    print(f"Luas lingkaran dengan jari-jari {r} adalah {luas}")
elif pilihan == "3":
    a = float(input("Masukkan alas segitiga: "))
    t = float(input("Masukkan tinggi segitiga: "))
    luas = hitung_luas_segitiga(a, t)
    print(f"Luas segitiga dengan alas {a} dan tinggi {t} adalah {luas}")
else:
    print("Pilihan tidak valid.")