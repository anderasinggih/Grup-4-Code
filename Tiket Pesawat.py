tiket_tersedia = [
    {
        'maskapai': 'Garuda Indonesia',
        'kode_penerbangan': 'GA123',
        'harga': 1000000,
        'jadwal': [
            {'jam': '08:00', 'asal': 'Jakarta', 'tujuan': 'Surabaya'},
            {'jam': '12:00', 'asal': 'Jakarta', 'tujuan': 'Surabaya'},
            {'jam': '16:00', 'asal': 'Jakarta', 'tujuan': 'Surabaya'}
        ],
        'kursi': 100
    },
    {
        'maskapai': 'Lion Air',
        'kode_penerbangan': 'JT456',
        'harga': 800000,
        'jadwal': [
            {'jam': '09:00', 'asal': 'Jakarta', 'tujuan': 'Bali'},
            {'jam': '13:00', 'asal': 'Jakarta', 'tujuan': 'Bali'},
            {'jam': '17:00', 'asal': 'Jakarta', 'tujuan': 'Bali'}
        ],
        'kursi': 80
    },
    {
        'maskapai': 'AirAsia',
        'kode_penerbangan': 'QZ789',
        'harga': 600000,
        'jadwal': [
            {'jam': '10:00', 'asal': 'Jakarta', 'tujuan': 'Yogyakarta'},
            {'jam': '14:00', 'asal': 'Jakarta', 'tujuan': 'Yogyakarta'},
            {'jam': '18:00', 'asal': 'Jakarta', 'tujuan': 'Yogyakarta'}
        ],
        'kursi': 120
    },
    {
        'maskapai': 'Citilink',
        'kode_penerbangan': 'QG321',
        'harga': 500000,
        'jadwal': [
            {'jam': '11:00', 'asal': 'Jakarta', 'tujuan': 'Medan'},
            {'jam': '15:00', 'asal': 'Jakarta', 'tujuan': 'Medan'},
            {'jam': '19:00', 'asal': 'Jakarta', 'tujuan': 'Medan'}
        ],
        'kursi': 70
    },
    {
        'maskapai': 'Batik Air',
        'kode_penerbangan': 'ID987',
        'harga': 900000,
        'jadwal': [
            {'jam': '12:00', 'asal': 'Jakarta', 'tujuan': 'Bandung'},
            {'jam': '16:00', 'asal': 'Jakarta', 'tujuan': 'Bandung'},
            {'jam': '20:00', 'asal': 'Jakarta', 'tujuan': 'Bandung'}
        ],
        'kursi': 50
    }
]

pesanan_tiket = []

# Fungsi untuk melihat tiket (menu pembeli)
def info_tiket_penerbangan():
    print("\nInfo Tiket Penerbangan")
    for tiket in tiket_tersedia:
        print("\nDetail Tiket:")
        print("Maskapai:", tiket['maskapai'])
        print("Kode Penerbangan:", tiket['kode_penerbangan'])
        print("Harga Tiket:", tiket['harga'])
        print("Jadwal Penerbangan:")
        for jadwal_penerbangan in tiket['jadwal']:
            print(f"- Jam: {jadwal_penerbangan['jam']}")
            print(f"  Asal: {jadwal_penerbangan['asal']}")
            print(f"  Tujuan: {jadwal_penerbangan['tujuan']}")
        print("Kursi Tersedia:", tiket['kursi'])

