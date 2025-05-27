# inisialisasi menu 
menu_lauk = [
              {"nama": "Ayam Goreng", "harga": 10, "kenyang": 4},
              {"nama": "Ayam Rica-rica", "harga": 10, "kenyang": 4},
              {"nama": "Cumi Lada Hitam", "harga": 10, "kenyang": 2},
              {"nama": "Sapi Lada Hitam", "harga": 15, "kenyang": 3},
              {"nama": "Telur Bumbu Bali", "harga": 7, "kenyang": 3},
              {"nama": "Ikan Palumara", "harga": 15, "kenyang": 3},
              {"nama": "Ikan Tongkol Bumbu Merah", "harga": 10, "kenyang": 4},
              {"nama": "Sambel Goreng Ati Ampela", "harga": 10, "kenyang": 2},
              {"nama": "Ikan Suir Tuna", "harga": 10, "kenyang": 3},
              {"nama": "Udang Goreng Asam Manis", "harga": 10, "kenyang": 3},
              {"nama": "Kulit Ayam Crispy", "harga": 10, "kenyang": 2},
              {"nama": "Gongso Paru", "harga": 15, "kenyang": 2},
              {"nama": "Ceker tanpa Tulang", "harga": 10, "kenyang": 2},
              {"nama": "Perkedel Jagung", "harga": 2, "kenyang": 3},
              {"nama": "Perkedel Kentang", "harga": 3, "kenyang": 2},
              {"nama": "Tahun Bulat", "harga": 2, "kenyang": 1},
              {"nama": "Tempe Mendoan", "harga": 2, "kenyang": 2}
            ]

# item = lauk
# weight = harga lauk
# value = nilai kenyang dari lauk
# kapasitas = budget user


# fungsi pilih menu kalo ngga pake nasi
def pilih_lauk (budget, total_kenyang_maksimal, list_lauk):

  jumlah_lauk = len(list_lauk)

  # inisiasi tabel dynamic programming nilai awal 0
  dp = [[0 for kapasitas in range (budget + 1)]
        for indeks_lauk in range (jumlah_lauk + 1)]
  
  for indeks_lauk in range (1, jumlah_lauk + 1):
    for kapasitas in range (1, budget + 1) :

      harga_lauk = list_lauk[indeks_lauk - 1]["harga"]
      nilai_kenyang = list_lauk[indeks_lauk - 1]["kenyang"]

      # menentukan ambil lauk dan tidak ambil lauk
      if harga_lauk <= kapasitas:
        ambil_lauk = nilai_kenyang + dp[indeks_lauk - 1][kapasitas - harga_lauk]
        tidak_ambil_lauk = dp[indeks_lauk - 1][kapasitas]
        
        dp[indeks_lauk][kapasitas] = max(ambil_lauk, tidak_ambil_lauk)

      else:
        dp[indeks_lauk][kapasitas] = dp[indeks_lauk - 1][kapasitas]

  total_kenyang_maksimal = dp[jumlah_lauk][budget]

  # cari lauk terpilih (backtracking)
  sisa_kapasitas = budget
  list_lauk_terpilih = []

  for indeks_lauk in range(jumlah_lauk, 0, -1):
    if dp[indeks_lauk][sisa_kapasitas] != dp[indeks_lauk - 1][sisa_kapasitas]:
      lauk = list_lauk[indeks_lauk - 1]
      list_lauk_terpilih.append(lauk)
      sisa_kapasitas -= lauk["harga"]

  total_harga = sum(lauk["harga"] for lauk in list_lauk_terpilih)

  hasil_terpilih = {
    "lauk": list(reversed(list_lauk_terpilih)),
    "total_harga": total_harga,
    "total_kenyang": total_kenyang_maksimal,
  }

  print("\n\033[33m------------ Hasil Pilihan Lauk ------------\033[0m")
  for lauk in hasil_terpilih["lauk"]:
    print(f"\033[36m{lauk['nama']} (Rp{(lauk['harga'])*1000}, Kenyang {lauk['kenyang']})\033[0m")
  
  print()
  print(f"Total harga\t: Rp{(hasil_terpilih['total_harga'])*1000}")
  print(f"Total kenyang\t: {hasil_terpilih['total_kenyang']}")
  print(f"Sisa uang\t: Rp{(budget*1000) - (hasil_terpilih['total_harga'])*1000}")

  print(f"\n\033[35mKompleksitas: O(n × budget) = O({len(menu_lauk)} × {budget_user}) = O({len(menu_lauk) * budget_user})\033[0m\n")

  print("\033[32mWorst Case\t= O(n x W)")
  print("Best Case\t= O(n)")
  print("Average Case\t= O(n)\033[0m\n")
  
