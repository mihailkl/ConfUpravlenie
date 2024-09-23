# Практическое занятие №2. Менеджеры пакетов

## Задача 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
![alt-text](https://sun9-72.userapi.com/impg/712TEEYgHSI_WjtD2-Y9YJt9R-hOoCcCOk_HfQ/s2Wx0TVQgms.jpg?size=687x198&quality=96&sign=6ce84df5bb413e93349113de8952b8b2&type=album)
![alt-text](https://sun9-31.userapi.com/impg/eHhnqvzOSxrzmYluf-Nm43ClTzSVuZWQ1O2uJA/Hp_fRLpaQHk.jpg?size=1106x74&quality=96&sign=a784c61f289b061ea5f585802721071d&type=album)

## Задача 2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
![alt-text](https://sun9-19.userapi.com/impg/s44yD81cEyyEA9kMXCya8xMQgbMJJE2w5bL0Ng/693IPNbggEU.jpg?size=1080x729&quality=96&sign=d4abe465e5edf24cb51af7a6e2eeda01&type=album)

## Задача 3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.
![alt-text](https://sun9-10.userapi.com/impg/bi6YQ4vXQNkmqLAaACLb0kW95jhPeUccyqBnwg/5uQZXYrGXy0.jpg?size=1899x726&quality=96&sign=144f31203e2ef4708b67b0215e3595e5&type=album)
![alt-text](https://sun9-18.userapi.com/impg/46RlR1g2khsYX0voMbVGw4_021hIRftN-C4vGg/RpeN4JQ9fLM.jpg?size=1864x1051&quality=96&sign=fb184674d1f488f86e629839867d1d76&type=album)

## Задача 4
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.
![alt-text](https://sun9-77.userapi.com/impg/mWTKoikeg1U_zmABr9LC6cULo3Upl-O_G9HPNg/pDiqIxP-yJM.jpg?size=1417x902&quality=96&sign=4af6a1d323da90eb5d525dd75eed113a&type=album)

## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![](images/pubgrub.png)

![alt-text](https://sun9-79.userapi.com/impg/XCBbEcLd_cQoNGv5_ckkpr3vH_Nnt0__aeuXjw/OoQxBSPzkvc.jpg?size=1697x804&quality=96&sign=8d2fcffb787810cc6cba135e2542958e&type=album)

## Задача 6

Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```
![alt-text](https://sun9-42.userapi.com/impg/oOfi63tKHBdcihzG14SoYUbYVcjrhoQvJbds8g/-uiZPYYtWwM.jpg?size=1908x804&quality=96&sign=1a24837c0bbac5c0b326d927f5123198&type=album)
