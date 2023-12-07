for i in range(1, 100):
    # Mengecek apakah i merupakan kelipatan 10
    if i % 10 == 0:
        # Jika i adalah kelipatan 10, maka akan ada perulangan dalam sebanyak 3 kali
        for _ in range(3):
            # Mencetak "Your Name" sebanyak 3 kali
            print("Your Name")
    else:
        # Jika i bukan kelipatan 10, maka mencetak nilai i
        print(i)

