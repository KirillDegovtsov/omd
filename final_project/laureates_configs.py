from json_dict_processing import create_processor
from prizes_configs import process_prizes


def process_year(date_string: str | None) -> int | None:
    """Извлекает год"""
    if not date_string:
        return None
    return int(date_string[:4])


CONFIG_PERSON = {
    'id': (['id'], int),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], process_prizes),
}


CONFIG_ORG = {
    'id': (['id'], int),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], process_prizes),
}


person_processor = create_processor(CONFIG_PERSON, list_processor=False)
org_processor = create_processor(CONFIG_ORG, list_processor=False)

process_persons = person_processor
process_orgs = org_processor
