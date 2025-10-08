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
                      [1000, 'одна тысяча'], [2000, 'две тысячи'], [3000, 'три тысячи'], [4000, 'четыре тысячи'], [5000, 'пять тысяч'], [6000, 'шесть тысяч'], [7000, 'семь тысяч'], [8000, 'восемь тысяч'], [9000, 'девять тысяч'],
                      [10_000, 'десять тысяч'], [20_000, 'двадцать тысяч'], [30_000, 'тридцать тысяч'],    [40_000, 'сорок тысяч'], [50_000, 'пятьдесят тысяч'], [60_000, 'шестьдесят тысяч'],    [70_000, 'семьдесят тысяч'], [80_000, 'восемьдесят тысяч'], [90_000, 'девяносто тысяч'],
                      [100_000, 'сто тысяч'], [200_000, 'двести тысяч'], [300_000, 'триста тысяч'], [400_000, 'четыреста тысяч'], [500_000, 'пятьсот тысяч'], [600_000, 'шестьсот тысяч'],[700_000, 'семьсот тысяч'], [800_000, 'восемьсот тысяч'], [900_000, 'девятьсот тысяч'],
                      [1_000_000, 'один миллион'], [2_000_000, 'два миллиона'], [3_000_000, 'три миллиона'],[4_000_000, 'четыре миллиона'], [5_000_000, 'пять миллионов'], [6_000_000, 'шесть миллионов'], [7_000_000, 'семь миллионов'], [8_000_000, 'восемь миллионов'], [9_000_000, 'девять миллионов'],
                      ['+', 'плюс'], ['-', 'минус'], ['*', 'умножить'], ['/', 'разделить'], ['и', 'и'], ['%', 'остаток'], ['в периоде', 'в периоде'],
                      [0.1, 'десятых'], [0.1, 'десятая'], [0.1, 'десятые'], [0.01, 'сотых'], [0.01, 'сотая'], [0.01, 'сотые'], [0.001, 'тысячных'], [0.001, 'тысячная'], [0.001, 'тысячные'], [0.0001, 'десятитысячных'],
                      [0.0001, 'десятитысячная'], [0.0001, 'десятитысячные'], [0.00001, 'стотысячных'], [0.00001, 'стотысячная'], [0.00001, 'стотысячные'], [0.000001, 'миллионных'], [0.000001, 'миллионная'], [0.000001, 'миллионные'])


primer = input()

def slova_v_cifri(primer):
    # переходит на цифры: двадцать два - 20 2
    primer_chisla_grubie_drobi_razdelno = []
    primer = primer.split()
    for i in primer:
        for j in spisok_vsex_chisel:
            if i == j[1]:
                primer_chisla_grubie_drobi_razdelno.append(j[0])
    print('primer_chisla_grubie_drobi_razdelno', primer_chisla_grubie_drobi_razdelno)

    # складывает цифры, стоящие рядом, знаки не трогает: 500 40 3 0.001= 543.001
    primer_chisla_grubie_drobi_vmeste = []
    kazhdoe_chislo = 0
    c = 0
    for i in range(len(primer_chisla_grubie_drobi_razdelno)):
        #print(primer_chisla_grubie_drobi_razdelno, primer_chisla_grubie_drobi_vmeste, kazhdoe_chislo)

        if i+1 < len(primer_chisla_grubie_drobi_razdelno) and str(primer_chisla_grubie_drobi_razdelno[i]) not in '*-+и/%': # если это число и оно не последнее
            kazhdoe_chislo += primer_chisla_grubie_drobi_razdelno[i]
        elif i+1 < len(primer_chisla_grubie_drobi_razdelno) and (str(primer_chisla_grubie_drobi_razdelno[i]) in '*-+и/%'): # если это знак и это не последнее место в списке
            primer_chisla_grubie_drobi_vmeste += [kazhdoe_chislo]
            primer_chisla_grubie_drobi_vmeste += [primer_chisla_grubie_drobi_razdelno[i]]
            kazhdoe_chislo = 0
        elif i+1 == len(primer_chisla_grubie_drobi_razdelno): # если это последнее число
            kazhdoe_chislo += primer_chisla_grubie_drobi_razdelno[i]
            primer_chisla_grubie_drobi_vmeste += [kazhdoe_chislo]
    print('primer_chisla_grubie_drobi_vmeste', primer_chisla_grubie_drobi_vmeste)

    # перерабатывает дробные числа 31.01 в 31*0.01 в 0.31
    primer_chisla_normalnie_drobi = primer_chisla_grubie_drobi_vmeste
    for i in range(len(primer_chisla_normalnie_drobi)):
        if '.' in str(primer_chisla_normalnie_drobi[i]):
            primer_chisla_normalnie_drobi[i] = str(primer_chisla_normalnie_drobi[i]).replace('.', '*0.')
            primer_chisla_normalnie_drobi[i] = eval(str(primer_chisla_normalnie_drobi[i]))
    print('primer_chisla_normalnie_drobi', primer_chisla_normalnie_drobi)

    # соединяет целые и дробные числа в списке 22 0.1 в 22.1
    primer_chisla_pravilnie_drobi_ps = []
    for i in range(len(primer_chisla_normalnie_drobi)):
        if i+1 < len(primer_chisla_normalnie_drobi) and primer_chisla_normalnie_drobi[i+1] == 'и':
            primer_chisla_pravilnie_drobi_ps += [primer_chisla_normalnie_drobi[i] + primer_chisla_normalnie_drobi[i+2]]
            primer_chisla_normalnie_drobi[i] = ''
            primer_chisla_normalnie_drobi[i + 1] = ''
            primer_chisla_normalnie_drobi[i + 2] = ''
        else:
            primer_chisla_pravilnie_drobi_ps += [primer_chisla_normalnie_drobi[i]]
    print('primer_chisla_pravilnie_drobi_ps', primer_chisla_pravilnie_drobi_ps)

    # убирает пустые строки
    primer_chisla_pravilnie_drobi = []
    for i in range(len(primer_chisla_pravilnie_drobi_ps)):
        if primer_chisla_pravilnie_drobi_ps[i] != '':
            primer_chisla_pravilnie_drobi += [primer_chisla_pravilnie_drobi_ps[i]]
    print('primer_chisla_pravilnie_drobi', primer_chisla_pravilnie_drobi)

    # переделывает в сплошную строку для eval
    cifri = ''
    for i in primer_chisla_pravilnie_drobi:
        cifri += str(i)
    itog_otvet_cifri = round(eval(cifri), 11)
    print('itog_otvet_cifri', itog_otvet_cifri)

    return itog_otvet_cifri


