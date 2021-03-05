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

def samakan_koef(matriks_persamaan, matriks_hasil, kolom, koef_ke):
    matriks_temp = matriks_persamaan
    hasil = matriks_hasil
    pengali = []
    if kolom == 2:
        total_koef = 0
        for line in matriks_temp:
            total_koef += 1
        koef = []
        for line in matriks_temp:
            koef.append(line)
        i = 0
        pengali.append(koef[1][koef_ke-1])
        pengali.append(koef[0][koef_ke-1])
        for i in range(0, total_koef):
            if i == 0:
                koef[i][0] = koef[i][0]*pengali[i]
                koef[i][1] = koef[i][1]*pengali[i]
                hasil[i] = hasil[i]*pengali[i]
                print("persamaan ke "+str(i+1)+" akan dikalikan dengan "+str(pengali[i]))
            if i == 1:
                koef[i][0] = koef[i][0]*pengali[i]
                koef[i][1] = koef[i][1]*pengali[i]
                hasil[i] = hasil[i]*pengali[i]
                print("persamaan ke "+str(i+1)+" akan dikalikan dengan "+str(pengali[i]))
    if kolom == 3:
        total_koef = 0
        for line in matriks_temp:
            total_koef += 1
        koef = []
        for line in matriks_temp:
            koef.append(line)
        i = 0
        pengali.append(koef[1][koef_ke-1])
        pengali.append(koef[0][koef_ke-1])
        for i in range(0, total_koef):
            if i == 0:
                koef[i][0] = koef[i][0]*pengali[i]
                koef[i][1] = koef[i][1]*pengali[i]
                koef[i][2] = koef[i][2]*pengali[i]
                hasil[i] = hasil[i]*pengali[i]
                print("persamaan ke "+str(i+1)+" akan dikalikan dengan "+str(pengali[i]))
            if i == 1:
                koef[i][0] = koef[i][0]*pengali[i]
                koef[i][1] = koef[i][1]*pengali[i]
                koef[i][2] = koef[i][2]*pengali[i]
                hasil[i] = hasil[i]*pengali[i]
                print("persamaan ke "+str(i+1)+" akan dikalikan dengan "+str(pengali[i]))
    output = []
    output.append(koef)
    output.append(hasil)
    return output

def print_as_spl(matriks_persamaan):
    matriks_temp = matriks_persamaan[0]
    hasil = matriks_persamaan[1]
    string = ''
    if type(matriks_temp[0]) == list:
        for i in range(0, len(matriks_temp)):
            for j in range(0, len(matriks_temp[i])):
                if (matriks_temp[i][j] != 0):
                    if (matriks_temp[i][j] > 0 and j > 0):
                        string += '+'
                    if matriks_temp[i][j] != 0 and matriks_temp[i][j] != 1 and matriks_temp[i][j] != -1:
                        string += str(matriks_temp[i][j])
                    if matriks_temp[i][j] == -1:
                        string += '-'
                    if j == 0:
                        string += 'x'
                    if j == 1:
                        string += 'y'
                    if j == 2:
                        string += 'z'
            string += "="+str(hasil[i])
            print(string)
            string = ''
    if type(matriks_temp[0]) == int:
        for i in range(0, len(matriks_temp)):
            if matriks_temp[i] != 0:
                if (matriks_temp[i] > 0 and i > 0):
                    string += '+'
                if matriks_temp[i] != 0 and matriks_temp[i] != 1 and matriks_temp[i] != -1:
                    string += str(matriks_temp[i])
                if matriks_temp[i] == -1:
                    string += '-'
                if i == 0:
                    string += 'x'
                if i == 1:
                    string += 'y'
                if i == 2:
                    string += 'z'
        string += '='
        string += str(hasil[0])
        if string[0] == "+": string = string[1:]
        print(string)

def pengurangan_koef(matriks_persamaan, kolom):
    matriks_temp = matriks_persamaan[0]
    hasil = matriks_persamaan[1]
    output = []
    output_hasil = []
    for i in range(0, len(matriks_temp[0])):
        matriks_temp[0][i] -= matriks_temp[1][i]
    for i in range(1, len(hasil)):
        hasil[0] -= hasil[i]
    output.append(matriks_temp[0])
    output_hasil.append(hasil[0])
    output.append(output_hasil)
    return output

def sisa_dari_2var(matriks_persamaan, matriks_hasil, kolom_dicari, nilai_variabel_lain, kondisi):
    matriks_temp = matriks_persamaan
    kolom_dicari -= 1
    string = ''
    if kolom_dicari == 0:
        hasil = matriks_temp[1]*nilai_variabel_lain
        hasil = (matriks_hasil-hasil)/matriks_temp[0]
        string += 'x = '+str(hasil)
    if kolom_dicari == 1:
        hasil = matriks_temp[0]*nilai_variabel_lain
        hasil = (matriks_hasil-hasil)/matriks_temp[1]
        string += 'y = '+str(hasil)
    if kondisi == 'print': return string
    if kondisi == 'nilai': return hasil

