# Первая домашняя работа

## Установка

Клонировать репозиторий:
```bash
git clone git@github.com:KirillDegovtsov/omd.git
cd omd
git switch first_homework
```

Виртуальное окружение и установка flake8:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install flake8
```

## Запуск заданий
```bash
python first_homework/task_1.py
python first_homework/task_2.py
python first_homework/task_3.py
python first_homework/task_4.py
python first_homework/task_5.py
```

## Проверка кода
```bash
flake8 first_homework/task_*.py
```