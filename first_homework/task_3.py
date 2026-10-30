from collections import Counter


def main():
    orders = [
        {'id': 1, 'buyer': 'anya', 'status': 'delivered', 'amount': 900},
        {'id': 2, 'buyer': 'boris', 'status': 'returned', 'amount': 4_500},
        {'id': 3, 'buyer': 'anya', 'status': 'delivered', 'amount': 1_500},
        {'id': 4, 'buyer': 'vera', 'status': 'delivered', 'amount': 3_200},
        {'id': 5, 'buyer': 'boris', 'status': 'delivered', 'amount': 700},
        {'id': 6, 'buyer': 'gleb', 'status': 'returned', 'amount': 2_100},
    ]

    print('Возвраты оформили на сумму в', sum([order['amount'] for order in orders if order['status'] == 'returned']))
    print(f'Заказы возвращали {', '.join({order['buyer'] for order in orders if order['status'] == 'returned'})}')
    print(Counter([order['status'] for order in orders])['delivered'], 'заказа доехали до покупателей')

    delivered_orders = [order['amount'] for order in orders if order['status'] == 'delivered']
    print('Средний чек доставленных заказов', sum(delivered_orders) / len(delivered_orders))


if __name__ == '__main__':
    main()
