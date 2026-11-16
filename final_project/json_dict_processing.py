def extract_nested_value(obj: dict, keys: list[str]):
    """Возвращает значение по нескольким ключам"""
    current_value = obj

    for key in keys:
        if not isinstance(current_value, dict):
            return None
        current_value = current_value.get(key)

    return current_value


def process_dictionary_with_config(dictionary: dict, config: dict) -> dict:
    """Преобразует вложенный словарь по конфигу, сохраняет пропуски"""
    result = {}

    for attribute, rule in config.items():
        if isinstance(rule, tuple):
            path, processor = rule
            raw_value = extract_nested_value(dictionary, path)
            if raw_value is not None:
                raw_value = processor(raw_value)
            result[attribute] = raw_value
        else:
            result[attribute] = extract_nested_value(dictionary, rule)

    return result


def process_list_of_dicts_with_config(list_of_dicts: list[dict] | None, config: dict) -> list[dict]:
    """Применяет конфигурацию к каждому словарю из списка"""
    return [process_dictionary_with_config(dictionary, config) for dictionary in list_of_dicts or []]


def create_processor(config: dict, list_processor: bool = False):
    """Создаёт функцию с заранее сохранённой конфигурацией"""
    if list_processor:
        processor = process_list_of_dicts_with_config
    else:
        processor = process_dictionary_with_config

    def configured_processor(data):
        return processor(data, config)

    return configured_processor
