import re

def validasi_kartu_kredit(nomor_kartu):
    if len(nomor_kartu)==16:
        pola=r'^[456]\d{15}$'
        if nomor_kartu == pola:
            print("Valid Reguler")
        if nomor_kartu==pola:
            if re.search(r'8{4}'):
                print("Valid Platinum")
    else:
        print("tidak valid")
    
# nomor_kartu = '4111111111111111'
# hasil = validasi_kartu_kredit(nomor_kartu)
# print(hasil)

nomor_kartu = '4234567888823456'
print(len(nomor_kartu))
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)
