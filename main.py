# edinici = [0, 'ноль'], [1, "один"], [2, 'два'], [3, 'три'], [4, 'четыре'], [5, 'пять'], [6, 'шесть'], [7, 'семь'], [8, 'восемь'], [9, 'девять']
# desatki = ([10, 'десять'], [11, 'одиннадцать'], [12, 'двенадцать'], [13, 'тринадцать'], [14, 'четырнадцать'], [15, 'пятнадцать'], [16, 'шестнадцать'], [17, 'семнадцать'], [18, 'восемндацать'],[19, 'девятнадцать'],
#            [20, 'двадцать'], [30, 'тридцать'], [40, 'сорок'], [50, 'пятьдесят'],[60, 'шестьдесят'], [70, 'семьдесят'], [80, 'восемьдесят'], [90, 'девяносто'])
# sotni = [100, 'сто'], [200, 'двести'], [300, 'триста'], [400, 'четыреста'], [500, 'пятьсот'], [600, 'шестьсот'], [700, 'семьсот'], [800, 'восемьсот'], [900, 'девятьсот']
# tisyachi = [1000, 'одна тысяча'], [2000, 'две тысячи'], [3000, 'три тысячи'], [4000, 'четыре тысячи'], [5000, 'пять тысяч'], [6000, 'шесть тысяч'], [7000, 'семь тысяч'], [8000, 'восемь тысяч'], [9000, 'девять тысяч']

spisok_vsex_chisel = ([0, 'ноль'], [1, "один"], [2, 'два'], [3, 'три'], [4, 'четыре'], [5, 'пять'], [6, 'шесть'], [7, 'семь'], [8, 'восемь'], [9, 'девять'],
                      [10, 'десять'], [11, 'одиннадцать'], [12, 'двенадцать'], [13, 'тринадцать'], [14, 'четырнадцать'], [15, 'пятнадцать'], [16, 'шестнадцать'], [17, 'семнадцать'], [18, 'восемнадцать'],[19, 'девятнадцать'],
                      [20, 'двадцать'], [30, 'тридцать'], [40, 'сорок'], [50, 'пятьдесят'],[60, 'шестьдесят'], [70, 'семьдесят'], [80, 'восемьдесят'], [90, 'девяносто'],
                      [100, 'сто'], [200, 'двести'], [300, 'триста'], [400, 'четыреста'], [500, 'пятьсот'], [600, 'шестьсот'], [700, 'семьсот'], [800, 'восемьсот'], [900, 'девятьсот'],
                      [1000, 'одна тысяча'], [2000, 'две тысячи'], [3000, 'три тысячи'], [4000, 'четыре тысячи'], [5000, 'пять тысяч'], [6000, 'шесть тысяч'], [7000, 'семь тысяч'], [8000, 'восемь тысяч'], [9000, 'девять тысяч'],
                      ['+', 'плюс'], ['-', 'минус'], ['*', 'умножить'], ['/', 'разделить'], [1, 'одна'], [2, 'две'], ['и', 'и'],
                      [0.1, 'десятых'], [0.1, 'десятые'], [0.1, 'десятая'], [0.01, 'сотых'], [0.01, 'сотая'], [0.01, 'сотые'], [0.001, 'тысячных'], [0.001, 'тысячная'], [0.001, 'тысячные'])

#operacii = ['+', 'плюс'], ['-', 'минус'], ['*', 'умножить на']


primer = input()

