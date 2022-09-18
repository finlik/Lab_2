number = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
count = ['одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
teens = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
tens = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundred = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
thousand = ['тысяча', 'тысячи', 'тысяч']

a = int(input('Введите любую сумму от 1 до 999999: ')) #Ввод числа

if a > 999999 or a < 1:
    print ('Вы ввели неправильную сумму. Повторите попытку еще раз')
else:
    #Разбиваем число 4 разряда: тысячи, сотки, десятки, единицы
    a1 = a // 1000
    a2 = (a // 100) % 10
    a3 = (a // 10) % 10
    a4 = a % 10

    print('Ваше число:', end='')
    #Следующие 4 оператора if определяют в каких позициях стоят числа
    if a1 != 0: 
        b = a1
        #Смотрим количество цифр в тысячном разряде, чтобы правильно определить название числа
        if len(str(b)) == 3:
            
            k1 = b // 100
            k2 = (b // 10) % 10
            k3 = b % 10
        
            if (1 <= k1 <= 9) and (k2 == 0) and (k3 == 0):
                call1 = hundred[k1-1] + ' ' + thousand[2] #Вызов из массивов нужное название

            elif (1 <= k1 <= 9) and (k2 != 0) and (k3 == 0):
                call1 = hundred[k1-1] + ' ' + tens[k2-1] + ' ' + thousand[2]

            elif (k1 == 1) and (k2 == 0) and (k3 == 1):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[0]
            elif (2 <= k1 <= 4) and (k2 == 0) and (2 <= k3 <= 4):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[1]
            elif (5 <= k1 <= 9) and (k2 == 0) and (5 <= k3 <= 9):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[2]
            
            elif (2 <= k1 <= 4) and (k2 == 0) and (k3 == 1):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[0]
            elif (2 <= k1 <= 4) and (k2 == 0) and (2 <= k3 <= 4):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[1]
            elif (2 <= k1 <= 4) and (k2 == 0) and (5 <= k3 <= 9):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[2]
            
            elif (5 <= k1 <= 9) and (k2 == 0) and (k3 == 1):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[0]
            elif (5 <= k1 <= 9) and (k2 == 0) and (2 <= k3 <= 4):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[1]
            elif (5 <= k1 <= 9) and (k2 == 0) and (5 <= k3 <= 9):
                call1 = hundred[k1-1] + ' ' + count[k3-1] + ' ' + thousand[2]


            elif (k3 == 1) and (k2 != 0) and (k3 != 0):
                call1 = hundred[k1-1] + ' ' + tens[k2-1] + ' ' + count[k3-1] + ' ' + thousand[0]
            elif (2 <= k3 <= 4) and (k2 != 0) and (k3 != 0): 
                call1 = hundred[k1-1] + ' ' + tens[k2-1] + ' ' + count[k3-1] + ' ' + thousand[1]
            else:
                 call1 = hundred[k1-1] + ' ' + tens[k2-1] + ' ' + count[k3-1] + ' ' + thousand[2]

        elif len(str(b)) == 2:

            k1 = b // 10
            k2 = b % 10
            
            if (1 <= k1 <= 9) and (k2 == 1):
                call1 = tens[k1-1] + ' ' + count[k2-1] + ' ' + thousand[0]
            elif (1 <= k1 <= 9) and (2 <= k2 <= 4):
                call1 = tens[k1-1] + ' ' + count[k2-1] + ' ' + thousand[1]
            elif (1 <= k1 <= 9) and (5 <= k2 <= 9):
                call1 = tens[k1-1] + ' ' + count[k2-1] + ' ' + thousand[2]        
            else:
                call1 = q1 + ' ' + count[k2-1] + ' ' + thousand[2]
            
        elif len(str(b)) == 1:      
            if b == 1:
                call1 = count[b-1] + ' ' + thousand[0]
            elif (2 <= b <= 4):
                call1 = count[b-1] + ' ' + thousand[1]
            else:
                call1 = count[b-1] + ' ' + thousand[2]
    else:
        call1 = ''

    if a2 != 0:
        b = a2
        call2 = hundred[b-1]
    else:
        call2 = ''

    if a3 == 0:
        b = a4
        if a4 == 0:
            call5 = 'рублей'
            print (call1, call2, call5)
        else:
            call3 = number[b-1]
            if 5 <= b <= 9:
                call5 = 'рублей'
            elif 2 <= b <= 4:
                call5 = 'рубля'
            else:
                call5 = 'рубль'
            print(call1, call2, call3, call5)
            
    elif a3 == 1:
        b = a4
        call3 = teens[b-1]
        print (call1, call2, call3, 'рублей')
        
    else:
        b = a3
        call3 = tens[b-1]
        b = a4
        call4 = number[b-1]
        if 5 <= b <= 9:
            call5 = 'рублей'
        elif 2 <= b <= 4:
            call5 = 'рубля'
        else:
            call5 = 'рубль'
        print (call1, call2, call3, call4, call5)
        


   
        
