from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    mau_ngau_nhien=choice(shapes)
    item_ngau_nhien=choice(shapes)
    return [
            mau_ngau_nhien['color'],
            item_ngau_nhien['text'],
            randint(0,1),

            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        if text == 'BLUE':
            if (20 <= x <= 120 and 60 <= y <= 160 ) == True:
                return True
            else:
                return False
        elif text == 'RED':
            if  (140<=x<=240 and 60<=y<=160) == True:
                return True
            else:
                return False
        elif text == 'YELLOW':
            if  (20<=x<=120 and 180<=y<=280) == True:
                return True
            else:
                return False
                     
        elif text == 'GREEN':
            if  (20 <= x <= 120 and 180 <= y <= 280) == True:
                return True
            else:
                return False
    elif quiz_type == 1:
        if text == '#3F51B5':
            if (20 <= x <= 120 and 60 <= y <= 160 ) == True:
                return True
            else:
                return False
        elif text == '#C62828':
            if  (140<=x<=240 and 60<=y<=160) == True:
                return True
            else:
                return False
        elif text == '#FFD600':
            if  (20<=x<=120 and 180<=y<=280) == True:
                return True
            else:
                return False
                     
        elif text == '#4CAF50':
            if  (20 <= x <= 120 and 180 <= y <= 280) == True:
                return True
            else:
                return False
