from itertools import groupby

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

reviews_copy = reviews.copy()
for i in range(len(reviews_copy)):
    reviews_copy[i]["product"] = reviews_copy[i]["product"].lower().capitalize()

products = []
sorted_reviews_copy = sorted(reviews_copy, key=lambda review: review["product"])
for value, group in groupby(sorted_reviews_copy, key=lambda review: review["product"]):
    stars = [item["stars"] for item in group]
    avg = sum(stars) / len(stars)
    print(f"У товара {value} средняя оценка {avg}")
    if len(stars) >= 2:
        products.append((avg, value))

print("Худший товар по средней оценке среди тех, у кого хотя бы два отзыва", min(products)[1])
low_stars = [1 for review in reviews_copy if review["stars"] == 1 or review["stars"] == 2]
print("Отзывов на 1 или 2 звезды", sum(low_stars))
print(f"Отзывы на 1 или 2 звезды составляют {(sum(low_stars) / len(reviews_copy)) * 100:.0f}% от вех отзывов")
