def options():
    print("Pilih rumus yang ingin dihitung:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        from pemilihan import penjurusan_persegi
        penjurusan_persegi()
    elif pilihan == "2":
        from pemilihan import penjurusan_lingkaran
        penjurusan_lingkaran()
    elif pilihan == "3":
        from pemilihan import penjurusan_segitiga
        penjurusan_segitiga()

def main():
    while True:
        options()

if __name__ == "__main__":
    main()