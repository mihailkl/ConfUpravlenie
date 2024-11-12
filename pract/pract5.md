# Практическое занятие №5. Вопросы виртуализации

## Задача 1

Исследование виртуальной стековой машины CPython.

Изучите возможности просмотра байткода ВМ CPython.

```
import dis

def foo(x):
    while x:
        x -= 1
    return x + 1

print(dis.dis(foo))
```

Опишите по шагам, что делает каждая из следующих команд (приведите эквивалентное выражение на Python):

 11           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               1 (10)
              4 BINARY_MULTIPLY
              6 LOAD_CONST               2 (42)
              8 BINARY_ADD
             10 RETURN_VALUE
![alt-text](https://sun9-75.userapi.com/impg/LYdb-g15nEMJhfRmIi0ay2O_5LCwbUnPQD7AVA/xnkvSEdi_WU.jpg?size=772x992&quality=96&sign=be8246c6d8aa10c9f781fc4a87ea30df&type=album)
![alt-text](https://sun9-63.userapi.com/impg/j5vLX31K9K2SQhbc-R1xez8bA9bBUSaBq6AMyA/YsTzE2cCp3c.jpg?size=1294x761&quality=96&sign=14d4825afbf352036a0a79ba5e538e30&type=album)

## Задача 2
Что делает следующий байткод (опишите шаги его работы)? Это известная функция, назовите ее.

```
  5           0 LOAD_CONST               1 (1)
              2 STORE_FAST               1 (r)

  6     >>    4 LOAD_FAST                0 (n)
              6 LOAD_CONST               1 (1)
              8 COMPARE_OP               4 (>)
             10 POP_JUMP_IF_FALSE       30

  7          12 LOAD_FAST                1 (r)
             14 LOAD_FAST                0 (n)
             16 INPLACE_MULTIPLY
             18 STORE_FAST               1 (r)

  8          20 LOAD_FAST                0 (n)
             22 LOAD_CONST               1 (1)
             24 INPLACE_SUBTRACT
             26 STORE_FAST               0 (n)
             28 JUMP_ABSOLUTE            4

  9     >>   30 LOAD_FAST                1 (r)
             32 RETURN_VALUE
```
![alt-text](https://sun9-34.userapi.com/impg/WMTM6VJABm5Gh3lDHC5AyqOsxzgW3gxmJ5EkDA/LWUha8yqiwQ.jpg?size=777x564&quality=96&sign=fe49c1f68f3eaad34b435d21438735fa&type=album)

## Задача 3
Приведите результаты из задач 1 и 2 для виртуальной машины JVM (Java) или .Net (C#).
![alt-text](https://sun9-67.userapi.com/impg/qpUblliSUEuGtNqa7VaJGMzFWR_49xtIJClruA/d4niByCuAtI.jpg?size=1245x853&quality=96&sign=c058d1e6ebba55831250a795c48c13d5&type=album)

## Задача 4
Работа с qemu. Скачать и установить ISO-образ Alpine Linux для виртуальных машин с официального сайта.
Создать с помощью qemu образ жесткого диска (опция -f qcow2). Объем диска 500 Мб.
Запустить Alpine Linux с CD-ROM.
Установить систему на sda. Изменить motd.
Загрузиться уже с sda.
Прислать полный список команд для установки и загрузки, а также скриншот с motd, где фигурируют ваши имя и фамилия.
![alt-text](https://sun9-19.userapi.com/impg/dxOTiLLWHObyJj_dxvOCzRdOEccuPUhBverNYg/wChRqs4c96M.jpg?size=1850x909&quality=96&sign=0841bf49292918c27ef6bbfc986c8366&type=album)
![alt-text](https://sun1-92.userapi.com/impg/iwmDVkCkaBLrZ2E_3FT_9E9TL8KyYfVQk3O76Q/J4PIkob9_kU.jpg?size=1272x806&quality=96&sign=0890a78bc7f7b717638f25bee5286dce&type=album)
![alt-text](https://sun9-34.userapi.com/impg/_4m7usM-Sc7TXIiGncEtkLBA3z22zmiwY9fCqA/OTuDx1UBv2Y.jpg?size=1277x856&quality=96&sign=fe9a2d7a965b9dee6ac40751e37f5229&type=album)
![alt-text](https://sun1-57.userapi.com/impg/Iaz4fpfuEptPJd_IiqXhTo7txC169J0Sl85RKw/5k5esv6C0Tk.jpg?size=1281x866&quality=96&sign=24208f950364739a9f527b2d56566baf&type=album)

Команды:
```
qemu-img create alpine.img 1G
qemu-system-x86_64 -m 1024 -k none -nic user,ipv6=off,hostfwd=tcp::22022-:22 -boot order=cd -drive file=alpine.img,format=raw,index=0,media=disk -cdrom alpine.iso 
setup-alpine
su
echo "Kleymenov Mihail" > /etc/motd
cat /etc/motd
qemu-system-x86_64 -m 1024 -hda alpine.img -boot c
```
