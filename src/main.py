# edinici = [0, 'ноль'], [1, "один"], [2, 'два'], [3, 'три'], [4, 'четыре'], [5, 'пять'], [6, 'шесть'], [7, 'семь'], [8, 'восемь'], [9, 'девять']
# desatki = ([10, 'десять'], [11, 'одиннадцать'], [12, 'двенадцать'], [13, 'тринадцать'], [14, 'четырнадцать'], [15, 'пятнадцать'], [16, 'шестнадцать'], [17, 'семнадцать'], [18, 'восемндацать'],[19, 'девятнадцать'],
#            [20, 'двадцать'], [30, 'тридцать'], [40, 'сорок'], [50, 'пятьдесят'],[60, 'шестьдесят'], [70, 'семьдесят'], [80, 'восемьдесят'], [90, 'девяносто'])
# sotni = [100, 'сто'], [200, 'двести'], [300, 'триста'], [400, 'четыреста'], [500, 'пятьсот'], [600, 'шестьсот'], [700, 'семьсот'], [800, 'восемьсот'], [900, 'девятьсот']
# tisyachi = [1000, 'одна тысяча'], [2000, 'две тысячи'], [3000, 'три тысячи'], [4000, 'четыре тысячи'], [5000, 'пять тысяч'], [6000, 'шесть тысяч'], [7000, 'семь тысяч'], [8000, 'восемь тысяч'], [9000, 'девять тысяч']
# operacii = ['+', 'плюс'], ['-', 'минус'], ['*', 'умножить на']

spisok_vsex_chisel = ([0, 'ноль'], [1, "один"], [1, 'одна'], [2, 'два'], [2, 'две'], [3, 'три'], [4, 'четыре'], [5, 'пять'], [6, 'шесть'], [7, 'семь'], [8, 'восемь'], [9, 'девять'],
                      [10, 'десять'], [11, 'одиннадцать'], [12, 'двенадцать'], [13, 'тринадцать'], [14, 'четырнадцать'], [15, 'пятнадцать'], [16, 'шестнадцать'], [17, 'семнадцать'], [18, 'восемнадцать'],[19, 'девятнадцать'],
                      [20, 'двадцать'], [30, 'тридцать'], [40, 'сорок'], [50, 'пятьдесят'],[60, 'шестьдесят'], [70, 'семьдесят'], [80, 'восемьдесят'], [90, 'девяносто'],
                      [100, 'сто'], [200, 'двести'], [300, 'триста'], [400, 'четыреста'], [500, 'пятьсот'], [600, 'шестьсот'], [700, 'семьсот'], [800, 'восемьсот'], [900, 'девятьсот'],
                      [2000, 'две тысячи'], [3000, 'три тысячи'], [4000, 'четыре тысячи'], [5000, 'пять тысяч'], [6000, 'шесть тысяч'], [7000, 'семь тысяч'], [8000, 'восемь тысяч'], [9000, 'девять тысяч'],
                      [10_000, 'десять тысяч'], [20_000, 'двадцать тысяч'], [30_000, 'тридцать тысяч'],    [40_000, 'сорок тысяч'], [50_000, 'пятьдесят тысяч'], [60_000, 'шестьдесят тысяч'],    [70_000, 'семьдесят тысяч'], [80_000, 'восемьдесят тысяч'], [90_000, 'девяносто тысяч'],
                      [100_000, 'сто тысяч'], [200_000, 'двести тысяч'], [300_000, 'триста тысяч'], [400_000, 'четыреста тысяч'], [500_000, 'пятьсот тысяч'], [600_000, 'шестьсот тысяч'],[700_000, 'семьсот тысяч'], [800_000, 'восемьсот тысяч'], [900_000, 'девятьсот тысяч'],
                      [1_000_000, 'один миллион'], [2_000_000, 'два миллиона'], [3_000_000, 'три миллиона'],[4_000_000, 'четыре миллиона'], [5_000_000, 'пять миллионов'], [6_000_000, 'шесть миллионов'], [7_000_000, 'семь миллионов'], [8_000_000, 'восемь миллионов'], [9_000_000, 'девять миллионов'],
                      ['+', 'плюс'], ['-', 'минус'], ['*', 'умножить'], ['/', 'разделить'], ['и', 'и'], ['%', 'остаток'], ['в периоде', 'в периоде'], [1000, 'одна тысяча'], [1000, 'тысяч'], [1000, 'тысячи'], [1000, 'тысяча'],
                      [0.1, 'десятых'], [0.1, 'десятая'], [0.1, 'десятые'], [0.01, 'сотых'], [0.01, 'сотая'], [0.01, 'сотые'], [0.001, 'тысячных'], [0.001, 'тысячная'], [0.001, 'тысячные'], [0.0001, 'десятитысячных'],
                      [0.0001, 'десятитысячная'], [0.0001, 'десятитысячные'], [0.00001, 'стотысячных'], [0.00001, 'стотысячная'], [0.00001, 'стотысячные'], [0.000001, 'миллионных'], [0.000001, 'миллионная'], [0.000001, 'миллионные'],
                      ['(', 'скобка открывается'], [')', 'скобка закрывается'])


