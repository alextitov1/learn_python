# -*- coding: utf-8 -*-
"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

SALLES = [
    {'product': 'iPhone 12', 'items_sold': [
        363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [
        317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [
        343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main():
    for phone in SALLES:
        print(f"Model: {phone['product']}")
        print(f"Total salles: {sum(phone['items_sold'])}")
        print(
            f"Avarage salle: {sum(phone['items_sold']) / len(phone['items_sold']):.1f}")
        print()

    total_salles = sum([sum(phone['items_sold']) for phone in SALLES])
    number_of_salles = sum([len(phone['items_sold']) for phone in SALLES])
    ava_salles = total_salles / number_of_salles

    print(f"Total salles: {total_salles}")
    print(f"Avarage salle: {ava_salles}")


if __name__ == "__main__":
    main()
