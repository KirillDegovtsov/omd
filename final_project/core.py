import json


def load_laureates(file_path='laureates.json') -> list[dict]:
    """Читает список лауреатов из JSON"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)['laureates']
