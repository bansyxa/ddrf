import datetime, re
while True:
    print(f"Доступные пиццы:\n",
               f"1.Маргарита\n",
               f"2.Пепперони\n",
               f"3.Грибная\n",
               f"4.Четыре сыра\n",
               f"5.Капричоза\n")
    rita="Маргарита"
    pepe="Пепперони"
    geb="Грибная"
    sir="Четыре сыра"
    kapri="Капричоза"
    regex=re.compile("вкусно")
    number_pizza=int(input('Какую пиццу вы хотите заказать?(Введите номер) :'))
    if number_pizza == 1:
        name_pizza=rita
    elif number_pizza == 2:
        name_pizza=pepe
    elif number_pizza == 3:
        name_pizza=geb
    elif number_pizza == 4:
        name_pizza=sir
    elif number_pizza == 5:
        name_pizza=kapri
    how_many=int(input("Сколько пицц вы хотите заказать?(Введите количество) :"))
    print(f"Вы заказали {how_many} пицц {name_pizza}" )
    feedback=input("Готовы ли вы оставить отзыв?(да/нет) :")
    if feedback == "да":
        text_feedback=input("Введите ваш отзыв: ")
        if regex.search(text_feedback):
            print("Спасибо за положительный отзыв!Получите бесплатную пиццу")
        else:
            print("Спасибо за положительный отзыв")
            break
    if feedback == "нет":
            print("Спасибо что воспользовались нашим сервисом!")
            break