# ==========APLIKASI STOK ATK==========
#     1. Rekap Stok Barang
#     2. Mengubah Stok Barang
#     3. Menambahkan Item Barang
#     4. Menghapus Item Barang
#     5. Request Barang
#     6. Exit
#     Silahkan Masukkan Menu yang Anda Inginkan: ''')                
                



List_barang = [['A11','Kertas A4',10, "Rim"],
               ['B21','Pulpen Hitam',20, "Box"],
               ['C31','Gunting',5, "Pcs"],
               ['D41', 'Penggaris', 10, 'Pcs'], 
               ['E51', 'Stapler', 3, 'Pcs'],
               ['A12', 'Kertas F4', 4, 'Rim'],
               ['B22', 'Pulpen Merah', 2, 'Box'],
               ['C32', 'Stabilo', 1, 'Box'],
               ['D42', 'Post It', 5, 'Box'],
               ['E52', 'Penghapus', 2, 'Box']
               ]

#Read Function
def Read_Data():
    read = True
    while read != "3":
        print("\n==========REKAP PERSEDIAAN ATK==========")
        print('1. Rekap Seluruh Stok Barang')
        print('2. Rekap Barang Tertentu')
        print('3. Kembali ke Menu Utama')
        
        read = input('Pilih SubMenu [1-3]:')
        if read == '1':
            if len(List_barang)!= 0:
                print('Rekap Stok Barang:')
                print('No\t| Kode \t|Nama \t \t|  Stock\t|Satuan\t')
                for  i in range(len(List_barang)):
                    print (f'{i+1}. \t| {List_barang[i][0]} \t|{List_barang[i][1]}\t|  {List_barang[i][2]}\t \t| {List_barang[i][3]}\t')
            else:
                print('\n __________Tidak Ada Data Barang__________')
            continue
        elif read =='2':
            if len(List_barang)!=0:
                brg=input('Masukkan Kode Barang: ').upper()
                found = False
                print('No\t| Kode \t|Nama \t \t|  Stock\t|Satuan\t')
                for i in range(len(List_barang)):
                    if List_barang[i][0]==brg:
                        print (f'{i+1}. \t| {List_barang[i][0]} \t|{List_barang[i][1]}\t|  {List_barang[i][2]}\t \t| {List_barang[i][3]}\t')
                        found = True
                        break
                if not found:
                    print('\n __________Tidak Ada Data Barang__________')
            else:
                print('\n __________Tidak Ada Data Barang__________')
                continue
                    
        elif read =='3':
            break
        else: 
            print('Pilihan Tidak Valid')
            
            
#Mengubah Data Stok
def ubah_Data():
    ubah = True
    while ubah !='2':
        print("\n==========UBAH STOK ATK==========")
        print('1. Ubah Stok Barang')
        print('2. Kembali ke Menu Utama')
        ubah = input('Masukkan Submenu [1-2]: ')
        if ubah == "1":
            item_ubah = input('Masukkan Kode Barang yang akan diubah: ')
            found = False
            for i in range(len(List_barang)):
                if List_barang[i][0]== item_ubah:
                    jumlah_baru = int(input('Masukkan Stok Barang : '))
                    List_barang[i][2]= jumlah_baru
                    print('Stok {} berhasil di ubah'.format(List_barang[i][1]))
                    print('Update Stok Baru: ')
                    print('No\t| Kode \t|Nama \t \t|  Stock\t|Satuan\t')
                    print (f'{i+1}. \t| {List_barang[i][0]} \t|{List_barang[i][1]}\t|  {List_barang[i][2]}')
                    found = True
                    break
            if not found:
                print('\n __________Tidak Ada Data Barang__________')
        elif ubah=='2':
            break
        else:
            print('Pilihan Tidak Valid')


