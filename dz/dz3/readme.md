# 1. Клонирование репозитория

Склонируйте репозиторий с исходным кодом и тестами:

```bash
git clone <URL репозитория>
cd <директория проекта/dz/dz3>
```

# 2. Установка зависимостей и запуске
pyyaml, unittest

## Запуск
```bash
bash:       cat config.yaml | python config_translator.py
PowerShell: Get-Content config.yaml | python config_translator.py
```

# 3. Структура проекта
Проект содержит следующие файлы и директории, связанные с тестированием:
```bash
config_translator.py                    # Файл с трансляцией
test_config_translator.py               # Файл с тестами
```

# 4. Запуск тестов
В этом руководстве описывается, как запустить тесты для команд эмулятора оболочки. Мы будем использовать модуль Python `unittest` для тестирования.
```bash
python test_config_translator.py
```
