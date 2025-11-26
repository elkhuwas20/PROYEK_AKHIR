from colorama import Fore, Style, init
from autentikasi import registrasi, login
from admin_menu import (
    read_drama, create_drama, update_drama, delete_drama,
    read_user_watchlists, search_drama_menu
)
from user_menu import (
    create_watchlist, read_watchlist, remove_watchlist, search_drama_user
)
from storage import load_users
import os 

init(autoreset=True)
ungu = Fore.RED

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def clear():
    input("\nTekan ENTER untuk kembali ke menu..."); cls()

def clear_2():
    input("\nTekan ENTER untuk masuk ke menu..."); cls()


def menu_admin(username):
    while True:
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.RED}{'█' * 70}")
        print(f"{Fore.YELLOW}  👑 SELAMAT DATANG, ADMIN {username.upper()}! 👑")
        print(f"{Fore.RED}{'█' * 70}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print()
        print(f"{Fore.GREEN}  1. {Fore.CYAN}📺 Lihat Semua Drama")
        print(f"{Fore.GREEN}  2. {Fore.CYAN}➕ Tambah Drama Baru")
        print(f"{Fore.GREEN}  3. {Fore.CYAN}✏️  Update Data Drama")
        print(f"{Fore.GREEN}  4. {Fore.CYAN}🗑️  Hapus Drama")
        print(f"{Fore.GREEN}  5. {Fore.CYAN}👤 Lihat Watchlist Pengguna")
        print(f"{Fore.GREEN}  6. {Fore.CYAN}🔍 Cari Drama")
        print(f"{Fore.RED}  7. {Fore.CYAN}🚪 Logout")
        print()

        opsi = input(f"{Fore.YELLOW}Pilih menu (1-7): {Style.RESET_ALL}").strip()
        if opsi == '1':
            read_drama()
            clear()
        elif opsi == '2':
            create_drama()
            clear()
        elif opsi == '3':
            update_drama()
            clear()
        elif opsi == '4':
            delete_drama()
            clear()
        elif opsi == '5':
            read_user_watchlists()
            clear()
        elif opsi == '6':
            search_drama_menu()
            clear()
        elif opsi == '7':
            print(f"{Fore.YELLOW}Terima kasih, Admin!")
            clear()
            return
        else:
            print(f"{Fore.RED}Pilihan tidak valid!")


def menu_user(username):
    while True:
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.RED}{'█' * 70}")
        print(f"{Fore.YELLOW}  👤 SELAMAT DATANG, {username.upper()}! 👤")
        print(f"{Fore.RED}{'█' * 70}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print()
        print(f"{Fore.GREEN}  1. {Fore.CYAN}📺 Lihat Semua Drama Korea")
        print(f"{Fore.GREEN}  2. {Fore.CYAN}➕ Tambah ke Watchlist")
        print(f"{Fore.GREEN}  3. {Fore.CYAN}📋 Lihat Watchlist Saya")
        print(f"{Fore.GREEN}  4. {Fore.CYAN}🗑️  Hapus dari Watchlist")
        print(f"{Fore.GREEN}  5. {Fore.CYAN}🔍 Cari Drama")
        print(f"{Fore.RED}  6. {Fore.CYAN}🚪 Logout")
        print()

        opsi = input(f"{Fore.YELLOW}Pilih menu (1-6): {Style.RESET_ALL}").strip()

        if opsi == '1':
            read_drama()
            clear()
        elif opsi == '2':
            create_watchlist(username)
            clear()
        elif opsi == '3':
            read_watchlist(username)
            clear()
        elif opsi == '4':
            remove_watchlist(username)
            clear()
        elif opsi == '5':
            search_drama_user()
            clear()
        elif opsi == '6':
            print(f"{Fore.YELLOW}👋 Sampai jumpa!")
            clear()
            return
        else:
            print(f"{Fore.RED}Pilihan tidak valid!")


def menu_awal():
    print(f"{Fore.RED}")
    print("\n" + "█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + f"{Fore.YELLOW}  🎬 WELCOME TO K-BLACKLIST: PLATFORM STREAMING DRAMA KOREA! 🎬".center(68) + f"{Fore.RED}█")
    print("█" + " " * 68 + "█")
    print("█" * 70 + f"{Style.RESET_ALL}")
    print()
    print(f"{Fore.GREEN}  1. {Fore.CYAN}📝 Registrasi")
    print(f"{Fore.GREEN}  2. {Fore.CYAN}🔐 Login")
    print(f"{Fore.GREEN}  3. {Fore.CYAN}👁️  Lihat sebagai Tamu")
    print(f"{Fore.RED}  4. {Fore.CYAN}🚪 Keluar")
    print()
    opsi = input(f"{Fore.YELLOW}Silahkan pilih opsi (1-4): {Style.RESET_ALL}").strip()
    return opsi


def main():
    while True:
        opsi = menu_awal()
        if opsi == "1":
            registrasi()
            clear()
            continue
        elif opsi == "2":
            username_isadmin = login()
            if username_isadmin is None:
                continue
            username, is_admin = username_isadmin
            if is_admin:
                clear_2()
                menu_admin(username)
            else:
                clear_2()
                menu_user(username)
        elif opsi == "3":
            print(f"{Fore.CYAN}👁️  Anda login sebagai tamu!{Style.RESET_ALL}")
            read_drama()
            clear()
            continue
        elif opsi == "4":
            print(f"{Fore.RED}\n✨ Terima kasih telah menggunakan K-Blacklist! ✨\n{Style.RESET_ALL}")
            exit()
        else:
            print(f"{Fore.RED}Pilihan tidak valid.")

if __name__ == "__main__":
    main()
