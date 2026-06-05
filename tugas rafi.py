def display_menu():
    print("==========================")
    print("Selamat Datang di Studio!")
    print("1. Durasi belajar Anda")
    print("2. Hari paling produktif Anda")
    print("3. Evaluasi kebiasaan belajar Anda")
    print("4. Selesai")
    print("==========================")

def select_menu(menu):
    if menu == "1":
        print("Anda memilih menu durasi belajar")

    elif menu == "2":
        print("Anda memilih menu hari paling produktif")

    elif menu == "3":
        print("Anda memilih menu evaluasi kebiasaan belajar")

    elif menu == "4":
        print("Program selesai")

    else:
        print("Pilihan tidak tersedia")


display_menu()

menu = input("Masukkan pilihan menu (1-4): ")

select_menu(menu)