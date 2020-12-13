input_ = open('input_lch.txt', 'r')

# Read predictions from inputs
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
def oneGroupCalc(group, index):
    score = 0
    real_group = real[index][1:]
    real_group = '99' + real_group + '9'
    group = '99' + group + '9'
    for i in range(2,5):
        if group[i] == real_group[i]:
            score+=3
        elif group[i] == real_group[i-1] or group[i] == real_group[i+1]:
            score+=2
        elif group[i] == real_group[i-2] or group[i] == real_group[i+2]:
            score+=1
    return score

#print(oneGroupCalc('A1243', 0))

def calcResults(player):
    score = 0
    for i,group in enumerate(player):
        score += oneGroupCalc(group, i)
    return score


print('Kub', calcResults(kub))
print('Ali', calcResults(ali))
print('Tit', calcResults(tit))
print('Ryk', calcResults(ryk))
print('Lev', calcResults(lev))