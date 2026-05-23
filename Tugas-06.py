from datetime import datetime

print("=== Aplikasi Manajemen Aktivitas ===")
print("1. Sarapan")
print("2. Berangkat Kerja")

pilihan = input("Masukkan pilihan: ")

if pilihan == "1":

    print("Menu tersedia:")
    print("- telur")
    print("- ikan")
    print("- nugget")

    menu = input("Pilih menu: ")

    if menu == "telur":
        print("Masak telur terlebih dahulu")

    elif menu == "ikan":
        print("Masak ikan terlebih dahulu")

    elif menu == "nugget":
        print("Masak nugget terlebih dahulu")

    else:
        print("Menu tidak tersedia")

elif pilihan == "2":

    sekarang = datetime.now()

    jam = sekarang.hour
    menit = sekarang.minute

    if jam > 8 or (jam == 8 and menit > 0):
        print("Anda terlambat masuk kerja")

    else:
        print("Anda tepat waktu")

else:
    print("Pilihan tidak valid")