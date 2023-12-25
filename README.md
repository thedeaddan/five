#### Описание

Этот репозиторий представляет собой утилиту для решения игры 5 букв от банка Тинькофф. Программа позволяет пользователям задать условия для поиска слов, соответствующих определенному шаблону и набору букв.

#### Использование

1. **Установка Python**: Если у вас еще не установлен Python, выполните [инструкции по установке](https://www.python.org/downloads/).
2. **Создание виртуального окружения (рекомендуется)**:
   - **Windows**:
     1. Откройте `cmd`.
     2. Перейдите в директорию репозитория.
     3. Введите `python -m venv venv` для создания виртуального окружения.
     4. Активируйте окружение: `venv\Scripts\activate`.
   - **macOS и Linux**:
     1. Откройте терминал.
     2. Перейдите в директорию репозитория.
     3. Введите `python3 -m venv venv` для создания виртуального окружения.
     4. Активируйте окружение: `source venv/bin/activate`.
3. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Запустите утилиту, выполнив команду: `python main.py`.
5. Введите требуемые параметры для поиска слов.

#### Структура репозитория

- `main.py`: Основной файл утилиты.
- `russian_nouns_with_definition.json`: Файл с данными слов и их определениями.
- `requirements.txt`: Список зависимостей для утилиты.

Приложение разработано для помощи в решении игры и предоставляет пользователю информацию о соответствующих словах и их определениях.