primer = input()
# primer = 'четыре разделить на тридцать три'


def slova_v_cifri(chislo):
    # переходит на цифры: двадцать два - 20 2
    primer_chisla_grubie_drobi_razdelno = []
    primer = chislo.split()
    # print(primer)

    for i in primer:
        for j in spisok_vsex_chisel:
            if i == j[1]:
                primer_chisla_grubie_drobi_razdelno.append(j[0])
    # print('primer_chisla_grubie_drobi_razdelno', primer_chisla_grubie_drobi_razdelno)

    # складывает цифры, стоящие рядом, знаки не трогает: 500 40 3 0.001= 543.001
    primer_chisla_grubie_drobi_vmeste = []
    kazhdoe_chislo = primer_chisla_grubie_drobi_razdelno[0]
    for i in range(len(primer_chisla_grubie_drobi_razdelno)):
        if primer_chisla_grubie_drobi_razdelno[i] == 'и':
            primer_chisla_grubie_drobi_vmeste += [kazhdoe_chislo]
            kazhdoe_chislo = primer_chisla_grubie_drobi_razdelno[i + 1]
            continue

        if i+1 < len(primer_chisla_grubie_drobi_razdelno):
            if (primer_chisla_grubie_drobi_razdelno[i] != 'и') and (primer_chisla_grubie_drobi_razdelno[i+1] != 'и') and primer_chisla_grubie_drobi_razdelno[i] > primer_chisla_grubie_drobi_razdelno[i+1]: # 900 9 1000 - 909 1000
                kazhdoe_chislo += primer_chisla_grubie_drobi_razdelno[i+1]
            elif type(primer_chisla_grubie_drobi_razdelno[i]) == type(primer_chisla_grubie_drobi_razdelno[i+1]) and primer_chisla_grubie_drobi_razdelno[i] < primer_chisla_grubie_drobi_razdelno[i+1]: # 909 1000 - 909000
                kazhdoe_chislo *= primer_chisla_grubie_drobi_razdelno[i+1]

        elif  i+1 == len(primer_chisla_grubie_drobi_razdelno):
            primer_chisla_grubie_drobi_vmeste += [kazhdoe_chislo]
    # print('primer_chisla_grubie_drobi_vmeste', primer_chisla_grubie_drobi_vmeste)

    # перерабатывает дробные числа 31.01 в 31*0.01 в 0.31
    primer_chisla_normalnie_drobi = primer_chisla_grubie_drobi_vmeste
    for i in range(len(primer_chisla_normalnie_drobi)):
        if '.' in str(primer_chisla_normalnie_drobi[i]):
            primer_chisla_normalnie_drobi[i] = str(primer_chisla_normalnie_drobi[i]).replace('.', '*0.')
            primer_chisla_normalnie_drobi[i] = eval(str(primer_chisla_normalnie_drobi[i]))
    # print('primer_chisla_normalnie_drobi', primer_chisla_normalnie_drobi)

    if len(primer_chisla_normalnie_drobi) > 1:
        primer_chisla_pravilnie_drobi = [primer_chisla_normalnie_drobi[0] + primer_chisla_normalnie_drobi[1]]
    else:
        primer_chisla_pravilnie_drobi = primer_chisla_normalnie_drobi
    # print('primer_chisla_pravilnie_drobi', primer_chisla_pravilnie_drobi)

    if primer_chisla_pravilnie_drobi[0] == int(primer_chisla_pravilnie_drobi[0]):
        itog_otvet_cifri = int(primer_chisla_pravilnie_drobi[0])
    else:
        itog_otvet_cifri = float(primer_chisla_pravilnie_drobi[0])
    return itog_otvet_cifri


# print(slova_v_cifri(primer))

# строит пример цифрами и знаками
if 'скобка' not in primer:
    skob = False
    primer_cifri = primer.replace('плюс', 'f').replace('минус', 'f').replace('умножить на', 'f').replace('разделить на', 'f').replace('остаток от деления на', 'f').replace('скобка открывается', 'f').replace('скобка закрывается', 'f').replace('f f', 'f')
    primer_cifri = primer_cifri.split(' f ')
    primer = primer.replace('плюс', '+').replace('минус', '-').replace('умножить на', '*').replace('разделить на', '/').replace('остаток от деления на', '%').replace('скобка открывается', '(').replace('скобка закрывается', ')')
