# 1. Клонирование репозитория

Склонируйте репозиторий с исходным кодом и тестами:

```bash
git clone <URL репозитория>
cd <директория проекта/dz/dz4>
```

# 2. Установка зависимостей и запуске
unittest

## Запуск
```bash
python assembler.py test_program.asm test_program.bin test_program.json
python interpreter.py test_program.bin results_test_program.json "1000:1007"
```

# 3. Структура проекта
Проект содержит следующие файлы и директории, связанные с тестированием:
```bash
assembler.py                            # Файл с преобразованием ассемблера в бин файл
interpreter.py                          # Файл с интепретацией бин файла
test_program.asm                        # Файл с ассемблером программой
```

# 4. Запуск тестов
В этом руководстве описывается, как запустить тесты для команд эмулятора оболочки. Мы будем использовать модуль Python `unittest` для тестирования.
```bash
python test.py
```
