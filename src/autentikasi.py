try:
    import pwinput
    _has_pwinput = True
except Exception:
    import getpass
    _has_pwinput = False

from colorama import Fore, Style
from storage import load_users, save_users, load_admin


def _get_password(prompt: str) -> str:
    if _has_pwinput:
        return pwinput.pwinput(prompt)
    return getpass.getpass(prompt)

def registrasi():
    storage_users = load_users()
    admin = load_admin()
    print(f"\n{Fore.MAGENTA}{'█' * 50}")
    print(f"{Fore.YELLOW}📝 REGISTRASI AKUN 📝")
    print(f"{Fore.MAGENTA}{'█' * 50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}(Ketik 'cancel' kapan saja untuk membatalkan)\n{Style.RESET_ALL}")
    
    while True:
        username = input(f"{Fore.CYAN}Masukkan username baru: {Style.RESET_ALL}").strip()
        if username.lower() == 'cancel':
            print(f"{Fore.YELLOW}⏹️  Pembatalan registrasi.")
            return
        if not username:
            print(f"{Fore.RED}❌ Username tidak boleh kosong!")
            continue
        if username in storage_users or username in admin:
            print(f"{Fore.RED}❌ Username sudah terdaftar, coba lagi!")
            continue
        break
    
    while True:
        password = _get_password(f"{Fore.CYAN}Masukkan password: {Style.RESET_ALL}")
        if password.lower() == 'cancel':
            print(f"{Fore.YELLOW}⏹️  Pembatalan registrasi.")
            return
        if not password:
            print(f"{Fore.RED}❌ Password tidak boleh kosong!")
            continue
        break
    
    storage_users[username] = {"password": password, "watchlist": []}
    save_users(storage_users)
    print(f"{Fore.GREEN}✅ Registrasi berhasil! Silakan login.")

def login():
    storage_users = load_users()
    admin = load_admin()
    print(f"\n{Fore.MAGENTA}{'█' * 50}")
    print(f"{Fore.YELLOW}🔐 LOGIN SISTEM 🔐")
    print(f"{Fore.MAGENTA}{'█' * 50}{Style.RESET_ALL}")
    while True:
        username = input(f"{Fore.CYAN}Masukkan username: {Style.RESET_ALL}").strip()
        password = _get_password(f"{Fore.CYAN}Masukkan password: {Style.RESET_ALL}")
        if username in admin and password == admin[username]:
            print(f"{Fore.GREEN}✅ Login berhasil sebagai ADMIN!")
            return username, True
        if username in storage_users and password == storage_users[username]["password"]:
            print(f"{Fore.GREEN}✅ Login berhasil sebagai USER!")
            return username, False
        print(f"{Fore.RED}❌ Input data akun tidak valid! Coba lagi...\n")