def nilai_variabel(matriks_persamaan, koef_0, kondisi):
    matriks_temp = matriks_persamaan
    koef_0 -= 1
    if koef_0 == 0:
        y = matriks_temp[1][0]/matriks_temp[0][1]
        if kondisi == 'print':
            return print("y = "+str(y))
        if kondisi == 'nilai':
            return y
    if koef_0 == 1:
        x = matriks_temp[1][0]/matriks_temp[0][0]
        if kondisi == 'print':
            return print("x = "+str(x))
        if kondisi == 'nilai':
            return x

def nilai_variabel_dari3(matriks_persamaan, koef_dicari, kondisi):
    matriks_temp = matriks_persamaan
    koef_dicari -= 1
    string = ''
    nilai = (matriks_temp[1][0])/matriks_temp[0][koef_dicari]
    if kondisi == 'print':
        if koef_dicari == 0: string += 'x = '
        if koef_dicari == 1: string += 'y = '
        if koef_dicari == 2: string += 'z = '
        return print(string+str(nilai))
    if kondisi == 'nilai':
        return nilai

def kurangi_koef(matriks_persamaan):
    matriks_temp = matriks_persamaan[0]
    matriks_hasil = matriks_persamaan[1]

def spltv_to_spldv(matriks_persamaan, hasil):
    matriks_temp = matriks_persamaan
    matriks_hasil = hasil
    output = []
    output1 = []
    output2 = []
    persamaan_baru = []
    hasil_baru = []
    keluaran = []
    total_koef = 0
    matriks_olah = []
    for line in matriks_temp:
        total_koef += 1
    koef = []
    output = samakan_koef(matriks_temp[:][:-1], matriks_hasil[:-1], 3, 1)
    print_as_spl(output)
    output1 = pengurangan_koef(output, 1)
    print_as_spl(output1)
    print('\n')
    matriks_olah.append(matriks_temp[:][1:])
    matriks_olah.append(matriks_hasil[1:])
    print_as_spl(matriks_olah)
    output = samakan_koef(matriks_temp[:][1:], matriks_hasil[1:], 3, 1)
    output2 = pengurangan_koef(output, 1)
    print_as_spl(output2)
    persamaan_baru.append(output1[0])
    persamaan_baru.append(output2[0])
    hasil_baru.append(output1[1])
    hasil_baru.append(output2[1])
    keluaran.append(persamaan_baru)
    keluaran.append(hasil_baru)
    print(" ")
    print_as_spl(output1)
    print_as_spl(output2)
    return keluaran

def matikan_1_dari_3(matriks_persamaan):
    matriks_temp = matriks_persamaan[0]
    matriks_hasil = []
    matriks_hasil.append(matriks_persamaan[1][0][0])
    matriks_hasil.append(matriks_persamaan[1][1][0])
    output = samakan_koef(matriks_temp, matriks_hasil, 3, 2)
    print_as_spl(output)
    output = pengurangan_koef(output, 3)
    print_as_spl(output)
    return nilai_variabel_dari3(output, 3, 'nilai')


if perintah == 'read' :
    print ("format perintah : python tugas02.py read nama_file1.txt nama_file2.txt ...dst...")
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
    print("format perintah : python tugas02.py add nama_file1.txt nama_file2.txt ...dst...")
    if len(arg) < 4:
        print ("Harap masukkan lebih dari 1 file matriks seperti perintah di bawah :")
        print ("python tugas02.py add matriks-1 matriks-2")
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
    print("format perintah : python tugas02.py sub nama_file1.txt nama_file2.txt ...dst...")
    if len(arg) < 4:
        print ("Harap masukkan lebih dari 1 file matriks seperti perintah di bawah :")
        print ("python tugas02.py sub matriks-1 matriks-2")
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
    print("format perintah : python tugas02.py scalar nilai_skalar nama_file1.txt")
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
    print("format perintah : python tugas02.py mul nama_file1.txt nama_file2.txt")
    if len(arg) < 4:
        print ("Harap masukkan lebih dari 1 file matriks seperti perintah di bawah :")
        print ("python tugas02.py mul matriks-1 matriks-2")
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
    print("format perintah : python tugas02.py det namna_file1.txt")
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

