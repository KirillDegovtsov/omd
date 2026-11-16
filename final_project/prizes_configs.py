from json_dict_processing import create_processor


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
    'motivation_en': ['motivation', 'en'],
}
prize_processor = create_processor(CONFIG_PRIZE, list_processor=False)


def process_prizes(prizes: list[dict] | None) -> list[dict]:
    """Обрабатывает каждую премию в списке"""
    return [prize_processor(prize) for prize in prizes or []]
