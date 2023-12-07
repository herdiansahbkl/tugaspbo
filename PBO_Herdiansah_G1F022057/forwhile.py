# Menggunakan for loop
print("Menggunakan for loop:")
# Perulangan for dengan range(1, 11), artinya nilai i akan berjalan dari 1 hingga 10 (inklusif).
for i in range(1, 11):
    # Pemeriksaan apakah nilai i adalah angka genap.
    if i % 2 == 0:
        # Jika genap, mencetak bahwa i adalah angka genap.
        print(f"{i} adalah angka genap.")
    else:
        # Jika ganjil, mencetak bahwa i adalah angka ganjil.
        print(f"{i} adalah angka ganjil.")
# Menggunakan while loop
print("\nMenggunakan while loop:")
# Inisialisasi variabel counter dengan nilai awal 1.
counter = 1
# Perulangan while akan berjalan selama nilai counter kurang dari atau sama dengan 10.
while counter <= 10:
    # Pemeriksaan apakah nilai counter adalah angka genap.
    if counter % 2 == 0:
        # Jika genap, mencetak bahwa counter adalah angka genap.
        print(f"{counter} adalah angka genap.")
    else:
        # Jika ganjil, mencetak bahwa counter adalah angka ganjil.
        print(f"{counter} adalah angka ganjil.")
    # Meningkatkan nilai counter setiap kali iterasi untuk menghindari perulangan tanpa henti.
    counter += 1

