import json
import pwinput


def load_data():
    try:
        with open("storage.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "admin": {},
            "users": {},
            "drama_list": {},
            "favorite": {}
        }

def save_data(data):
    with open("storage.json", "w") as file:
        json.dump(data, file, indent=4)



def registrasi():
    data = load_data()

    print("\n=== REGISTRASI AKUN ===")

    while True:
        username = input("Masukkan username baru: ").strip()

        
        if username in data["users"] or username in data["admin"]:
            print("Username sudah terdaftar, coba lagi!")
            continue  

        password = pwinput.pwinput("Masukkan password: ")

        
        data["users"][username] = password
        data["favorite"][username] = []  # siapkan list favorit user

        save_data(data)

        print("Registrasi berhasil! Silakan login.")
        break




def login():
    data = load_data()

    print("\n=== LOGIN SISTEM ===")

    while True:
        username = input("Masukkan username: ").strip()
        password = pwinput.pwinput("Masukkan password: ")

        
        if username in data["admin"] and password == data["admin"][username]:
            print("Login berhasil sebagai ADMIN!")
            return username, True   # is_admin = True

    
        if username in data["users"] and password == data["users"][username]:
            print("Login berhasil sebagai USER!")
            return username, False  # is_admin = False

        print("Input data akun tidak valid! Coba lagi...\n")



def login_tamu():
    print("\n== MASUK SEBAGAI TAMU ==")
    return "TAMU", None   # Tidak punya role