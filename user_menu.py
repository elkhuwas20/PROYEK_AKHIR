from prettytable import PrettyTable
from drama import DramaManager
from storage import Storage

class UserManager:
    def _init_(self):
        self.drama_manager = DramaManager()
        self.storage = Storage()
    
    def menu_user(self, username):
        while True:
            print("\n" + "="*60)
            print(f"SELAMAT DATANG, {username.upper()}!")
            print("="*60)
            print("1. Lihat Semua Drama Korea")
            print("2. Tambah ke Watchlist")
            print("3. Lihat Watchlist Saya")
            print("4. Hapus dari Watchlist")
            print("5. Cari Drama")
            print("6. Logout")
            
            choice = input("\nPilih menu (1-6): ").strip()
            
            if choice == '1':
                self.drama_manager.read_dramas()
            elif choice == '2':
                self.create_watchlist(username)
            elif choice == '3':
                self.read_watchlist(username)
            elif choice == '4':
                self.remove_watchlist(username)
            elif choice == '5':
                self.search_drama()
            elif choice == '6':
                print("Sampai jumpa!")
                break
            else:
                print("334Pilihan tidak valid!")
    
    def create_watchlist(self, username):
        print("\n" + "="*50)
        print("TAMBAH KE WATCHLIST")
        print("="*50)
        
        self.drama_manager.display_all_dramas()
        judul = input("\nMasukkan judul drama yang ingin ditambahkan: ").strip()
        
        dramas = self.storage.load_dramas()
        users = self.storage.load_users()
        
        if judul not in dramas:
            print("Drama tidak ditemukan!")
            return
        
        if judul in users[username]["watchlist"]:
            print("Drama sudah ada di watchlist Anda!")
            return
        
        users[username]["watchlist"].append(judul)
        self.storage.save_users(users)
        print(f" '{judul}' berhasil ditambahkan ke watchlist!")
    
    def read_watchlist(self, username):
        print("\n" + "="*50)
        print("WATCHLIST SAYA")
        print("="*50)
        
        users = self.storage.load_users()
        dramas = self.storage.load_dramas()
        watchlist = users[username]["watchlist"]
        
        if not watchlist:
            print("Watchlist Anda masih kosong.")
            return
        
        table = PrettyTable()
        table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]
        
        for i, judul in enumerate(watchlist, 1):
            if judul in dramas:
                data = dramas[judul]
                table.add_row([
                    i,
                    judul,
                    data["genre"],
                    data["episode"],
                    data["status"],
                    data["rating"]
                ])
        
        print(table)
    
    def remove_watchlist(self, username):
        print("\n" + "="*50)
        print("HAPUS DARI WATCHLIST")
        print("="*50)
        
        self.view_my_watchlist(username)
        
        users = self.storage.load_users()
        watchlist = users[username]["watchlist"]
        
        if not watchlist:
            return
        
        judul = input("\nMasukkan judul drama yang ingin dihapus: ").strip()
        
        if judul not in watchlist:
            print("Drama tidak ditemukan di watchlist Anda!")
            return
        
        confirm = input(f"Apakah Anda yakin ingin menghapus '{judul}' dari watchlist? (y/n): ").lower()
        if confirm == 'y':
            users[username]["watchlist"].remove(judul)
            self.storage.save_users(users)
            print("Drama berhasil dihapus dari watchlist!")
        else:
            print("Penghapusan dibatalkan.")
    
    def search_drama(self):
        print("\n" + "="*50)
        print("CARI DRAMA")
        print("="*50)
        
        keyword = input("Masukkan judul atau genre drama: ").strip()
        results = self.drama_manager.search_drama(keyword)
        
        if not results:
            print("Tidak ditemukan drama dengan kata kunci tersebut.")
            return
        
        table = PrettyTable()
        table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]
        
        for i, (judul, data) in enumerate(results.items(), 1):
            table.add_row([
                i,
                judul,
                data["genre"],
                data["episode"],
                data["status"],
                data["rating"]
            ])
        
        print(f"\nHasil pencarian untuk '{keyword}':")
        print(table)