# разбивает число на целую и дробную часть
itog_otvet_cifri = str(slova_v_cifri(primer))
if itog_otvet_cifri.find('.') != -1:
    celaia_chast = itog_otvet_cifri[:itog_otvet_cifri.find('.')]
    drobnaia_chast = itog_otvet_cifri[itog_otvet_cifri.find('.') + 1:]
else:
    celaia_chast = itog_otvet_cifri
    drobnaia_chast = []

period = 0
if len(drobnaia_chast) == 11:
    for j in range(2):
        if all(drobnaia_chast[i+j] == drobnaia_chast[i+4+j] and drobnaia_chast[i+1+j] == drobnaia_chast[i+5+j] and drobnaia_chast[i+2+j] == drobnaia_chast[i+6+j] and drobnaia_chast[i+3+j] == drobnaia_chast[i+7+j] for i in range(2-j)):
            period = 4, j
            break
    for j in range(3):
        if all(drobnaia_chast[i+j] == drobnaia_chast[i+j+3] and drobnaia_chast[i+j+1] == drobnaia_chast[i+j+4] and drobnaia_chast[i+j+2] == drobnaia_chast[i+j+5] for i in range(6-j)):
            period = 3, j
            break
    for j in range(4):
        if all(drobnaia_chast[i+j] == drobnaia_chast[i+j+2] and drobnaia_chast[i+j+1] == drobnaia_chast[i+j+3] for i in range(8-j)):
            period = 2, j
            break
    for j in range(5):
        if all(drobnaia_chast[i+j] == drobnaia_chast[i+j+1] for i in range(9-j)):
            period = 1, j
            break
print('period', period)

if len(drobnaia_chast) > 6:
    drobnaia_chast = drobnaia_chast[:6]
if period != 0:
    drobnaia_chast = drobnaia_chast[:period[1]] + drobnaia_chast[period[1]:period[0]+1] # +1
print('drobnaia_chast', drobnaia_chast)

# переделывает 432 в 400 30 2
celaia_chast_cifri = []
for i in range(len(celaia_chast)):
    if int(celaia_chast[i]) * int('1' + '0' * (len(celaia_chast) - i - 1)) == 0 and len(celaia_chast) > 1:
        continue
    else:
        celaia_chast_cifri += [int(celaia_chast[i]) * int('1' + '0' * (len(celaia_chast) - i - 1))]

# проверка на числа от 11 до 19: 10 1 - 11
for i in range(len(celaia_chast_cifri)):
    if celaia_chast_cifri[i] == 10 and i + 1 < len(celaia_chast_cifri) and celaia_chast_cifri[i] in '0123456789':
        celaia_chast_cifri[i] = celaia_chast_cifri[i] + celaia_chast_cifri[i + 1]
        celaia_chast_cifri[i + 1] = ''
print('celaia_chast_cifri', celaia_chast_cifri)