if perintah == 'elm':
    print("format perintah : python tugas02.py elm matriksA.txt matriksB.txt")
    file = arg[3]
    baca()
    hasil = []
    kolom2 = cek_ukuran('baris')
    i = 0
    for line in content:
        line = line.strip('\n')
        line = int(line)
        hasil.append(line)
    file = arg[2]
    baca()
    baris, kolom = (cek_ukuran('baris'), cek_ukuran('kolom'))
    if (kolom != kolom2):
        print ("E: Ukuran kolom matriks pertama tidak sama dengan kolom kedua.")
        exit()
    if (baris != kolom):
        print("E: Ukuran baris dan kolom matriks tidak sama.")
        exit()
    if kolom == 2:
        matriks_temp = []
        matriks_asal = []
        persamaan = []
        for line in content:
            nilai = line.split(' ')
            for i in range(0, len(nilai)-1):
                nilai[i] = int(nilai[i])
            nilai[len(nilai)-1] = int(nilai[len(nilai)-1].strip('\n'))
            matriks_temp.append(nilai)
        persamaan.append(matriks_temp)
        persamaan.append(hasil)
        print_as_spl(persamaan)
        print(" ")
        output = samakan_koef(matriks_temp, hasil, kolom2, 1)
        print_as_spl(output)
        output = pengurangan_koef(output, kolom2)
        print_as_spl(output)
        y = nilai_variabel(output, 1, 'nilai')
        print('y = '+str(y))
        print('')
        x = sisa_dari_2var(matriks_temp[1], hasil[1], 1, nilai_variabel(output, 1, 'nilai'), 'nilai')
        print('x = '+str(x))
        print('')
        print('Maka = ')
        print('x = '+str(x))
        print('y = '+str(y))
        exit()
    if kolom == 3:
        matriks_temp = []
        matriks_asal = []
        persamaan = []
        j = 0
        for line in content:
            nilai = line.split(' ')
            for i in range(0, len(nilai)-1):
                nilai[i] = int(nilai[i])
            nilai[len(nilai)-1] = int(nilai[len(nilai)-1].strip('\n'))
            matriks_temp.append(nilai)
        persamaan.append(matriks_temp)
        persamaan.append(hasil)
        print_as_spl(persamaan)
        persamaan_baru = spltv_to_spldv(matriks_temp, hasil)
        print(" ")
        z = matikan_1_dari_3(persamaan_baru)
        print("z = "+str(z))
        j = 0
        print('')
        matriks_baru = []
        for line in content:
            if (j < 2):
                nilai = line.split(' ')
                for i in range(0, len(nilai)-1):
                    nilai[i] = int(nilai[i])
                nilai[len(nilai)-1] = int(nilai[len(nilai)-1].strip('\n'))
                hasil[j] = hasil[j]-(z*nilai[len(nilai)-1])
                nilai = nilai[:-1]
                j += 1;
                matriks_asal.append(nilai)
        matriks_baru.append(matriks_asal)
        matriks_baru.append(hasil)
        print_as_spl(matriks_baru)
        print('')
        output = samakan_koef(matriks_asal, hasil, 2, 2)
        matriks_terbaru = output[0]
        hasil_terbaru = output[1][:-1]
        olah_baru = []
        olah_baru.append(matriks_terbaru)
        olah_baru.append(hasil_terbaru)
        print_as_spl(output)
        print('')
        output = pengurangan_koef(olah_baru, 1)
        print_as_spl(output)
        x = nilai_variabel(output, 2, 'nilai')
        print("x = "+str(x))
        print('')
        matriks_akhir = []
        hasil_baru = []
        hasil_baru = [matriks_baru[1][1]]
        matriks_akhir.append(matriks_baru[0][1])
        matriks_akhir.append(hasil_baru)
        matriks_akhir[1][0] = matriks_akhir[1][0]-(matriks_akhir[0][0]*x)
        matriks_akhir[0][0] = 0
        y = nilai_variabel(matriks_akhir, 1, 'nilai')
        print("y = "+str(y))
        print('')
        print('Maka nilainya adalah :')        
        print('x = '+str(x))
        print('y = '+str(y))
        print('z = '+str(z))
        exit()

# def masukkan_z()



print ("E: Perintah salah, harap coba lagi.\n\n")
print ("Tugas 01 -- Matematika Lanjut | Imam Mashur - 23220368\nProgram Operasi Dasar Matriks")
print ("Tugas 02 -- Matematika Lanjut | Imam Mashur - 23220368\nMetode Eliminasi Persamaan Linier dengan Input Matriks")
print ("Format perintah menjalanklan program : ")
print ("python tugas02.py 'perintah' 'argumen-1' 'argumen-2' dst....")
print ("daftar perintah tersedia : read add sub mul scalar det")
print ("Selamat mencoba")