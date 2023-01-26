with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def transliterate_lat(text):
    text = text.replace('a', 'а')
    text = text.replace('e', 'е')
    text = text.replace('o', 'о')
    text = text.replace('c', 'с')
    with open('text_uniq.txt', 'w', encoding='utf-8') as f:
        f.write(text)


def transliterate_rus(text):
    text = text.replace('а', 'a')
    text = text.replace('е', 'e')
    text = text.replace('о', 'o')
    text = text.replace('с', 'c')
    with open('text_uniq.txt', 'w', encoding='utf-8') as f:
        f.write(text)

with open('text_uniq.txt', 'w', encoding='utf-8') as f:
    f.write('')


print('Выберите символы для замены: 1 - русские, 2 - английсие')
choice = input()
if choice == '1':
    transliterate_lat(text)
elif choice == '2':
    transliterate_rus(text)