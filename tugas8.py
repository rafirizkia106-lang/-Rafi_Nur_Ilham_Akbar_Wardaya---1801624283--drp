# ==========================================
# TUGAS 8 - LOOPING
# Nama : Rafi Nur Ilham Akbar Wardaya
# ==========================================

print("=== LAYOUT CATUR ===")

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()


print("\n=== DAFTAR AKTIVITAS ===")

aktivitas_list = []

jumlah = int(input("Berapa aktivitas yang ingin diinput? "))

for i in range(jumlah):
    aktivitas = input(f"Masukkan aktivitas ke-{i+1}: ")
    waktu = input("Jam kegiatan: ")
    prioritas = input("Prioritas: ")

    data = {
        "aktivitas": aktivitas,
        "waktu": waktu,
        "prioritas": prioritas
    }

    aktivitas_list.append(data)

print("\n===== HASIL DATA AKTIVITAS =====")

for i, item in enumerate(aktivitas_list, start=1):
    print(f"\nAktivitas {i}")
    print("Nama :", item["aktivitas"])
    print("Waktu :", item["waktu"])
    print("Prioritas :", item["prioritas"])