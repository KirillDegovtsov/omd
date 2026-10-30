# Вторая домашняя работа

## Установка

Клонировать репозиторий:
```bash
git clone git@github.com:KirillDegovtsov/omd.git
cd omd
git switch second_homework
cd second_homework
```

Виртуальное окружение и установка flake8:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install flake8
```

## Запуск отчётов
Иерархия департаментов и команд:
```bash
python homework2.py 1
```

Сводка по департаментам:
```bash
python homework2.py 2
```

Запись сводки в `department_summary.csv`:
```bash
python homework2.py 3
```

Файл `Corp_Summary.csv` должен находиться в одной папке с `homework2.py`

## Проверка кода

```bash
flake8 homework2.py
```