def slova_v_cifri(primer):
    primer_chisla = []
    primer = primer.split()
    for i in primer: # считывает слова и переходит на цифры пятьсот - 500
        for j in spisok_vsex_chisel:
            if i == j[1]:
                primer_chisla += [j[0]]

    primer_chisla_vmeste = []
    kazhdoe_chislo = 0
    c = 0
    for i in range(len(primer_chisla)): # каждое слово перерабатывает в число или знак 22 = 20 2
        #print(primer_chisla, primer_chisla_vmeste, kazhdoe_chislo)

        if i+1 < len(primer_chisla) and str(primer_chisla[i]) not in '*-+и/':
            kazhdoe_chislo += primer_chisla[i]
        elif i+1 < len(primer_chisla) and (str(primer_chisla[i]) in '*-+и/'):
            primer_chisla_vmeste += [kazhdoe_chislo]
            primer_chisla_vmeste += [primer_chisla[i]]
            kazhdoe_chislo = 0
        elif i+1 == len(primer_chisla):
            kazhdoe_chislo += primer_chisla[i]
            primer_chisla_vmeste += [kazhdoe_chislo]

    spisok_chisel = primer_chisla_vmeste
    for i in range(len(spisok_chisel)): # перерабатывает дробные числа 31.01 в 31*0.01 в 0.31
        if '.' in str(spisok_chisel[i]):
            spisok_chisel[i] = str(spisok_chisel[i]).replace('.', '*0.')
            spisok_chisel[i] = eval(str(spisok_chisel[i]))

    spisok_chisel1 = []
    for i in range(len(spisok_chisel)): # соединяет целые и дробные числа в списке 22 0.1 в 22.1
        if i+1 < len(spisok_chisel) and spisok_chisel[i+1] == 'и':
            spisok_chisel1 += [spisok_chisel[i] + spisok_chisel[i+2]]
            spisok_chisel[i] = ''
            spisok_chisel[i + 1] = ''
            spisok_chisel[i + 2] = ''
        else:
            spisok_chisel1 += [spisok_chisel[i]]

    spisok_chisel2 = []
    for i in range(len(spisok_chisel1)): # убирает пустые строки
        if spisok_chisel1[i] != '':
            spisok_chisel2 += [spisok_chisel1[i]]
    #print(spisok_chisel2)

    cifri = ''
    for i in spisok_chisel2: # переделывает в сплошную строку для eval
        cifri += str(i)
    itog_otvet_cifri = round(eval(cifri), 3)

    return itog_otvet_cifri

print(slova_v_cifri(primer))

itog_otvet_cifri = str(slova_v_cifri(primer))
if itog_otvet_cifri.find('.') != -1: # разбивает число на целую и дробную часть
    celaia_chast = itog_otvet_cifri[:itog_otvet_cifri.find('.')]
    drobnaia_chast = itog_otvet_cifri[itog_otvet_cifri.find('.') + 1:]
else:
    celaia_chast = itog_otvet_cifri
    drobnaia_chast = []

celaia_chast_cifri = []
for i in range(len(celaia_chast)): # переделывает 432 в 400 30 2
    celaia_chast_cifri += [int(celaia_chast[i]) * int('1' + '0' * (len(celaia_chast) - i - 1))]
for i in range(len(celaia_chast_cifri)):
    if celaia_chast_cifri[i] == 10:
        celaia_chast_cifri[i] = celaia_chast_cifri[i] + celaia_chast_cifri[i + 1]
        celaia_chast_cifri[i + 1] = ''

print(celaia_chast_cifri)
print(drobnaia_chast)
drobnaia_chast_cifri = []
if drobnaia_chast != '0' and drobnaia_chast != []: # переделывает 0.432 в 400 30 2 0.001
    for i in range(len(drobnaia_chast)):
        drobnaia_chast_cifri += [int(drobnaia_chast[i]) * int('1' + '0' * (len(drobnaia_chast) - i - 1))]
    drobnaia_chast_cifri += [float('0.' + '0' * (len(drobnaia_chast) - 1) + '1')]
    print(drobnaia_chast_cifri, '1')
    for i in range(len(drobnaia_chast_cifri)):
        if drobnaia_chast_cifri[i] == 10:
            drobnaia_chast_cifri[i] = drobnaia_chast_cifri[i] + drobnaia_chast_cifri[i+1]
            drobnaia_chast_cifri[i+1] = ''

    itog_cifri = celaia_chast_cifri + ['и'] + drobnaia_chast_cifri
else:
    itog_cifri = celaia_chast_cifri
print(itog_cifri)

itog_bukvi = []
for i in range(len(itog_cifri)): # переводит из цифр в буквы
    for j in range(len(spisok_vsex_chisel)):
        if itog_cifri[i] == spisok_vsex_chisel[j][0]:
            itog_bukvi += [spisok_vsex_chisel[j][1]]
            break

print(*(itog_bukvi))



#2.43 - 2 и 40 3 0.01


# девяносто девять плюс сорок восемь      двадцать два умножить на двадцать два    двадцать два и сорок восемь сотых минус ноль и пять десятых
#сорок один и тридцать одна сотая разделить на семнадцать   пятьдесят семь умножить на сорок два      ноль плюс два и пятьсот тридцать восемь тысячных