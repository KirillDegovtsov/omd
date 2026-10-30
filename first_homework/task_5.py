from itertools import groupby


def main():
    reviews = [
        {'id': 1, 'product': 'Чехол', 'stars': 5},
        {'id': 1, 'product': 'Чехол', 'stars': 3},
        {'id': 1, 'product': 'Чехол', 'stars': 4},
        {'id': 2, 'product': 'Наушники', 'stars': 2},
        {'id': 2, 'product': 'наушники', 'stars': 2},
        {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
        {'id': 3, 'product': 'Планшет', 'stars': 5},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 5, 'product': 'Кабель', 'stars': 1},
    ]

    for review in reviews:
        review['product'] = review['product'].lower().capitalize()

    ratings = []
    sorted_reviews = sorted(reviews, key=lambda review: review['product'])
    for product, group in groupby(sorted_reviews, key=lambda review: review['product']):
        stars = [item['stars'] for item in group]
        avg = sum(stars) / len(stars)
        print(f'У товара {product} средняя оценка {avg}')
        if len(stars) >= 2:
            ratings.append((avg, product))

    print('Худший товар по средней оценке среди тех, у кого хотя бы два отзыва', min(ratings)[1])
    low_stars = [1 for review in reviews if review['stars'] == 1 or review['stars'] == 2]
    print('Отзывов на 1 или 2 звезды', sum(low_stars))
    print(f'Отзывы на 1 или 2 звезды составляют {(sum(low_stars) / len(reviews)) * 100:.0f}% от всех отзывов')


if __name__ == '__main__':
    main()
