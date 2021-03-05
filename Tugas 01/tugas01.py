# Nama : Imam Mashur
# NIM : 23220368
# Tugas 01 - Matematika Lanjut

import sys

arg = sys.argv

perintah = arg[1]
global file

print ('PERINTAH : ' + perintah)

def baca():
    try:
        with open(file) as f:
            global content
            content = f.readlines()
    except IOError:
        print ("E: File tidak ditemukan!")
        exit()

def tampilkan():
    for line in content:
        print(line),
        
def generate_matriks_0(baris, kolom):
    matriks_hasil = []
    for i in range(baris):
        isi_perkolom = []
        for j in range(kolom):
            isi_perkolom.append(0)
        matriks_hasil.append(isi_perkolom)
    return matriks_hasil
        
def cek_ukuran(output):
    baris = 0
    kolom = 0
    for line in content:
        isi = line.split(' ')
        kolom = len(isi)
        baris += 1
    if output == 'baris':
        return baris
    if output == 'kolom':
        return kolom
    if output == 'semua':
        return str(baris)+"x"+str(kolom)

def penjumlahan_matriks(baris, kolom, matriks_a, matriks_b):
    matriks_hasil = []
    for i in range(baris):
        isi_perkolom = []
        for j in range(kolom):
            isi_perkolom.append(int(matriks_a[i][j]) + int(matriks_b[i][j]))
        matriks_hasil.append(isi_perkolom)
    return matriks_hasil

def pengurangan_matriks(baris, kolom, matriks_a, matriks_b):
    matriks_hasil = []
    for i in range(baris):
        isi_perkolom = []
        for j in range(kolom):
            isi_perkolom.append(int(matriks_a[i][j]) - int(matriks_b[i][j]))
        matriks_hasil.append(isi_perkolom)
    return matriks_hasil

def pengurangan_matriks(baris, kolom, matriks_a, matriks_b):
    matriks_hasil = []
    for i in range(baris):
        isi_perkolom = []
        for j in range(kolom):
            isi_perkolom.append(int(matriks_a[i][j]) - int(matriks_b[i][j]))
        matriks_hasil.append(isi_perkolom)
    return matriks_hasil

def perkalian_skalar(baris, kolom, skalar, matriks):
    matriks_hasil = []
    for i in range(baris):
        isi_perkolom = []
        for j in range(kolom):
            isi_perkolom.append(int(matriks[i][j])*int(skalar))
        matriks_hasil.append(isi_perkolom)
    return matriks_hasil

def perkalian_matriks(baris, kolom, baris_b, matriks_a, matriks_b):
    matriks_hasil = []
    for i in range(baris):
        isi_perkolom = []
        for j in range(kolom):
            if (j == baris_b):
                break
            total = 0
            for k in range(baris):
                total += int(matriks_a[i][k])*int(matriks_b[k][j])
            isi_perkolom.append(total)
        matriks_hasil.append(isi_perkolom)
    return matriks_hasil

def cari_minor(matriks,baris,kolom):
    matriks_temp = matriks
    matriks_temp = matriks_temp[:baris] + matriks_temp[baris+1:]
    for i in range(0, len(matriks_temp)):
        matriks_temp[i] = matriks_temp[i][:kolom]+matriks_temp[i][kolom+1:]
    return matriks_temp

def cari_determinan(matriks, ordo):
    if ordo == 1:
        return int(matriks[0][0])
    if ordo == 2:
        det = int(matriks[0][0])*int(matriks[1][1])
        det -= int(matriks[1][0])*int(matriks[0][1])
        return det
    det = 0
    matriks_temp = matriks
    for i in range(0, ordo):
        matriks_minor = cari_minor(matriks_temp, 0, i)
        det = det + ((-1)**i)*matriks_temp[0][i]*cari_determinan(matriks_minor, ordo-1)
    return det
 

if perintah == 'read' :
    print ("format perintah : python tugas01.py read nama_file1.txt nama_file2.txt ...dst...")
    for i in range(2, len(arg)):
        mat = i-1
        print ('Matriks ke-' + str(mat) + " =")
        file = arg[i]
        baca()
        tampilkan()
        print ("ukuran matriks = " + cek_ukuran('semua'))
        print (" ")
    exit()

if perintah == "add" :
    print("format perintah : python tugas01.py add nama_file1.txt nama_file2.txt ...dst...")
    if len(arg) < 4:
        print ("Harap masukkan lebih dari 1 file matriks seperti perintah di bawah :")
        print ("python tugas01.py add matriks-1 matriks-2")
        exit()
    matriks_ukuran = []
    for i in range(2, len(arg)):
        file = arg[i]
        baca()
        matriks_ukuran.append(cek_ukuran('semua')) # berarti dari 0, atau i-2
    for i in range(0, len(arg)-2):
        if i != len(arg)-3:
            if matriks_ukuran[i] != matriks_ukuran[i+1]:
                print("ukuran matriks tidak sama!")
                exit()
    file = arg[2]
    baca()
    baris, kolom = (cek_ukuran('baris'), cek_ukuran('kolom'))
    matriks_hasil = generate_matriks_0(baris, kolom)
    for i in range(2, len(arg)):
        file = arg[i]
        baca()
        matriks_temp = []
        for line in content:
            nilai = line.split(' ')
            nilai[len(nilai)-1] = nilai[len(nilai)-1].strip('\n')
            matriks_temp.append(nilai)
        matriks_hasil = penjumlahan_matriks(baris, kolom, matriks_hasil, matriks_temp)
    print ("Hasil = ")
    tmp = ''
    for i in range(baris):
        for j in range(kolom):
            tmp = tmp + str(matriks_hasil[i][j]) + ' '
        print (tmp)
        print (" ")
        tmp = '';
    exit()