# переделывает 0.432 в 400 30 2 0.001
drobnaia_chast_cifri = []
if drobnaia_chast != '0' and drobnaia_chast != []:
    if period != 0:
        if drobnaia_chast[:period[1]] != '':
            drobnaia_chast_cifri += [drobnaia_chast[:period[1]]]
        if drobnaia_chast_cifri != [] and period[1] != 0: # попрбовать где период сразу
            drobnaia_chast_cifri += 'и'
        drobnaia_chast_cifri += [drobnaia_chast[period[1]:period[0]+1]]

    else:
        for i in range(len(drobnaia_chast)):
            if int(drobnaia_chast[i]) != 0:
                drobnaia_chast_cifri += [int(drobnaia_chast[i]) * int('1' + '0' * (len(drobnaia_chast) - i - 1))]
        drobnaia_chast_cifri += [float('0.' + '0' * (len(drobnaia_chast) - 1) + '1')]

    for i in range(len(drobnaia_chast_cifri)):
        if drobnaia_chast_cifri[i] == 10:
            drobnaia_chast_cifri[i] = drobnaia_chast_cifri[i] + drobnaia_chast_cifri[i+1]
            drobnaia_chast_cifri[i + 1] = ''
    print('drobnaia_chast_cifri', drobnaia_chast_cifri)

    dl = '0'
    if period != 0:
        if period[1] > 0:
            for i in range(len(drobnaia_chast_cifri)):
                if drobnaia_chast_cifri[i][0] in '0987654321':
                    if drobnaia_chast_cifri[i][0] == '0' and i + 1 == len(drobnaia_chast_cifri): # не учитывает период нач с двух и более нулей
                        drobnaia_chast_cifri += '0'
                        drobnaia_chast_cifri += [drobnaia_chast_cifri[i][1:]]
                        dl = drobnaia_chast_cifri[i][1:]
                        del drobnaia_chast_cifri[-3]

            dl = drobnaia_chast_cifri[-1]
            dl1 = []
            if dl not in ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19']:
                for i in range(len(dl)):
                    if int(dl[i]) * int('1' + '0' * (len(dl) - i - 1)) == 0 and len(dl) > 1:
                        continue
                    else:
                        dl1 += [int(dl[i]) * int('1' + '0' * (len(dl) - i - 1))]
            else:
                dl1 = dl
            print('1', dl1)
            del drobnaia_chast_cifri[-1]
            drobnaia_chast_cifri += [str(i) for i in dl1]
        else:
            dl1 = []
            for i in range(len(drobnaia_chast_cifri[0])):
                if int(drobnaia_chast_cifri[0][i]) * int('1' + '0' * (len(drobnaia_chast_cifri[0]) - i - 1)) == 0 and len(drobnaia_chast_cifri[0]) > 1:
                    continue
                else:
                    dl1 += [int(drobnaia_chast_cifri[0][i]) * int('1' + '0' * (len(drobnaia_chast_cifri[0]) - i - 1))]
            if drobnaia_chast_cifri[0] in ['10', '11', '12' , '13', '14', '15', '16', '17', '18', '19']:
                print('2', drobnaia_chast_cifri)
            else:
                del drobnaia_chast_cifri[-1]
                print('2', dl1)
                drobnaia_chast_cifri += [str(i) for i in dl1]
        drobnaia_chast_cifri += ['в периоде']

        for i in range(len(drobnaia_chast_cifri)):
            if drobnaia_chast_cifri[i][0] in '0987654321':
                drobnaia_chast_cifri[i] = int(drobnaia_chast_cifri[i])
    print('drobnaia_chast_cifri', drobnaia_chast_cifri)
    itog_cifri = celaia_chast_cifri + ['и'] + drobnaia_chast_cifri
else:
    itog_cifri = celaia_chast_cifri
print('itog_cifri', itog_cifri)


# переводит из цифр в буквы
itog_bukvi = [] # подумать над универсальностью - 12_345_678 12 1000000 345 1000 12 плюс склонения
#сделать список где будут все слова в любом склонении и потом проходом по строке изменять на правильные
for i in range(len(itog_cifri)):
    for j in range(len(spisok_vsex_chisel)):
        if itog_cifri[i] == spisok_vsex_chisel[j][0]:
            itog_bukvi += [spisok_vsex_chisel[j][1]]
            break

# если слово тысяч встречается больше одного раза, то оставляем только последнее
c_tisach = itog_bukvi.count('тысяч')
for i in range(len(itog_bukvi)):
    if 'тысяч' in itog_bukvi[i]:
        c_tisach += 1
if c_tisach > 1:
    for i in range(c_tisach-1):
        for j in range(len(itog_bukvi)):
            if 'тысяч' in itog_bukvi[j]:
                itog_bukvi[j] = itog_bukvi[j][:-6]
                break

print(*(itog_bukvi))






# девяносто девять плюс сорок восемь      двадцать два умножить на двадцать два    двадцать два и сорок восемь сотых минус ноль и пять десятых   два и две миллионных плюс ноль
#сорок один и тридцать одна сотая разделить на семнадцать   пятьдесят семь умножить на сорок два      ноль плюс два и пятьсот тридцать восемь тысячных   восемь разделить на три
# одиннадцать разделить на девяносто   четыре разделить на тридцать три   два разделить на сто шестьдесят пять   сорок один разделить на триста тридцать три
# двадцать один разделить на двести два   один разделить на сто один  2.2-0.2    двадцать два разделить на сто восемьдесят