# fungsi pilih menu kalo pake nasi
def pilih_lauk_nasi (budget, total_kenyang_maksimal, list_lauk):
  if budget <= 6:
    print("\n\033[31mbudget tidak cukup untuk memilih lauk lain...\033[0m")

  else:
    nilai_kenyang_nasi = 5
    harga_nasi = 5
    budget_saat_ini = budget - harga_nasi

    jumlah_lauk = len(list_lauk)

    # inisiasi tabel dynamic programming nilai awal 0
    dp = [[0 for kapasitas in range (budget_saat_ini + 1)]
          for indeks_lauk in range (jumlah_lauk + 1)]
    
    for indeks_lauk in range (1, jumlah_lauk + 1):
      for kapasitas in range (1, budget_saat_ini + 1) :

        harga_lauk = list_lauk[indeks_lauk - 1]["harga"]
        nilai_kenyang = list_lauk[indeks_lauk - 1]["kenyang"]

        # menentukan ambil lauk dan tidak ambil lauk
        if harga_lauk <= kapasitas:
          ambil_lauk = nilai_kenyang + dp[indeks_lauk - 1][kapasitas - harga_lauk]
          tidak_ambil_lauk = dp[indeks_lauk - 1][kapasitas]
          
          dp[indeks_lauk][kapasitas] = max(ambil_lauk, tidak_ambil_lauk)

        else:
          dp[indeks_lauk][kapasitas] = dp[indeks_lauk - 1][kapasitas]

    total_kenyang_maksimal = dp[jumlah_lauk][budget_saat_ini]

    # cari lauk terpilih (backtracking)
    sisa_kapasitas = budget_saat_ini
    list_lauk_terpilih = []

    nasi = {"nama": "Nasi + Sayur", "harga": 5, "kenyang": 5}
    list_lauk_terpilih.append(nasi)

    for indeks_lauk in range(jumlah_lauk, 0, -1):
      if dp[indeks_lauk][sisa_kapasitas] != dp[indeks_lauk - 1][sisa_kapasitas]:
        lauk = list_lauk[indeks_lauk - 1]
        list_lauk_terpilih.append(lauk)
        sisa_kapasitas -= lauk["harga"]

    total_harga = sum(lauk["harga"] for lauk in list_lauk_terpilih)

    hasil_terpilih = {
      "lauk": list(reversed(list_lauk_terpilih)),
      "total_harga": total_harga,
      "total_kenyang": total_kenyang_maksimal + nilai_kenyang_nasi,
    }

    print("\n\033[33m------------ Hasil Pilihan Lauk ------------\033[0m")
    for lauk in hasil_terpilih["lauk"]:
      print(f"\033[36m{lauk['nama']} (Rp{(lauk['harga'])*1000}, Kenyang {lauk['kenyang']})\033[0m")
    
    print()
    print(f"Total harga\t: Rp{(hasil_terpilih['total_harga'])*1000}")
    print(f"Total kenyang\t: {hasil_terpilih['total_kenyang']}")
    print(f"Sisa uang\t: Rp{(budget*1000) - (hasil_terpilih['total_harga'])*1000}")

  print(f"\n\033[35mKompleksitas: O(n × budget) = O({len(menu_lauk)} × {budget_user}) = O({len(menu_lauk) * budget_user})\033[0m\n")

  print("\033[32mWorst Case\t= O(n x W)")
  print("Best Case\t= O(n)")
  print("Average Case\t= O(n)\033[0m\n")


# main
while True:
  try:
    print("\033[33m--------- Menu Utama ---------\033[0m")
    print("\033[33m1. Pilihin Lauk\033[0m")
    print("\033[33m2. Keluar\033[0m")

    pilihan = int(input("\npilih menu: \n-> "))
    
    try:
      if pilihan == 1:

        budget_user = (int(input("\nmasukkan budget-mu: \n-> ")))//1000
        maks_kenyang = -1

        if budget_user < 2:
          print("\033[31mMaaf, tidak ada lauk yang sesuai dengan budgetmu saat ini...\033[0m")

        else :
          try:
            pilih_nasi = str(input("\napakah kamu mau pake nasi? (jawab iya/tidak)\n-> "))

            if pilih_nasi == "iya":
              pilih_lauk_nasi(budget_user, maks_kenyang, menu_lauk)
              
            elif pilih_nasi == "tidak":
              pilih_lauk(budget_user, maks_kenyang, menu_lauk)

            else:
              print("\n \033[31minput tidak valid. masukkan pilihan yang benar. silahkan coba lagi.\033[0m")

          except ValueError:
            print("\n \033[31minput harus berupa teks. silahkan coba lagi\033[0m")

      elif pilihan ==2:
        print("keluar dari program.")
        break

      else:
        print("\n \033[31minput tidak valid. masukkan pilihan yang benar. silahkan coba lagi.\033[0m")

    except ValueError:
      print("\n \033[31minput harus berupa angka. silahkan coba lagi\033[0m")

  except ValueError:
      print("\n \033[31minput harus berupa angka. silahkan coba lagi\033[0m")