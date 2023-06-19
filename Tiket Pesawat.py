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


