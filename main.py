def options():
    print("Pilih rumus yang ingin dihitung:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    print ("4. Persegi Panjang")
    print ("5. Jajar Genjang")
    print ("6. Belah Ketupat")
    print ("7. Layang - layang")
    print ("8. Trapesium")
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
    elif pilihan == "4":
        from pemilihan import penjurusan_persegi_panjang
        penjurusan_persegi_panjang()
    elif pilihan == "5":
        from pemilihan import penjurusan_jajar_genjang
        penjurusan_jajar_genjang()
    elif pilihan == "6":
        from pemilihan import penjurusan_belah_ketupat
        penjurusan_belah_ketupat()
    elif pilihan == "7":
        from pemilihan import penjurusan_layang_layang
        penjurusan_layang_layang()
    elif pilihan == "8":
        from pemilihan import penjurusan_trapesium
        penjurusan_trapesium()

def main():
    while True:
        options()

if __name__ == "__main__":
    main()