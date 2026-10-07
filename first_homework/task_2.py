from collections import Counter

queries = ["чехол", "iphone", "чехол", "наушники", "iphone", "iphone", "кабель", "чехол", "iphone"]

print(f"Всего {len(queries)} поисковых запросов в ленте")
print("\n".join([f"Запрос {request} ввели {times} раз" for request, times in Counter(queries).items()]))
print(f"Запрос {sorted(Counter(queries).items(), key=lambda items: items[1], reverse=True)[0][0]} вводили чаще всего")
most_common = sorted(Counter(queries).items(), key=lambda items: items[1], reverse=True)[0][1]
print(f"Самый частый запрос занимает {(most_common / len(queries)) * 100:.0f}% от всех запросов")
print(f"Запросы {", ".join([request for request, times in Counter(queries).items() if times == 1])} встречались 1 раз")
