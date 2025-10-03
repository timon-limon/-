    # Создание словаря
    my_dict = {}

    # Добавление пар "ключ-значение"
    my_dict["apple"] = "яблоко"
    my_dict["banana"] = "банан"

    # Доступ к значению по ключу
    print(my_dict["apple"])  # Выведет: яблоко

    # Проверка наличия ключа
    if "banana" in my_dict:
        print("Банан есть в словаре")

    # Удаление пары
    del my_dict["apple"]
