import random
import datetime
from customer import Customer

atm=Customer(id)

#Loop benar
while True:
    
    id=int(input("Masukkan Pin anda: "))
    Try = 0
    
    #Looping pemeriksaan
    while (id!=int(atm.checkPin()) and Try<3):
        id=int(input("Pin anda belum benar, coba lagi! : "))
        
        Try+=1
        if Try == 3:
            print('Eror. Silahkan ambil kartu dan coba lagi..')
            exit()

    while (id==int(atm.checkPin())):
        print('--------------------------\n|Welcome to Progate ATM..|\n--------------------------')
        print('\n1 - Cek Saldo \t2 - Debet \t3 - Kredit \t4 - Ganti Pin \t5 - Exit')
        Try=1
        if Try == 1:
            selectMenu=int(input('\nSilahkan pilih menu: '))
    
            if selectMenu == 1:
                print('\nSaldo anda sekarang: Rp',str(atm.checkBalance())+'\n')
                break
            elif selectMenu == 2:
                nominal = float(input('Masukkan nominal saldo: '))
                verify_withdraw = input('Konfirmasi debet dengan nominal Rp. '+str(nominal)+'(y/n)? ')
                
                if verify_withdraw == 'y':
                    print('Saldo awal: Rp.',str(atm.checkBalance()),"")
                else:
                    break
                if nominal<=atm.checkBalance():
                    atm.WithdrawBalance(nominal)
                    print('Transaksi berhasil!')
                    print('Saldo sisa: Rp:',str(atm.checkBalance()),'')
                else:
                    print('Maaf saldo tidak cukup')
                    print('Silahkan tambahkan saldo dahulu')
                
            elif selectMenu == 3:
                nominal = float(input('Masukkan nominal saldo: '))
                verify_deposit = input('Konfirmasi deposit dengan nominal Rp. '+str(nominal)+' (y/n)? ')
                
                if verify_deposit == 'y':
                    atm.depositBalance(nominal)
                    print('Saldo sekarang: Rp.',str(atm.checkBalance()),"")
                else:
                    break

            elif selectMenu == 4:
                verify_pin=int(input('masukkan pin anda: '))
                while verify_pin != int(atm.checkPin()):
                    print('pin anda salah, silahkan ulang: ')
                updated_pin=int(input('silahkan masukkan pin baru:'))
                print('pin anda berhasil diganti!')
                verify_newpin = int(input('Coba masukkan pin baru anda: '))

                if verify_newpin == updated_pin:
                    print('pin baru sudah berhasil')
                else:
                    print('Pin anda salah!')
                    break

            elif selectMenu == 5:
                print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
                print("No. Rekord: ", random.randint(100000, 1000000))
                print("Tanggal: ", datetime.datetime.now())
                print("Saldo akhir: ", atm.checkBalance())
                print("Terima kasih telah menggunakan ATM Progate!")
                exit()
            else:
                print('Eror. Maaf, menu tidak tersedia')
