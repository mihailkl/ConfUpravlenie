# Практическое задание №6. Системы автоматизации сборки
Работа с утилитой Make.
Изучить основы языка утилиты make. Распаковать в созданный каталог [make.zip](make.zip), если у вас в в системе нет make.
Создать приведенный ниже Makefile и проверить его работоспособность.
```
dress: trousers shoes jacket
    @echo "All done. Let's go outside!"

jacket: pullover
    @echo "Putting on jacket."

pullover: shirt
    @echo "Putting on pullover."

shirt:
    @echo "Putting on shirt."

trousers: underpants
    @echo "Putting on trousers."

underpants:
    @echo "Putting on underpants."

shoes: socks
    @echo "Putting on shoes."

socks: pullover
    @echo "Putting on socks."
```
![alt-text](https://sun9-41.userapi.com/impg/19BxAH7YWPYLc4F2U0wgKtLU5krjTzL2_FRUvA/wEVt1KJJ2AQ.jpg?size=427x329&quality=96&sign=6a378ea902a65701253824ed640164b1&type=album)

## Задача 1
Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: [civgraph.json](civgraph.json).
Пример:

```
> make mathematics
mining
bronze_working
sailing
astrology
celestial_navigation
pottery
writing
code_of_laws
foreign_trade
currency
irrigation
masonry
early_empire
mysticism
drama_poetry
mathematics
```
![alt-text](https://sun9-25.userapi.com/impg/NXVZRLOKlug8zJV-f1HJxbp9VbzsPzDt_-YiIw/aOVJctbN2Q0.jpg?size=926x669&quality=96&sign=e76977e82282e607e8b9e79597961972&type=album)
![alt-text](https://sun9-21.userapi.com/impg/1Odj4Siu1cA2AhDnlj_edTg2QoALMeVoTaUNSg/HpPdQk3Qi_w.jpg?size=528x758&quality=96&sign=38c0f5eb357eb50a796e228969a44f37&type=album)

## Задача 2
Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".
![alt-text](https://sun1-23.userapi.com/impg/mjVhudRdTkGcgheHqjqajn_XRYXTJb_03DbH_A/Fo851IPjLSc.jpg?size=904x829&quality=96&sign=db5a5852adc1bd1c09eae75b84ba142d&type=album)
![alt-text](https://sun9-64.userapi.com/impg/nr-K-_i50j07blVdzNsPvkY6vwaQcFxcQf4BaQ/RhvFXReeUzc.jpg?size=1224x886&quality=96&sign=9f4519f292d7e08de4a18aba32fbd86b&type=album)

## Задача 3
Добавить цель clean, не забыв и про "животное".
![alt-text](https://sun9-6.userapi.com/impg/_uS7JegA2-H659CTyyJl6bTN96gBXjFQdviYdg/KiZIiT226fA.jpg?size=944x913&quality=96&sign=a8307b4dc53c804f3009a8c9102c31a4&type=album)
![alt-text](https://sun9-18.userapi.com/impg/wBGVQgv889dBj2syVVBfLF8ncQa57qevAmXl9A/cD_KrQPIVss.jpg?size=711x890&quality=96&sign=0c73f23bb8f58dfa561fb74dbe8fe4c7&type=album)

## Задача 4
Написать makefile для следующего скрипта сборки:

```
gcc prog.c data.c -o prog
dir /B > files.lst
7z a distr.zip *.*
```

Вместо gcc можно использовать другой компилятор командной строки, но на вход ему должны подаваться два модуля: prog и data.
Если используете не Windows, то исправьте вызовы команд на их эквиваленты из вашей ОС.
В makefile должны быть, как минимум, следующие задачи: all, clean, archive.
Обязательно покажите на примере, что уже сделанные подзадачи у вас не перестраиваются.
![alt-text](https://sun9-42.userapi.com/impg/EOcPEgxCIwNa6SHn0vBywYWbCV_pAtdyQbfZFA/p3RCR_Pk1pQ.jpg?size=626x615&quality=96&sign=e8393fdd66d9d309fa739bd182f14721&type=album)
![alt-text](https://sun9-6.userapi.com/impg/hwGCuTQj5Ge2wjF1SaPwyg78MhitCy7JazzdFg/AXyAtZdYc88.jpg?size=628x1099&quality=96&sign=972e82dc28ae726ff80f8149c31d2199&type=album)
