import pwinput
from storage import load_users, save_users, load_admin

def valid_password(password):
    # Minimal mengandung huruf dan angka
    ada_huruf = any(char.isalpha() for char in password)
    ada_angka = any(char.isdigit() for char in password)
    return ada_huruf and ada_angka


def registrasi():
    storage_users = load_users()
    admin = load_admin()
    print("\n=== REGISTRASI AKUN ===")
    
    while True:
        username = input("Masukkan username baru: ").strip()

        if username == "":
            print("Username tidak boleh kosong!")
            continue

        if username in storage_users or username in admin:
            print("Username sudah terdaftar, coba lagi!")
            continue

        password = pwinput.pwinput("Masukkan password: ").strip()

        if password == "":
            print("Password tidak boleh kosong!")
            continue

        # Validasi password huruf + angka
        if not valid_password(password):
            print("Password harus mengandung huruf dan angka!")
            continue

        # Simpan user baru
        storage_users[username] = {"password": password, "watchlist": []}
        save_users(storage_users)
        print("Registrasi berhasil! Silakan login.")
        break



def login():
    storage_users = load_users()
    admin = load_admin()
    print("\n=== LOGIN SISTEM ===")

    percobaan = 0  # Counter percobaan login

    while percobaan < 3:
        username = input("Masukkan username: ").strip()
        password = pwinput.pwinput("Masukkan password: ").strip()

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!\n")
            percobaan += 1
            continue

        # Login admin
        if username in admin and password == admin[username]:
            print("Login berhasil sebagai ADMIN!")
            return username, True

        # Login user biasa
        if username in storage_users and password == storage_users[username]["password"]:
            print("Login berhasil sebagai USER!")
            return username, False

        # Jika gagal
        percobaan += 1
        sisa = 3 - percobaan
        print(f"Akun tidak valid! Sisa percobaan: {sisa}\n")

    print("Terlalu banyak percobaan gagal! Silakan coba lagi nanti.")
    return None, None