#Menambah Item Barang 
def tambah_item():
    tambah = True
    while tambah !='2':
        print("\n==========TAMBAH ITEM ATK==========")
        print('1. Tambah Item')
        print('2. Kembali ke Menu Utama')
        tambah = input ('Masukkan Submenu [1-2]: ')
        if tambah == '1':
            kode_baru = input('Masukkan Kode Barang :').upper()
            if all(kode_baru != item[0] for item in List_barang):
                    nama_baru = input('Masukkan Nama Barang : ')
                    if 7<=len(nama_baru)<=12:
                        stok_barang = int(input('Masukkan Stok Barang: '))
                        satuan_barang = (input('Masukkan Satuan Barang: '))
                        list_baru = [kode_baru, nama_baru, stok_barang, satuan_barang]
                        List_barang.append(list_baru)
                        print('Item Barang Berhasil di Tambahkan')
                        print('Update Rekap Stok Barang :')
                        print('No\t| Kode \t|Nama \t \t|  Stock\t|Satuan\t')
                        for i, item in enumerate(List_barang):
                            print (f'{i+1}. \t| {item[0]} \t|{item[1]}\t|  {item[2]}\t\t| {item[3]}\t')
                    else:
                        print("Nama Barang harus memiliki panjang 7 - 12 karakter")
            else: 
                print("==========Data Barang Sudah Digunakan==========")
        elif tambah == '2':
            break
        else:
            print('Plihian Tidak Valid')

#Menghapus Data Barang
def hapus_data():
    hapus = True
    while hapus != '2':
        print("\n==========HAPUS DATA==========")
        print('1. Hapus Data')
        print('2. Kembali ke Menu Utama')
        hapus = input('Masukkan Submenu [1-2]: ')
        if hapus =='1':
            hapus_brg = input('Masukkan Kode Barang yang akan Dihapus: ').upper()
            found = False
            for i in range(len(List_barang)):
                if List_barang[i][0]== hapus_brg:
                    del List_barang[i]
                    print("Data Berhasil Dihapus")
                    found = True
                    break
            if not found:
                print('__________Data Tidak di Temukan_________')
        elif hapus =='2':
            break
        else:
            print('Pilihan Tidak Valid')

#Request Barang
def request_data():
    print("\n==========REQUEST BARANG==========")
    items_requested = []
    while True:
        kode_barang = input("Masukkan Kode Barang yang Anda Inginkan (tekan 'q' untuk selesai): ").upper()
        if kode_barang.lower() == 'q':
            break
        found = False
        for i in range(len(List_barang)):
            if List_barang[i][0] == kode_barang:
                jumlah_request = int(input(f"Masukkan Jumlah {List_barang[i][1]} yang Anda Inginkan: "))
                if jumlah_request <= List_barang[i][2]:
                    items_requested.append([List_barang[i][0], List_barang[i][1], jumlah_request])
                    List_barang[i][2] -= jumlah_request
                    found = True
                    break
                else:
                    print("Jumlah yang diminta melebihi stok yang tersedia.")
                    found = True
                    break
        if not found:
            print("Barang tidak ditemukan dalam stok.")

    # Output list barang yang di-request
    print("\n==========LIST BARANG YANG DI-REQUEST==========")
    if items_requested:
        print('No\t| Kode \t| Nama Barang \t| Jumlah')
        for i, request in enumerate(items_requested, 1):
            print(f"{i}\t| {request[0]}\t| {request[1]}\t| {request[2]}")
    else:
        print("Tidak ada barang yang di-request.")

    # Output list barang setelah request
    print("\n\n==========SISA STOOK SAAT INI==========")
    print('No\t| Kode \t|Nama \t \t|  Stock\t|Satuan\t')
    for i, barang in enumerate(List_barang, 1):
        print(f"{i}\t| {barang[0]}\t| {barang[1]}\t| {barang[2]}\t\t| {barang[3]}\t")



    

while(True):
    Menu = input('''\n==========APLIKASI STOK ATK==========
    1. Rekap Stok Barang
    2. Mengubah Stok Barang
    3. Menambahkan Item Barang
    4. Menghapus Item Barang
    5. Request Barang
    6. Exit
    Silahkan Masukkan Menu yang Anda Inginkan: ''')
                 
    if Menu == "1":
        Read_Data()
    if Menu == "2":
        ubah_Data()
    if Menu == "3":
        tambah_item()
    if Menu == "4":
        hapus_data()
    if Menu == "5":
        request_data()

    

