import json
import io
import sys

# functions for printing union code simbols
with io.open('result.json', encoding = 'utf-8') as read_file:
    data = json.load(read_file)

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# Could be changed in the future
chat_id = 9753295252

# List of chats
chats = data['chats']['list']

# Getting TurPro chat
for chat in chats:
    if chat['id'] == chat_id:
        messages = chat['messages']

# Getting players id
ali_id = messages[45]['from_id']
kub_id = messages[1]['from_id']
lev_id = messages[2]['from_id']
tit_id = messages[7]['from_id']
ryk_id = messages[94]['from_id']

# Getting name for id
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

def get_preds(player_id):
    preds = []
    for mess in messages:
        if mess['text'] != '' and mess['text'][0] == '$' and mess['text'][1] == '$' and mess['from_id'] == player_id:
            preds.append(mess['text'][3:])
    return preds[-1]

# Getting all the prediction and concatenatind them
def get_all_preds():
    return [get_preds(ali_id) + '\r\n', get_preds(kub_id) + '\r\n', get_preds(lev_id) + '\r\n', get_preds(tit_id) + '\r\n', get_preds(ryk_id) + '\r\n']

# Write in the text file
with open('input_lch.txt', 'w') as input_:
    input_.writelines(get_all_preds())

input_.close()