else:
    skob = True
    primer_cifri = primer.replace('плюс', 'f').replace('минус', 'f').replace('умножить на', 'f').replace('разделить на', 'f').replace('остаток от деления на', 'f').replace('скобка открывается', 'f').replace('скобка закрывается', 'f')
    primer_cifri = primer_cifri.split('f')
    primer = primer.replace('плюс', '+').replace('минус', '-').replace('умножить на', '*').replace('разделить на', '/').replace('остаток от деления на', '%').replace('скобка открывается', '(').replace('скобка закрывается', ')')
# print('primer_cifri', primer_cifri)

znaki = []
# print('primer', primer)

for i in range(len(primer)):
    if primer[i] in '+-*/%()':
        znaki.append(primer[i])
# print('znaki', znaki)

if skob:
    for i in range(len(primer_cifri)):
        if primer_cifri[i] != '' and primer_cifri[i] != ' ' and primer_cifri[i] != '  ' and primer_cifri[i] != '    ':
            primer_cifri[i] = primer_cifri[i].strip()
            primer_cifri[i] = slova_v_cifri(primer_cifri[i])
    # print('primer_cifri', primer_cifri)
    itog_cifri = [primer_cifri[0]]
    for i in range(len(primer_cifri)-1):
        itog_cifri.append(znaki[i])
        itog_cifri.append(primer_cifri[i+1])

else:
    for i in range(len(primer_cifri)):
        primer_cifri[i] = slova_v_cifri(primer_cifri[i])
# print(primer_cifri)

# (2+2+2+2)*2
# 1+(1+1)*(1+1)
# 2*(2+2)

if not skob:
    itog_cifri = [primer_cifri[0]]
    for i in range(len(znaki)):
        itog_cifri.append(znaki[i])
        itog_cifri.append(primer_cifri[i+1])
# print('itog_cifri', itog_cifri)

for i in range(len(itog_cifri)):
    itog_cifri[i] = str(itog_cifri[i])
itog_cifri = eval(' '.join(itog_cifri))
# print('itog_cifri', itog_cifri)


# разбивает число на целую и дробную часть
itog_otvet_cifri = str(itog_cifri)
minus = False
if itog_otvet_cifri[0] == '-':
    minus = True
    itog_otvet_cifri = itog_otvet_cifri[1:]
if itog_otvet_cifri.find('.') != -1 and itog_otvet_cifri[itog_otvet_cifri.find('.') + 1:] != '0':
    celaia_chast = itog_otvet_cifri[:itog_otvet_cifri.find('.')]
    drobnaia_chast = itog_otvet_cifri[itog_otvet_cifri.find('.') + 1:]
else:
    celaia_chast = str(int(float(itog_otvet_cifri)))
    drobnaia_chast = []
# print('celaia_chast', celaia_chast)
# print('drobnaia_chast', drobnaia_chast)


if len(drobnaia_chast) < 16:
    drobnaia_chast = drobnaia_chast[:6]
elif len(drobnaia_chast) >= 16:
    drobnaia_chast = drobnaia_chast[:14]
# print('drobnaia_chast', drobnaia_chast)

period = do_perioda = 0
if drobnaia_chast != [] and len(drobnaia_chast) == 14:
    for i in range(3):
        if all(drobnaia_chast[j: j + 4] == drobnaia_chast[j + 4: j + 8] for j in range(i, 11 - i - 1 - 2, 3)):
            do_perioda = drobnaia_chast[:i]
            period = drobnaia_chast[i:i + 4]
            break
    for i in range(4):
        if all(drobnaia_chast[j: j + 3] == drobnaia_chast[j + 3: j + 6] for j in range(i, 12 - i - 1 - 2, 3)):
            do_perioda = drobnaia_chast[:i]
            period = drobnaia_chast[i:i + 3]
            break
    for i in range(5):
        if all(drobnaia_chast[j: j + 2] == drobnaia_chast[j + 2: j + 4] for j in range(i, 13 - i - 1, 2)):
            do_perioda = drobnaia_chast[:i]
            period = drobnaia_chast[i:i + 2]
            break
    for i in range(6):
        if all(drobnaia_chast[j + i] == drobnaia_chast[j + 1 + i] for j in range(14 - i - 1)):
            do_perioda = drobnaia_chast[:i]
            period = drobnaia_chast[i]
            break
    # print('period', period)
    # print('do_perioda', do_perioda)

    nyl_per = nyl_do_per = ''
    copy_period = str(period)
    copy_do_perioda = str(do_perioda)
    while copy_period != '' and copy_period[0] == '0':
        nyl_per += '0'
        copy_period = copy_period[1:]
    while copy_do_perioda != '' and copy_do_perioda[0] == '0':
        nyl_do_per += '0'
        copy_do_perioda = copy_do_perioda[1:]
    # print('nylper', nyl_per)
    # print('nyldoper', nyl_do_per)

