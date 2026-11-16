from collections import Counter, defaultdict
from collections.abc import Callable, Iterable


def where(data: list[dict], predicate: Callable) -> list[dict]:
    """Фильтр строк по условию"""
    return [row for row in data if predicate(row)]


def group_by(data: list[dict], columns: list[str]) -> dict[tuple, list[dict]]:
    """Группировка строк по указанным столбцам"""
    grouped = defaultdict(list)

    for row in data:
        # Кортеж объединяет значения всех полей группировки в один ключ.
        key = tuple(row.get(column) for column in columns)
        grouped[key].append(row)

    return dict(grouped)


def missing_stats(data: list[dict]) -> tuple[dict[str, int], dict[str, float]]:
    """Пропуски и их доли"""
    totals = Counter()
    missing = Counter()

    for row in data:
        for field, value in row.items():
            totals[field] += 1
            if value is None or value == []:
                missing[field] += 1

    counts = {field: missing[field] for field in totals}
    shares = {field: round(missing[field] / total, 4) for field, total in totals.items()}
    return counts, shares


def summarize_ids(data: list[dict]) -> tuple[dict, dict, list[int], list[tuple[int, int]]]:
    """Максимальный и минимальный ID, повторяющиеся ID и разрывы"""
    id_counts = Counter(row['id'] for row in data)
    ids = sorted(id_counts)
    duplicate_ids = [row_id for row_id, count in id_counts.items() if count > 1]
    id_gaps = [(left, right) for left, right in zip(ids, ids[1:]) if right - left > 1]
    first_id_row = min(data, key=lambda row: row['id'])
    last_id_row = max(data, key=lambda row: row['id'])
    return first_id_row, last_id_row, duplicate_ids, id_gaps


def top_n_counts(values: Iterable, n: int = 5) -> list[tuple]:
    """Возвращает n самых частых заполненных значений"""
    counts = Counter(value for value in values if value is not None)
    return counts.most_common(n)


def flatten_prizes(laureates: list[dict]) -> list[dict]:
    """Добавляет к каждой записи о премии сведения о лауреате"""
    result = []

    for laureate in laureates:
        laureate_fields = {
            'laureate_id': laureate['id'],
            'country_now': laureate.get('country_now'),
            'gender': laureate.get('gender'),
        }
        for prize in laureate['prizes_relevant']:
            result.append({**laureate_fields, **prize})

    return result
