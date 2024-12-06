import json #Подключение модуля json

id = input("Введите номер квалификации: ") #Ввод номера квалификации с клавиатуры
find = False #Создание булевой переменной

with open("dump.json", 'r', encoding='utf-8') as file: #Открытие файла и присваивание его переменной file
    data = json.load(file) #Преобразование файла с помощью функции load()
    for skill in data: #Цикл for для перебора элементов файла
        if skill.get("model") == "data.skill": #Оператор if для проверки является ли значением ключа data.skill
            if skill["fields"].get("code") == id: #Оператор if для проверки равняется ли значению ключа переменная id
                skill_code = skill["fields"].get("code") #Присваивание переменной номера квалификации
                skill_title = skill["fields"].get("title") #Присваивание переменной описания квалификации
                find = True #Изменение булевой переменной в случае если данные найдены

                for specialty in data: #Цикл for для перебора элементов файла
                    if specialty.get("model") == "data.specialty": #Оператор if для проверки является ли значением ключа data.specialty
                        specialty_code = specialty["fields"].get("code") #Присваивание переменной номера специальности
                        if specialty_code in skill_code: #Проверка является ли подстрокой
                            specialty_title = specialty["fields"].get("title") #Присваивание переменной описания специальности
                            specialty_educational = specialty["fields"].get("c_type") #Присваивание переменной типа учреждения образования
                            specialty_id = specialty["fields"].get("code") #Присваивание переменной номера специальности

if not find: #Цикл if для вывода в случае неистинности переменной
    print("=============== Не найдено ===============") #Вывод на консоль
else: #Оператор else для вывода в случае истинности переменной
    print("=============== Найдено ===============") #Вывод на консоль
    print(f"{specialty_id} >> Специальность '{specialty_title}', {specialty_educational}") #Форматированный вывод на консоль
    print(f"{id} >> Квалификация '{skill_title}'") #Форматированный вывод на консоль