if period == do_perioda == 0:
    drobnaia_chast = drobnaia_chast[:6]


def cifri_v_slova(celaia_chast, nyli): # переводит только целые числа
    # переделывает 432 в 400 30 2
    celaia_chast_cifri = []
    for i in range(len(celaia_chast)):
        if int(celaia_chast[i]) * int('1' + '0' * (len(celaia_chast) - i - 1)) == 0 and len(celaia_chast) > 1:
            continue
        else:
            celaia_chast_cifri += [int(celaia_chast[i]) * int('1' + '0' * (len(celaia_chast) - i - 1))]

    copy_cel = celaia_chast
    nyl = []
    if nyli:
        while copy_cel != '' and copy_cel[0] == '0':
            nyl += [0]
            copy_cel = copy_cel[1:]
    celaia_chast_cifri = nyl + celaia_chast_cifri
    # print('celaia_chast_cifri 1', celaia_chast_cifri)

    # проверка на числа от 11 до 19: 10 1 - 11
    for i in range(len(celaia_chast_cifri)-1, -1, -1):
        if celaia_chast_cifri[i] != '' and 10000 <= int(celaia_chast_cifri[i]) <= 90000 and i+1 < len(celaia_chast_cifri) and 1000 <= int(celaia_chast_cifri[i+1]) <= 9000:
            celaia_chast_cifri[i] = celaia_chast_cifri[i] + celaia_chast_cifri[i + 1]
            del celaia_chast_cifri[i + 1]
            # print(celaia_chast_cifri)
        if celaia_chast_cifri[i] != '' and 100000 <= int(celaia_chast_cifri[i]) <= 900000 and ((i+1 < len(celaia_chast_cifri) and 10000 <= int(celaia_chast_cifri[i+1]) <= 99000) or (i+1 < len(celaia_chast_cifri) and 1000 <= int(celaia_chast_cifri[i+1]) <= 9000)):
            celaia_chast_cifri[i] = celaia_chast_cifri[i] + celaia_chast_cifri[i + 1]
            del celaia_chast_cifri[i + 1]

    # print('celaia_chast_cifri 2', celaia_chast_cifri)

    flag = False
    for i in range(len(celaia_chast_cifri)-1, -1, -1):
        if 100000 <= celaia_chast_cifri[i] <= 999000:
            celaia_chast_cifri.insert(0, int(str(celaia_chast_cifri[i])[:3]))
            celaia_chast_cifri.insert(1, int('1' + str(celaia_chast_cifri[i+1])[3:]))
            del celaia_chast_cifri[2]
            flag = True
        if 10000 <= celaia_chast_cifri[i] <= 99000:
            celaia_chast_cifri.insert(0, int(str(celaia_chast_cifri[i])[:2]))
            celaia_chast_cifri.insert(1, int('1' + str(celaia_chast_cifri[i+1])[2:]))
            del celaia_chast_cifri[2]
            flag = True
    if flag:
        celaia_chast_cifri1 = []
        celaia_chast_cifri[0] = str(celaia_chast_cifri[0])
        for i in range(len(celaia_chast_cifri[0])):
            if int(celaia_chast_cifri[0][i]) * int('1' + '0' * (len(celaia_chast_cifri[0]) - i - 1)) == 0 and len(celaia_chast_cifri[0]) > 1:
                continue
            else:
                celaia_chast_cifri1 += [int(celaia_chast_cifri[0][i]) * int('1' + '0' * (len(celaia_chast_cifri[0]) - i - 1))]
        del celaia_chast_cifri[0]
        celaia_chast_cifri = celaia_chast_cifri1 + celaia_chast_cifri

    # print('celaia_chast_cifri 3', celaia_chast_cifri)

    for i in range(len(celaia_chast_cifri) - 1, -1, -1):
        if celaia_chast_cifri[i] == 10 and i + 1 < len(celaia_chast_cifri) and str(celaia_chast_cifri[i + 1]) in '0123456789':
            celaia_chast_cifri[i] = celaia_chast_cifri[i] + celaia_chast_cifri[i + 1]
            del celaia_chast_cifri[i + 1]
    # print('celaia_chast_cifri 4', celaia_chast_cifri)

    itog_bukvi = [] # подумать над универсальностью - 12_345_678 12 1000000 345 1000 12 плюс склонения
    #сделать список где будут все слова в любом склонении и потом проходом по строке изменять на правильные
    for i in range(len(celaia_chast_cifri)):
        for j in range(len(spisok_vsex_chisel)):
            if celaia_chast_cifri[i] == spisok_vsex_chisel[j][0]:
                if celaia_chast_cifri[i] == 1000 and i - 1 >= 0 and str(celaia_chast_cifri[i - 1])[0] in '0123456789':
                    if (str(celaia_chast_cifri[i - 1])) == '1':
                        itog_bukvi += [spisok_vsex_chisel[j+3][1]]
                        itog_bukvi[-2] = 'одна'
                    elif (str(celaia_chast_cifri[i - 1])) in '234':
                        itog_bukvi += [spisok_vsex_chisel[j + 2][1]]
                        if (str(celaia_chast_cifri[i - 1])) == '2':
                            itog_bukvi[-2] = 'две'
                    else:
                        itog_bukvi += [spisok_vsex_chisel[j+1][1]]
                else:
                    itog_bukvi += [spisok_vsex_chisel[j][1]]
                break
    # print('itog_bukvi', itog_bukvi)

    return ' '.join(itog_bukvi)


