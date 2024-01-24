import random

#KATEGORI
def tampilkan_menu(cat):
    print("\n===== UNIQLO =====")
    print("Daftar Produk:")
    for kategori, kat in cat.items():
        print(f"{kategori}. {kat['nama']}")

#LAKI
def tampilkan_pria(pria):
    print("\n===== UNIQLO : PRIA =====")
    print("Daftar Produk:")

    for kategori, produk in pria.items():
        print(f"{kategori}. {produk['nama']} : Rp {produk['harga']}")

def beli_produk(pria, keranjang, prod, jumlah):
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0. Silakan masukkan jumlah yang valid.")
        return

    produk = pria[prod]
    total_harga = produk['harga'] * jumlah
    keranjang.append({'nama': produk['nama'], 'jumlah': jumlah, 'total_harga': total_harga})

#WANITA
def tampilkan_wanita(wanita):
    print("\n===== UNIQLO : WANITA =====")
    print("Daftar Produk:")

    for kategori, produk in wanita.items():
        print(f"{kategori}. {produk['nama']} : Rp {produk['harga']}")    

def beli_produk(wanita, keranjang, prod, jumlah):
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0. Silakan masukkan jumlah yang valid.")
        return

    produk = wanita[prod]
    total_harga = produk['harga'] * jumlah
    keranjang.append({'nama': produk['nama'], 'jumlah': jumlah, 'total_harga': total_harga})

#ANAK
def tampilkan_anak(anak):
    print("\n===== UNIQLO : ANAK =====")
    print("Daftar Produk:")

    for kategori, produk in anak.items():
        print(f"{kategori}. {produk['nama']} : Rp {produk['harga']}")

def beli_produk(anak, keranjang, prod, jumlah):
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0. Silakan masukkan jumlah yang valid.")
        return

    produk = anak[prod]
    total_harga = produk['harga'] * jumlah
    keranjang.append({'nama': produk['nama'], 'jumlah': jumlah, 'total_harga': total_harga})

#BAYI
def tampilkan_bayi(bayi):
    print("\n===== UNIQLO : BAYI =====")
    print("Daftar Produk:")

    for kategori, produk in bayi.items():
        print(f"{kategori}. {produk['nama']} : Rp {produk['harga']}")

def beli_produk(bayi, keranjang, prod, jumlah):
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0. Silakan masukkan jumlah yang valid.")
        return

    produk = bayi[prod]
    total_harga = produk['harga'] * jumlah
    keranjang.append({'nama': produk['nama'], 'jumlah': jumlah, 'total_harga': total_harga})

#KERANJANG
def tampilkan_keranjang(keranjang):
    print("\n===== Keranjang Belanja =====")
    total_belanja = 0
    for item in keranjang:
        print(f"{item['nama']} x{item['jumlah']}: Rp {item['total_harga']}")
        total_belanja += item['total_harga']
    print("=============================")
    print(f"Total Belanja: Rp {total_belanja}")

def pilih_metode_pembayaran():
    while True:
        print("\nMetode Pembayaran:")
        print("1. Bayar di Counter")
        print("2. Transfer Bank")

        pilihan = input("Pilih metode pembayaran (1/2): ")

        if pilihan in ['1', '2']:
            break
        else:
            print("Pilihan tidak valid. Silakan pilih metode pembayaran yang tersedia.")

    metode_pembayaran = ""
    if pilihan == '1' :
        metode_pembayaran = "Bayar di Counter"
        kode_pembayaran = random.randint(100, 999)
        print(f"\n===== Kode Pembayaran {metode_pembayaran} =====")
        print(f"Kode Pembayaran Anda: 230{kode_pembayaran}")
        print("============================================")

    elif pilihan == '2':
        while True:
            print("\nMetode Pembayaran:")
            print("1. BNI")
            print("2. BCA")
            print("3. Mandiri")

            ATM = input("Pilih metode pembayaran (1/2/3): ")

            if ATM in ['1','2','3']:
                break
            else:
                print("Pilihan tidak valid. Silakan pilih Bank yang tersedia.")

        if ATM == '1':
            metode_pembayaran = "BNI"
            kode_pembayaran = random.randint(100000000, 999999999)
            print(f"\n===== Kode Pembayaran {metode_pembayaran} =====")
            print(f"Kode Pembayaran Anda: 1{kode_pembayaran}")
            print("=========================================")
        elif ATM == '2':
            metode_pembayaran = "BCA"
            kode_pembayaran = random.randint(1000000, 9999999)
            print(f"\n======= Kode Pembayaran {metode_pembayaran} =======")
            print(f"Kode Pembayaran Anda: 262{kode_pembayaran}")
            print("===================================")
        elif ATM == '3':
            metode_pembayaran = "Mandiri"
            kode_pembayaran = random.randint(100000000, 999999999)
            print(f"\n======= Kode Pembayaran {metode_pembayaran} =======")
            print(f"Kode Pembayaran Anda: 157{kode_pembayaran}")
            print("=======================================")

    return metode_pembayaran

