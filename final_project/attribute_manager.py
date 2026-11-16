def add_column(data: list[dict], column: str, value_function) -> list[dict]:
    """Вычисляет новый столбец для каждой строки и возвращает копии строк"""
    return [{**row, column: value_function(row)} for row in data]
