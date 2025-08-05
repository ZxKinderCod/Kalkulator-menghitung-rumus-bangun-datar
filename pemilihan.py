#PERSEGI
def penjurusan_persegi():
  print ("1. Luas Persegi")
  print ("2. Keliling persegi")
  pilihan = input ("Pilihlah salah satu : ")
  
  if pilihan == "1":
    from persegi import luas
    luas()
  elif pilihan == "2":
    from persegi import keliling
    keliling()
    
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
    from lingkaran import luas
    luas()
  elif pilihan == "2":
    from lingkaran import keliling
    keliling()
    
def lingkaran():
  while True:
    penjurusan_lingkaran()
        
if __name__ == "__main__":
  lingkaran()
  


#SEGITIGA
def penjurusan_segitiga():
  print ("1. Luas segitiga")
  print ("2. Keliling segitiga")
  pilihan = input ("Pilihlah salah satu : ")
  
  if pilihan == "1":
    from segitiga import luas
    luas()
  elif pilihan == "2":
    from segitiga import keliling
    keliling()
    
def segitiga():
  while True:
    penjurusan_segitiga()
        
if __name__ == "__main__":
  segitiga()
  