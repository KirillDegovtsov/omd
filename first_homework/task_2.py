from collections import Counter


def main():
    queries = ['чехол', 'iphone', 'чехол', 'наушники', 'iphone', 'iphone', 'кабель', 'чехол', 'iphone']

    len_queries = len(queries)
    queries_counter = Counter(queries)
    print(f'Всего {len_queries} поисковых запросов в ленте')
    print('\n'.join([f'Запрос {request} ввели {times} раз' for request, times in queries_counter.items()]))
    most_common = sorted(queries_counter.items(), key=lambda items: items[1], reverse=True)[0]
    print(f'Запрос {most_common[0]} вводили чаще всего')
    print(f'Самый частый запрос занимает {(most_common[1] / len_queries) * 100:.0f}% от всех запросов')
    print(f'Запросы {', '.join([request for request, times in queries_counter.items() if times == 1])} встречались 1 раз')


if __name__ == '__main__':
    main()