if perintah == "sub" :
    print("format perintah : python tugas01.py sub nama_file1.txt nama_file2.txt ...dst...")
    if len(arg) < 4:
        print ("Harap masukkan lebih dari 1 file matriks seperti perintah di bawah :")
        print ("python tugas01.py sub matriks-1 matriks-2")
        exit()
    matriks_ukuran = []
    for i in range(2, len(arg)):
        file = arg[i]
        baca()
        matriks_ukuran.append(cek_ukuran('semua')) # berarti dari 0, atau i-2
    for i in range(0, len(arg)-2):
        if i != len(arg)-3:
            if matriks_ukuran[i] != matriks_ukuran[i+1]:
                print("ukuran matriks tidak sama!")
                exit()
    file = arg[2]
    baca()
    baris, kolom = (cek_ukuran('baris'), cek_ukuran('kolom'))
    matriks_hasil = generate_matriks_0(baris, kolom)
    
    for i in range(2, len(arg)):
        file = arg[i]
        baca()
        matriks_temp = []
        for line in content:
            nilai = line.split(' ')
            nilai[len(nilai)-1] = nilai[len(nilai)-1].strip('\n')
            matriks_temp.append(nilai)
        if i == 2:
            matriks_hasil = matriks_temp
        if i != 2:
            matriks_hasil = pengurangan_matriks(baris, kolom, matriks_hasil, matriks_temp)
    print ("Hasil = ")
    tmp = ''
    for i in range(baris):
        for j in range(kolom):
            tmp = tmp + str(matriks_hasil[i][j]) + ' '
        print (tmp)
        print (" ")
        tmp = '';
    exit()

if perintah == "scalar":
    print("format perintah : python tugas01.py scalar nilai_skalar nama_file1.txt")
    file = arg[3]
    baca()
    baris, kolom = (cek_ukuran('baris'), cek_ukuran('kolom'))
    matriks_temp = []
    for line in content:
        nilai = line.split(' ')
        nilai[len(nilai)-1] = nilai[len(nilai)-1].strip('\n')
        matriks_temp.append(nilai)
    matriks_hasil = perkalian_skalar(baris, kolom, arg[2], matriks_temp)
    tmp = ''
    for i in range(baris):
        for j in range(kolom):
            tmp = tmp + str(matriks_hasil[i][j]) + ' '
        print (tmp)
        print (" ")
        tmp = '';
    exit()

if perintah == "mul" :
    print("format perintah : python tugas01.py mul nama_file1.txt nama_file2.txt")
    if len(arg) < 4:
        print ("Harap masukkan lebih dari 1 file matriks seperti perintah di bawah :")
        print ("python tugas01.py mul matriks-1 matriks-2")
        exit()
    matriks_ukuran = []
    for i in range(2, len(arg)):
        if i == 2:
            file = arg[i]
            baca()
            baris_a = cek_ukuran('baris')
            kolom_a = cek_ukuran('kolom')
        if i == 3:
            file = arg[i]
            baca()
            baris_b = cek_ukuran('baris')
            kolom_b = cek_ukuran('kolom')
    if baris_b != kolom_a:
        print ("E: Ukuran kolom matriks pertama tidak sama dengan baris matriks kedua!")
        exit()
    file = arg[2]
    baca()
    baris, kolom = (cek_ukuran('baris'), cek_ukuran('kolom'))
    matriks_hasil = generate_matriks_0(baris, kolom)
    for i in range(2, len(arg)):
        file = arg[i]
        baca()
        matriks_temp = []
        for line in content:
            nilai = line.split(' ')
            nilai[len(nilai)-1] = nilai[len(nilai)-1].strip('\n')
            matriks_temp.append(nilai)
        if i == 2:
            matriks_hasil = matriks_temp
        if i != 2:
            matriks_hasil = perkalian_matriks(baris, kolom, kolom_b, matriks_hasil, matriks_temp)
    kolom = len(matriks_hasil)
    baris = len(matriks_hasil[0])
    print ("Hasil = ")
    tmp = ''
    for i in range(kolom):
        for j in range(baris):
            tmp = tmp + str(matriks_hasil[i][j]) + ' '
        print (tmp)
        print (" ")
        tmp = '';
    exit()

if perintah == 'det':
    print("format perintah : python tugas01.py det namna_file1.txt")
    file = arg[2]
    baca()
    baris, kolom = (cek_ukuran('baris'), cek_ukuran('kolom'))
    if (baris != kolom):
        print("E: Ukuran baris dan kolom matriks tidak sama.")
        exit()
    matriks_temp = []
    for line in content:
        nilai = line.split(' ')
        for i in range(len(nilai)-1):
            nilai[i] = int(nilai[i])
        nilai[len(nilai)-1] = int(nilai[len(nilai)-1].strip('\n'))
        matriks_temp.append(nilai)
    print ("Hasil = " + str(cari_determinan(matriks_temp, baris)))
    exit()



print ("E: Perintah salah, harap coba lagi.\n\n")
print ("Tugas 01 -- Matematika Lanjut | Imam Mashur - 23220368\nProgram Operasi Dasar Matriks")
print ("Tugas 02 -- Matematika Lanjut | Imam Mashur - 23220368\nMetode Eliminasi Persamaan Linier dengan Input Matriks")
print ("Format perintah menjalanklan program : ")
print ("python tugas01.py 'perintah' 'argumen-1' 'argumen-2' dst....")
print ("daftar perintah tersedia : read add sub mul scalar det")
print ("Selamat mencoba")