import json
import io
import sys

# Функции для печати кириллицы
with io.open("result.json", encoding = 'utf-8') as read_file:
    data = json.load(read_file)

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# id чата с прогнозами участников
chat_id = 9753295252

# Список всех чатов
chats = data['chats']['list']

# Ищем чат по id
for chat in chats:
    if chat['id'] == chat_id:
        messages = chat['messages']

# Ищем id каждого из участников
ali_id = messages[45]['from_id']
kub_id = messages[1]['from_id']
lev_id = messages[2]['from_id']
tit_id = messages[7]['from_id']
ryk_id = messages[94]['from_id']

# Закрепляем имя за id
def decode_id(player_id):
    if player_id == lev_id:
        return 'Lev'
    elif player_id == tit_id:
        return 'Tit'
    elif player_id == ryk_id:
        return 'Ryk'
    elif player_id == ali_id:
        return 'Ali'
    elif player_id == kub_id:
        return 'Kub'

# Ищем последний прогноз от каждого из участников (прогноз начинается с $)
def get_preds(player_id):
    preds = []
    for mess in messages:
        if mess['text'] != '' and mess['text'][0] == '$' and mess['from_id'] == player_id:
            preds.append(mess['text'][1:])
    return preds[-1]

# Функция для объединения прогнозов от всех участников (одна строка - прогноз от одного участника на 10 игр)
def get_all_preds():
    return [get_preds(ali_id) + '\r\n', get_preds(kub_id) + '\r\n', get_preds(lev_id) + '\r\n', get_preds(tit_id) + '\r\n', get_preds(ryk_id) + '\r\n']

# Выводим прогнозы в отдельный файл
with open('input.txt', 'w') as input_:
    input_.writelines(get_all_preds())

input_.close()
