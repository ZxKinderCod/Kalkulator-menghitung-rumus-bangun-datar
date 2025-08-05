#PERSEGI
def penjurusan_persegi():
  print ("1. Luas Persegi")
  print ("2. Keliling persegi")
  pilihan = input ("Pilihlah salah satu : ")
  
  if pilihan == "1":
    from persegi import start
    start()
  elif pilihan == "2":
    pass
def main():
  while True:
    penjurusan_persegi()
        
if __name__ == "__main__":
  main()
  
  #LINGKARAN
  
def penjurusan_lingkaran():
  print ("1. Luas lingkaran")
  print ("2. Keliling lingkaran")
  pilihan = input ("Pilihlah salah satu : ")
  
  if pilihan == "1":
    from lingkaran import start
    start()
  elif pilihan == "2":
    pass
def lingkaran():
  while True:
    penjurusan_lingkaran()
        
if __name__ == "__main__":
  lingkaran()
  
  
  