# Fungsi untuk membeli tiket (menu pembeli)
def beli_tiket():
    print("\nBeli Tiket")
    asal = input("Masukkan Lokasi Pemberangkatan: ")
    tujuan = input("Masukkan Lokasi Tujuan: ")


    tiket_ditemukan = False
    for tiket in tiket_tersedia:
        if tiket['jadwal'][0]['asal'] == asal and tiket['jadwal'][0]['tujuan'] == tujuan:
            print("Maskapai:", tiket['maskapai'])
            print("Kode Penerbangan:", tiket['kode_penerbangan'])
            print("Harga Tiket:", tiket['harga'])
            print("Jadwal Penerbangan:")
            for jadwal_penerbangan in tiket['jadwal']:
                print(f"- Jam: {jadwal_penerbangan['jam']}")
            print("Kursi Tersedia:", tiket['kursi'])
            print("")


            jadwal_terpilih = input("Masukkan Jadwal Penerbangan yang Anda Inginkan: ")
            jumlah_tiket = int(input("Masukkan Jumlah Tiket yang Ingin Dibeli: "))


            kursi_tersedia = tiket['kursi']
            if jumlah_tiket > kursi_tersedia:
                print("Jumlah tiket yang diminta melebihi kursi yang tersedia.")
                return


            nama_pembeli = input("Masukkan Nama Pembeli: ")
            alamat = input("Masukkan Alamat: ")
            no_telp = input("Masukkan Nomor Telepon: ")


            pesanan = {
                'maskapai': tiket['maskapai'],
                'kode_penerbangan': tiket['kode_penerbangan'],
                'harga': tiket['harga'],
                'jadwal': jadwal_terpilih,
                'jumlah_tiket': jumlah_tiket,
                'nama_pembeli': nama_pembeli,
                'alamat': alamat,
                'no_telp': no_telp
            }


            pesanan_tiket.append(pesanan)


            tiket['kursi'] -= jumlah_tiket
            tiket_ditemukan = True
            print("Pemesanan tiket berhasil, Silahkan melanjutkan pembayaran di kasir")


    if not tiket_ditemukan:
        print("Tidak ada tiket tersedia untuk rute tersebut.")


# Fungsi untuk melihat pesanan (menu pembeli)
def lihat_pesanan():
    print("\nLihat Pesanan")
    if len(pesanan_tiket) == 0:
        print("Belum ada pesanan tiket.")
    else:
        for pesanan in pesanan_tiket:
            print("\nDetail Pesanan:")
            print("Maskapai:", pesanan['maskapai'])
            print("Kode Penerbangan:", pesanan['kode_penerbangan'])
            print("Harga Tiket:", pesanan['harga'])
            print("Jadwal Penerbangan:", pesanan['jadwal'])
            print("Jumlah Tiket:", pesanan['jumlah_tiket'])
            print("Nama Pembeli:", pesanan['nama_pembeli'])
            print("Alamat:", pesanan['alamat'])
            print("Nomor Telepon:", pesanan['no_telp'])

# Fungsi untuk mencetak tiket (menu pembeli)
def cetak_tiket():
    print("\nCetak Tiket")
    if len(pesanan_tiket) == 0:
        print("Belum ada pesanan tiket.")
    else:
        kode_penerbangan = input("Masukkan Kode Penerbangan: ")
        tiket_ditemukan = False
        for pesanan in pesanan_tiket:
            if pesanan['kode_penerbangan'] == kode_penerbangan:
                print("\nDetail Tiket:")
                print("Maskapai:", pesanan['maskapai'])
                print("Kode Penerbangan:", pesanan['kode_penerbangan'])
                print("Harga Tiket:", pesanan['harga'])
                print("Jadwal Penerbangan:", pesanan['jadwal'])
                print("Jumlah Tiket:", pesanan['jumlah_tiket'])
                print("Nama Pembeli:", pesanan['nama_pembeli'])
                print("Alamat:", pesanan['alamat'])
                print("Nomor Telepon:", pesanan['no_telp'])
                tiket_ditemukan = True

        if not tiket_ditemukan:
            print("Tiket tidak ditemukan.")

# Fungsi untuk menu pembeli
def menu_pembeli():
    while True:
        print("\n=== MENU PEMBELI ===")
        print("1. Info Tiket Penerbangan")
        print("2. Beli Tiket")
        print("3. Lihat Pesanan")
        print("4. Cetak Tiket")
        print("5. Kembali")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            info_tiket_penerbangan()
        elif pilihan == '2':
            beli_tiket()
        elif pilihan == '3':
            lihat_pesanan()
        elif pilihan == '4':
            cetak_tiket()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


