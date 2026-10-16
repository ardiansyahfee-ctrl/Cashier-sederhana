print("=" * 10, "Cashier Coffee Shop", "=" * 10)

import datetime

tanggal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Tanggal dan waktu: {tanggal}\n")

MENU_KOPI = {
    1: ("Espresso",            15000),
    2: ("Americano",           18000),
    3: ("Cappuccino",          25000),
    4: ("Caffe Latte",         25000),
    5: ("Kopi Susu Gula Aren", 22000),
    6: ("Mocha",               28000),
    7: ("Caramel Macchiato",   30000),
    8: ("Vietnam Drip",        24000),
}

MENU_NON_KOPI = {
    1: ("Matcha Latte", 28000),
    2: ("Chocolate",    26000),
    3: ("Red Velvet",   27000),
    4: ("Taro Latte",   26000),
    5: ("Thai Tea",	    20000),
}

MENU_MINUMAN_SEGAR = {
    1: ("Lemon Tea",	 15000),
    2: ("Es Teh Manis",	 8000),
    3: ("Lychee Tea",	 20000),
    4: ("Air Mineral",	 5000),
}

MENU_MAKANAN_RINGAN = {
    1: ("Kentang Goreng",	     18000),
    2: ("Roti Bakar Coklat Keju",20000),
    3: ("Croissant",	         22000),
    4: ("Brownies",	             20000),
    5: ("Banana Cake",	         18000),
}

MENU_MAKANAN_BERAT = {
    1:("Nasi Goreng Spesial",	 30000),
    2:("Mie Goreng",	         25000),
    3:("Chicken Katsu Rice",	 32000),
}

SEMUA_MENU = {
    "1": ("KOPI", MENU_KOPI),
    "2": ("NON KOPI", MENU_NON_KOPI),
    "3": ("MINUMAN SEGAR", MENU_MINUMAN_SEGAR),
    "4": ("MAKANAN RINGAN", MENU_MAKANAN_RINGAN),
    "5": ("MAKANAN BERAT", MENU_MAKANAN_BERAT),
}



DISKON_PERSEN = 10
MINIMAL_DISKON = 100000
PAJAK_PERSEN = 3


# --------- KERANJANG BELANJA ----------
keranjang = [] # isi tiap barang: (nama, harga, jumlah)


# ----------- ALAT BANTU ----------
def rupiah(angka):
    """Ubah 15000 jadi Rp15.0000"""
    return "Rp" + f"{angka:,.0f}".replace(",", ".")


def tampil_kategori():
    print("\n=== PILIH KATEGORI ===")
    for nomor, (nama, isi) in SEMUA_MENU.items():
        print(f"{nomor},{nama}")
    print("0.SELESAI /BAYAR ")



def pilih_menu(nama_kategori, isi):
    """PILIH menu di dalam satu kategori, bisa berkali kali."""
    while True:
        print(f"\n === MENU {nama_kategori} ===")
        for no, (menu, harga) in isi.items():
            print(f"{no}. {menu:<25} {rupiah(harga):>10}")
        print("0. Kembali ke kategori")

        pilih = input ("Pilih menu nomor berapa? ")
        if pilih == "0":
            return #kembali ke halaman kategori

        if pilih.isdigit() and int(pilih) in isi:
            nama_menu, harga = isi [int(pilih)]
            jumlah = input(f"Jumlah {nama_menu}: ")
            if jumlah.isdigit() and int(jumlah) > 0:
                keranjang.append((nama_menu, harga, int(jumlah)))
                print(f"\u2714 {nama_menu} x {jumlah} masuk keranjang")
            else:
                print("Jumlah harus angka lebih dari 0! ")
        else:
            print("Menu tidak ada! ")


# -------------- LOOP UTAMA: PILIH KATEGORI TERUS -------------
while True:
    tampil_kategori()
    pilih = input("Mau kategori nomor berapa? ")

    if pilih == "0":
        if len(keranjang) == 0:
            print ("Keranjang masih kosong, pilih menu dulu ya!")
            continue
        break   # keluar darri loop, lanjut ke pembayaran

    if pilih in SEMUA_MENU:
        nama, isi = SEMUA_MENU[pilih]
        pilih_menu(nama, isi)
    else:
        print("Kategori tidak ada!")


# --------- HITUNG TOTAL ----------
subtotal = 0
for nama_menu, harga, jumlah in keranjang:
    subtotal += harga * jumlah

if subtotal >= MINIMAL_DISKON:
    diskon = subtotal * DISKON_PERSEN / 100
else:
    diskon = 0

setelah_diskon = subtotal - diskon
pajak = setelah_diskon * PAJAK_PERSEN / 100
total_bayar = setelah_diskon + pajak

print("\n" + "=" * 30)
print(f"TOTAL BAYAR: {rupiah(total_bayar)}")
print("=" * 30)

# ---------- UANG BAYAR ----------
while True:
    try:
       uang_bayar = int(input("Uang bayar : Rp "))
       if uang_bayar >= total_bayar:
           break
       print("Uang kurang, coba lagi!")
    except ValueError:
        print("Harus angka ya, coba lagi!")

kembalian = uang_bayar - total_bayar

# ----------- CETAK STRUK -------------
print("\n" + "=" * 40)
print("           CASHIER COFFE SHOP")
print("=" * 40)
print(f"Tanggal: {tanggal}")
print("-" * 40)
for nama_menu, harga, jumlah in keranjang:
    print(f"{nama_menu}")
    print(f" {jumlah} x {rupiah(harga):<10} {rupiah(harga * jumlah):>20}")
print("-" * 40)
print(f"{'Subtotal':<20}{rupiah(subtotal):>20}")
if diskon > 0:
    print(f"{'Diskon ' + str(DISKON_PERSEN) + '%':<20}{'-' + rupiah(diskon):>20}")
print(f"{'Pajak ' + str(PAJAK_PERSEN) + '%':20}{rupiah(pajak):>20}")
print("-"* 40)
print(f"{'TOTAL':<20}{rupiah(total_bayar):>20}")
print(f"{'Uang bayar':<20}{rupiah(uang_bayar):>20}")
print(f"{'Kembalian':<20}{rupiah(kembalian):>20}")
print("=" * 40)
print("   Terima kasih, datang lagi ya!")
print("         KULIAH? BSI AJA!!")
print("          BSI?  OI OI OI")
print("=" * 40)