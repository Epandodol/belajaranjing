import json

data1 = []

def tambah_data():
    jumlah_data = int(input("Berapa banyak data yang ingin dimasukkan? "))
    
    for i in range(jumlah_data):
        print(f"Masukkan data ke-{i+1}:")
        nama_orang = input("Masukkan nama: ")
        usia_orang = input("Masukkan usia: ")
        hobi_orang = input("Masukkan hobi: ")
        
        data1.append({
            "nama": nama_orang,
            "usia": usia_orang,
            "hobi": hobi_orang
        })

    print("Data selesai dimasukkan")

    with open('test.json', 'w') as f:
        json.dump(data1, f)

    print("Data telah disimpan di test.json")

def lihat_data():
    try:
        with open('test.json', 'r') as f:
            data = json.load(f)
            print("Data yang telah disimpan:")
            for i, entry in enumerate(data, 1):
                print(f"Data ke-{i}:")
                print(f"Nama: {entry['nama']}")
                print(f"Usia: {entry['usia']}")
                print(f"Hobi: {entry['hobi']}\n")
    except FileNotFoundError:
        print("Tidak ada data yang ditemukan. Silakan tambah data terlebih dahulu.")

def hapus_data():
    try:
        with open('test.json', 'r') as f:
            data = json.load(f)
        
        if not data:
            print("Tidak ada data yang bisa dihapus.")
            return
        
        lihat_data()
        
        indeks = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
        
        if 0 <= indeks < len(data):
            data.pop(indeks)
            with open('test.json', 'w') as f:
                json.dump(data, f)
            print("Data telah dihapus.")
        else:
            print("Nomor data tidak valid.")
    except FileNotFoundError:
        print("Tidak ada data yang ditemukan. Silakan tambah data terlebih dahulu.")
    except json.JSONDecodeError:
        print("Tidak ada data yang valid. Silakan tambah data terlebih dahulu.")

def menu():
    while True:
        user_opsion = int(input("menu:\n\n1. Tambah Data\n2. Lihat Data\n3. Hapus Data\n4. Keluar\nMasukkan opsi: "))
        if user_opsion == 1:
            tambah_data()
        elif user_opsion == 2:
            lihat_data()
        elif user_opsion == 3:
            hapus_data()
        elif user_opsion == 4:
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
