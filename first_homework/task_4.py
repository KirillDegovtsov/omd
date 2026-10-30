def main():
    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    print('Выручка за всю неделю', sum([day['revenue'] for day in days]))
    print(f'В {sorted(days, key=lambda day: day['revenue'], reverse=True)[0]['day']} была самая большая выручка')
    print('\n'.join([f'В {day['day']} средняя выручка на один заказ была {day['revenue'] / day['orders']}' for day in days]))
    print(f'В {', '.join([day['day'] for day in days if day['returns'] / day['orders'] > 0.2])} было возвратов больше 20% заказов')


if __name__ == '__main__':
    main()
