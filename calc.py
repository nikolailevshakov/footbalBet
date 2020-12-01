from datetime import date

today = date.today()

input_ = open('input.txt', 'r')

# Считываем прогнозы с текстового файла
ali = input_.readline().rstrip().split(" ")
emp = input_.readline().rstrip().split(" ")
kub = input_.readline().rstrip().split(" ")
emp = input_.readline().rstrip().split(" ")
lev = input_.readline().rstrip().split(" ")
emp = input_.readline().rstrip().split(" ")
tit = input_.readline().rstrip().split(" ")
emp = input_.readline().rstrip().split(" ")
ryk = input_.readline().rstrip().split(" ")
emp = input_.readline().rstrip().split(" ")
real = input_.readline().rstrip().split(" ")

input_.close()
# Функция для подсчета баллов
def calculator(predict, amount=10, real=real):
    score = 0
    three = 0
    two = 0
    one = 0
    for i in range(0, amount):
        if predict[i] == real[i]:
            score += 3
            three += 1
        elif predict[i][0] != '0' and real[i][0] != '0':
            if (int(predict[i][1]) - int(predict[i][0])) == (int(real[i][1]) - int(real[i][0])):
                score += 2
                two += 1
            elif (int(predict[i][1]) - int(predict[i][0]))*(int(real[i][1]) - int(real[i][0]))>0:
                score += 1
                one += 1
        elif predict[i][0] != '0' and real[i][0] == '0':
            if (int(predict[i][1]) - int(predict[i][0])) == (int(real[i])):
                score += 2
                two += 1
            elif (int(predict[i][1]) - int(predict[i][0]))>0:
                score += 1
                one += 1
        elif predict[i][0] == '0' and real[i][0] != '0':
            if (int(predict[i])) == (int(real[i][1]) - int(real[i][0])):
                score += 2
                two += 1
            elif predict[i] == '00':
                score += 0
            elif (int(real[i][1]) - int(real[i][0]))>0:
                score += 1
                one += 1
        elif predict[i][0] == '0' and real[i][0] == '0':
            if int(predict[i]) == 0 or int(real[i]) == 0:
                score += 0
            else: 
                score += 1
                one += 1
    print(score)
    return score, three, two, one


# Выводим баллы для каждого игрока в отдельный файл
def output_stats(res, name):
    stats = str(today) + '  ' + str(res[0]) + '  ' + str(res[1]) + '  ' + str(res[2]) + '  ' + str(res[3]) 
    doc = open('{}.txt'.format(name), 'a')
    doc.write('\r\n' + stats)

# Считаем баллы для всех участников
def calc_all(amount):
    print('-------------------------------')
    print('lev')
    calculator(lev, amount)
    print('-------------------------------')
    print('tit')
    calculator(tit, amount)
    print('-------------------------------')
    print('ryk')
    calculator(ryk, amount)
    print('-------------------------------')
    print('ali')
    calculator(ali, amount)
    print('-------------------------------')
    print('kub')
    calculator(kub, amount)
    print('-------------------------------')


# Функция для подсчета и вывод результатов в отдельный текстовой файл для каждого из участников
def calc_all_stats(amount=10):
    print('-------------------------------')
    print('lev') 
    output_stats(calculator(lev, amount), 'lev')
    print('Tit')
    output_stats(calculator(tit, amount), 'tit')
    print('Ryk')
    output_stats(calculator(ryk, amount), 'ryk')
    print('Ali')
    output_stats(calculator(ali, amount), 'ali')
    print('Kub')
    output_stats(calculator(kub, amount), 'kub')
    print('-------------------------------')

# Запускаем рассчет на 10 игр
calc_all_stats(10)
