from colorama import Fore, Style
from autentikasi import registrasi, login, login_tamu

ungu = Fore.MAGENTA

def menu_awal():
    print(f"{ungu}"
        "\n======================================================================\n"
        "|      WELCOME TO K-BLACKLIST: PLATFORM STREAMING DRAMA KOREA!      |\n"
        "======================================================================\n"
        f"{Style.RESET_ALL}"
    )
    print("1. Registasi")
    print("2. Login")
    print("3. Lihat sebagai tamu")
    print("4. Keluar")
    return None

menu_awal()
opsi=input("Silahkan pilih menu 1-4: ")
if opsi == "1":
    registrasi()
    login()
elif opsi == "2":
    login()
elif opsi == "3":
    login_tamu()


# if autentikasi.is_admin:
#     while True:
#         menu = menu_admin()
#         if menu == "Menampilkan Daftar":
#             tampilkan_drama(drama_korea); clear()
#         elif menu == "Membuat Daftar":
#             tampilkan_drama(drama_korea)
#             membuat_daftar(int(input("\nPilih genre (1-5): "))); clear()
#         elif menu == "Mengganti Daftar":
#             tampilkan_drama(drama_korea)
#             mengganti_daftar(int(input("\nPilih genre (1-5): "))); clear()
#         elif menu == "Menghapus Daftar":
#             tampilkan_drama(drama_korea)
#             menghapus_daftar(int(input("\nPilih genre (1-5): "))); clear()
#         elif menu == "Keluar":
#             sys.exit()

# else:
#     while True:
#         menu = menu_member()
#         if menu == "Menampilkan Daftar":
#             tampilkan_drama(drama_korea); clear()
#         elif menu == "Mengganti Daftar":
#             tampilkan_drama(drama_korea)
#             mengganti_daftar(int(input("\nPilih genre (1-5): "))); clear()
#         elif menu == "Menghapus Daftar":
#             tampilkan_drama(drama_korea)
#             menghapus_daftar(int(input("\nPilih genre (1-5): "))); clear()
#         elif menu == "Keluar":
#             sys.exit()

