print('Hello world')

print('Задача 9. Аннуитетный платёж')

def annual_payment(credit):
    summ_percent = credit * percent
    body_credit = annuity - summ_percent
    print('Остаток долга на начало периода:', credit)
    print('Выплачено процентов:', summ_percent)
    print('Выплачено тела кредита:', body_credit)

    return body_credit


credit = float(input('Введите сумму кредита: '))
time = int(input('На сколько лет выдан? '))
year = int(input('Через сколько лет будем менять условия кредита? '))
percent = float(input('Сколько процентов годовых? '))

percent /= 100
annuity = round((percent * (1 + percent) ** time) / ((1 + percent) ** time - 1) * credit, 2)
body_credit = 0

for i in range(1, year + 1):
    print('\nПериод:', i)
    credit -= body_credit
    body_credit = annual_payment(credit)

print('\nОстаток долга:', credit - body_credit)
print('\n=========================')

new_time = int(input('На сколько лет продляется договор?: '))
percent = float(input('Увеличение ставки до: '))

time = time - year + new_time
percent /= 100
credit -= body_credit
annuity = round((percent * (1 + percent) ** time) / ((1 + percent) ** time - 1) * credit, 2)
body_credit = 0

for i in range(1, time + 1):
    print('\nПериод:', i)
    credit -= body_credit
    body_credit = annual_payment(credit)

print('\nОстаток долга:', credit - body_credit)
print('\n=========================')