def belanja():
    cat = {
        '1': {'nama': 'Pria'},
        '2': {'nama': 'Wanita'},
        '3': {'nama': 'Anak'},
        '4': {'nama': 'Bayi'}
    }

    pria = {
        '1': {'nama': 'Kardigan Sweat Lengan Panjang (Indigo)', 'harga': 599000},
        '2': {'nama': 'Jaket Rajut Luaran Kemeja', 'harga': 499000},
        '3': {'nama': 'AIRism T-Shirt Kerah Bulat Lengan Pendek', 'harga': 149000},
        '4': {'nama': 'AIRism T-Shirt Kerah V Lengan Pendek', 'harga': 149000},
        '5': {'nama': 'Celana Chino Slim Fit', 'harga': 599000},
    }

    wanita = {
        '1': {'nama': 'T-Shirt Waffle Kerah Bulat Lengan Panjang', 'harga': 199000},
        '2': {'nama': 'Kemeja Panjang Flannel Kotak Lengan Panjang', 'harga': 399000},
        '3': {'nama': 'Jaket Parka Katun Blend', 'harga': 699000},
        '4': {'nama': 'Celana Kargo Sweat', 'harga': 499000},
        '5': {'nama': 'Rok Gather Panjang', 'harga': 599000},
    }

    anak = {
        '1': {'nama': 'KIDS Kaos Polo Dry Pique Lengan Pendek (Bordir)', 'harga': 199000},
        '2': {'nama': 'KIDS UT Disney Lengan Pendek', 'harga': 149000},
        '3': {'nama': 'KIDS Kemeja Flannel Kotak Lengan Panjang', 'harga': 199000},
        '4': {'nama': 'KIDS Jeans Fit Lebar Ritsleting Denim', 'harga': 399000},
        '5': {'nama': 'KIDS Celana Pendek Sweat Dry Ultra Stretch', 'harga': 199000},
    }

    bayi = {
        '1': {'nama': 'Baju Terusan Rib 1*1 Lengan Panjang', 'harga': 199000},
        '2': {'nama': 'UT Studio Ghibli Lengan Pendek', 'harga': 149000},
        '3': {'nama': 'Piyama Disney KIDEA Lengan Panjang', 'harga': 199000},
        '4': {'nama': 'Celana Legging (Kotak)', 'harga': 129000},
        '5': {'nama': 'Kaos Kaki 2 Pack (Reguler)', 'harga': 79000},
    }

    keranjang = []

    while True:
        tampilkan_menu(cat)

        kategori = input("\nPilih kategori produk (ketik '0' untuk selesai): ").lower()
        if kategori == '0':
            break

        if kategori == '1':
            tampilkan_pria(pria)

            prod = input("Pilih Produk yang diinginkan: ")
            if prod in pria:
                jumlah = int(input("Masukan Jumlah yang ingin dibeli: "))
                beli_produk(pria, keranjang, prod, jumlah)

            else:
                print("Produk tidak valid. Silakan pilih Produk yang tersedia.")

        elif kategori == '2':
            tampilkan_wanita(wanita)

            prod = input("Pilih Produk yang diinginkan: ")
            if prod in wanita:
                jumlah = int(input("Masukan Jumlah yang ingin dibeli: "))
                beli_produk(wanita, keranjang, prod, jumlah)

            else:
                print("Produk tidak valid. Silakan pilih Produk yang tersedia.")

        elif kategori == '3':
            tampilkan_anak(anak)

            prod = input("Pilih Produk yang diinginkan: ")
            if prod in anak:
                jumlah = int(input("Masukan Jumlah yang ingin dibeli: "))
                beli_produk(anak, keranjang, prod, jumlah)

            else:
                print("Produk tidak valid. Silakan pilih Produk yang tersedia.")

        elif kategori == '4':
            tampilkan_bayi(bayi)

            prod = input("Pilih Produk yang diinginkan: ")
            if prod in bayi:
                jumlah = int(input("Masukan Jumlah yang ingin dibeli: "))
                beli_produk(bayi, keranjang, prod, jumlah)

            else:
                print("Produk tidak valid. Silakan pilih Produk yang tersedia.")

        else:
            print("Kategori tidak valid. Silakan pilih kategori yang tersedia.")

    if not keranjang:
        print("Keranjang belanja kosong.")
        return
    
    tampilkan_keranjang(keranjang)
    metode_pembayaran = pilih_metode_pembayaran()
    print("Silahkan Melakukan Pembayaran \n")
    

belanja()
