# Итоговый проект

## Структура

- `laureates_countries_task.ipynb` - отчёт с пояснениями и выводами
- `core.py` - чтение локального JSON
- `json_dict_processing.py` - универсальная обработка вложенного JSON
- `laureates_configs.py`, `prizes_configs.py` - конфигурации полей
- `dataset_helpers.py` - фильтрация, группировка и контроль пропусков
- `aggregations.py` - среднее, медиана, минимум, максимум и другие метрики
- `attribute_manager.py` - операции со столбцами
- `text_analysis.py`, `stopwords.py` - бонусный анализ мотиваций

## Источник стоп-слов

В `stopwords.py` я использовал слова с сайта https://www.englishclub.com/vocabulary/common-words-100.php

## Запуск

1. Чтобы все корректно отработало в одной дирректории с `laureates_countries_task.ipynb` должен лежать `laureates.json` со всеми данными (сделал такую реализацию, потому что как и у многих вылетала ошибка при обращении по api)

2. Виртуальное окружение и зависимости:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install jupyter flake8
   ```

## Проверка кода

```bash
python -m flake8 *.py
```
