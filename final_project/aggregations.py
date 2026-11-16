from statistics import fmean, median


AGGREGATIONS = {
    'count': len,
    'mean': fmean,
    'median': median,
    'min': min,
    'max': max,
}


def aggregate_rows(data: list[dict], column: str, metrics: list[str]) -> dict:
    """Вычисляем метрики по заполненным значениям столбца"""
    values = [row.get(column) for row in data if row.get(column) is not None]
    return {metric: AGGREGATIONS[metric](values) for metric in metrics}
