## Задача 1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
![alt-text](https://sun9-31.userapi.com/impg/lqtwqWiJB3ngMbqWAKnA7qU69zOaXtOIidFgjw/tFG_bRnHIOQ.jpg?size=981x889&quality=96&sign=9b30a532533149697acd712961167428&type=album)

## Задача 2

Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

```
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    <добавьте ваши данные в качестве четвертого студента>
  ],
  "subject": "Конфигурационное управление"
} 
```
![alt-text](https://sun9-64.userapi.com/impg/ispy3GfFvg-BqId42BbtqR9NBBb-5fraLK70Aw/BgPFDlRvOd4.jpg?size=996x412&quality=96&sign=c0aa5fcc14c6c219845d20a9550a2f9c&type=album)
Для решения дальнейших задач потребуется программа на Питоне, представленная ниже. Разбираться в самом языке Питон при этом необязательно.

```Python
import random


def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))

```

Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF:

## Задача 3

Язык нулей и единиц.

```
10
100
11
101101
000
```
![alt-text](https://sun9-30.userapi.com/impg/lNHpoc_MKPO0U8bMEM29_24QfQT6aJ_d_WVOZQ/Jr69ytO9t7I.jpg?size=661x426&quality=96&sign=812fda8692d83cd29c5704114d010dc8&type=album)

## Задача 4

Язык правильно расставленных скобок двух видов.

```
(({((()))}))
{}
{()}
()
{}
```
![alt-text](https://sun9-23.userapi.com/impg/vu3HkWfm4pFSuH5SNp9GXYMypvDkPg-RtmahGA/8AB-KYMalVs.jpg?size=621x434&quality=96&sign=9801ae89f469cfeeeef7dd3051c456f6&type=album)

## Задача 5

Язык выражений алгебры логики.

```
((~(y & x)) | (y) & ~x | ~x) & x
y & ~(y)
(~(y) & y & ~y)
~x
~((x) & y | (y) | (x)) & x | x | (y & ~y)
```
![alt-text](https://sun9-74.userapi.com/impg/zwK_mtf2F_8L8PvCVUMlmZzUpn9IyoBoy3YHnQ/39lpqj85K6E.jpg?size=607x431&quality=96&sign=45bb35661ae10703b4f691795daf6297&type=album)