# ставит слова тысячная десятая и тд плюс нужные склонения делает
if drobnaia_chast != [] and period == do_perioda == 0:
    kvo_cifr_posle_zapatoi = len(drobnaia_chast)
    drob = float('0.' + '0'*(kvo_cifr_posle_zapatoi-1) + '1')
    # print(drob)
    drobnaia_chast_cifri_spisok = cifri_v_slova(drobnaia_chast, False).split()
    # print(drobnaia_chast_cifri_spisok)
    for i in range(len(spisok_vsex_chisel)):
        if drob == spisok_vsex_chisel[i][0]:
            if drobnaia_chast[-1] == '1':
                drobnaia_chast_cifri_spisok[-1] = 'одна'
                drobnaia_chast = ' '.join(drobnaia_chast_cifri_spisok) + ' ' + spisok_vsex_chisel[i+1][1]
            elif drobnaia_chast[-1] in '2':
                if drobnaia_chast[-1] == '2':
                    drobnaia_chast_cifri_spisok[-1] = 'две'
                    drobnaia_chast = ' '.join(drobnaia_chast_cifri_spisok) + ' ' + spisok_vsex_chisel[i][1]
                else:
                    drobnaia_chast = cifri_v_slova(drobnaia_chast, False) + ' ' + spisok_vsex_chisel[i + 2][1]
            else:
                drobnaia_chast = cifri_v_slova(drobnaia_chast, False) + ' ' + spisok_vsex_chisel[i][1]
            break
elif period != 0:
    if do_perioda == '':
        drobnaia_chast = cifri_v_slova(period, True) + ' в периоде'
    else:
        drobnaia_chast = cifri_v_slova(do_perioda, True) + ' и ' + cifri_v_slova(period, True) + ' в периоде'
# print('drobnaia_chast', drobnaia_chast)

# добавляе минус если надо
if drobnaia_chast == []:
    if minus:
        otvet = ('минус', cifri_v_slova(celaia_chast, False))
    else:
        otvet = (cifri_v_slova(celaia_chast, False))
    print((''.join(otvet)))
else:
    if minus:
        otvet = ('минус', cifri_v_slova(celaia_chast, False), 'и', drobnaia_chast)
    else:
        otvet = (cifri_v_slova(celaia_chast, False), 'и', drobnaia_chast)
    print((' '.join(otvet)))


# print(vse(primer))


# девяносто девять плюс сорок восемь      двадцать два умножить на двадцать два    двадцать два и сорок восемь сотых минус ноль и пять десятых   два и две миллионных плюс ноль
#сорок один и тридцать одна сотая разделить на семнадцать   пятьдесят семь умножить на сорок два      ноль плюс два и пятьсот тридцать восемь тысячных   восемь разделить на три
# одиннадцать разделить на девяносто   четыре разделить на тридцать три   два разделить на сто шестьдесят пять   сорок один разделить на триста тридцать три
# двадцать один разделить на двести два   один разделить на сто один  2.2-0.2    двадцать два разделить на сто восемьдесят
# девятьсот девять тысяч девятьсот девять разделить на один    два плюс три плюс четыре    двадцать два умножить на скобка открывается два плюс два скобка закрывается