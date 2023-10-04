
print('Hi,guys!Are you ready to do this game viktorina???')
print('You need to answer the questions and have fun!')

omg = ['в каком году построили эйфиливую башню?',
       ' каком году началсь война России с Франций?',
       'назовите город-государство?',
       'кто король поп музыки?',
       'кто король рок музыки?',
       'сколько ушло лет на строительство Исаакиевского собора?',
       'кто такой Чарли Чаплин?',
       'кто поднимается в гору на четырёх ногах и спускается тоже на четырёх?',
       'кто написал маугли?Полное имя.',
       'в какой гостинице погиб Сергей Есенин?',
       'какого цвета язык у жирафа?',
       'cамое высокое здание в мире?',
       'сколько Моника может съесть пельмешек за раз?',
       'самый редкий цвет глаз?']
befree = ['1889',
          '1812',
          'Ватикан',
          'Майкл Джексон',
          'Фреди Меркьюри',
          '40 лет',
          'актёр',
          'горный козёл',
          'Редьярд Киплинг',
          'Англетер',
          'синий',
          'Бурдж-Халиф',
          '16',
          'зелёный']


score = 0


print(omg[0])
i = input('пиши ответ здесь:')

if i.lower() == befree[0].lower():
    print('Молодец!')
    score += 1
else:
    print('неправильно :(')


print(omg[1])

i = input('пиши ответ здесь:')

if i.lower() == befree[1].lower():
    print('Умничка!')
    score += 1
else:
    print('неправильно :(')



print(omg[2])
i = input('пиши ответ здесь:')

if i.lower() == befree[2].lower():
    print('Молодец!')
    score += 1
else:
    print('неправильно :(')

print(omg[3])
i = input('пиши ответ здесь:')

if i.lower() == befree[3].lower():
    print('Ты кто такой!?')
    score += 3
else:
    print('неправильно :(')

print(omg[4])
i = input('пиши ответ здесь:')

if i.lower() == befree[4].lower():
    print('Ты кто такой!?')
    score += 2
else:
    print('неправильно :(')

print(omg[5])
i = input('пиши ответ здесь:')

if i.lower() == befree[5].lower():
    print('Фантастика!')
    score += 2
else:
    print('неправильно :(')

print(omg[6])
i = input('пиши ответ здесь:')

if i.lower() == befree[6].lower():
    print('Ты кто такой!?')
    score += 9
else:
    print('неправильно :(')


print(omg[7])
i = input('пиши ответ здесь:')

if i.lower() == befree[7].lower():
    print('Ты кто такой!?')
    score += 2
else:
    print('неправильно :(')


print(omg[8])
i = input('пиши ответ здесь:')

if i.lower() == befree[8].lower():
    print('Ты кто такой!?')
    score += 2
else:
    print('неправильно :(')

print(omg[9])
i = input('пиши ответ здесь:')

if i.lower() == befree[9].lower():
    print('Ты кто такой!?')
    score += 2
else:
    print('неправильно :(')

print(omg[10])
i = input('пиши ответ здесь:')

if i.lower() == befree[10].lower():
    print('Ты кто такой!?')
    score += 3
else:
    print('неправильно :(')

print(omg[11])
i = input('пиши ответ здесь:')

if i.lower() == befree[11].lower():
    print('Ты кто такой!?')
    score += 5
else:
    print('неправильно :(')

print(omg[12])
i = input('пиши ответ здесь:')

if i.lower() == befree[12].lower():
    print('Ты кто такой!?')
    score += 4
else:
    print('неправильно :(')


print(omg[13])
i = input('пиши ответ здесь:')

if i.lower() == befree[13].lower():
    print('Ты кто такой!?')
    score += 1
else:
    print('неправильно :(')


print(score)

if score == 0:
    print('Очень жаль,но надежды были')

elif score > 0 and score < 33:
    print('Молодец,хочешь пройти ещё раз чтобы быть профи и заработать больше баллов?Перезапусти программу')

else:
    print('Ты огромный молодец!Мы будем рады если ты пройдёшь и другие наши викторины')

















