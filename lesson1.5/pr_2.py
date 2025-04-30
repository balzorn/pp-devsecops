subjects = [
    "математика",
    "изо",
    "русский язык",
    "биология",
    "химия",
    "физика"
]

def print_subj(sub):
    indx = 0
    for s in sub:
        print(f'{indx + 1}. {s}')
        indx += 1

while True:
    print_subj(subjects)
    s = subjects.pop(int(input("Предмет под каким номером удалить? ")) - 1)
    print(f'Предмет "{s}" удален!')