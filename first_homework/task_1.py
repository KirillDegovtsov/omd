def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print(f'Товары {', '.join(map(str, moscow & kazan))} можно забрать и в Москве и в Казани')
    print(f'Товары {', '.join(map(str, moscow - kazan))} есть только в Москве')
    print(f'Товары {', '.join(map(str, kazan - moscow))} есть только в Казани')
    print(f'На двух складах {len(kazan | moscow)} разных товаров')


if __name__ == '__main__':
    main()
