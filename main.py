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
                skill_specialty=skill["fields"].get("specialty") #Присваивание переменной кода квалификации
                find = True #Изменение булевой переменной в случае если данные найдены
                
if not find: #Проверяем, была ли найдена квалификация
    print("================== Не найдено ==================") #Вывод на консоль
    exit()

else: #Оператор else если квалификация найдена
    for specialty in data: #Цикл for для перебора элементов файла
        if specialty.get("model") == "data.specialty": #Оператор if для проверки равняется ли значением ключа data.specialty
            specialty_code = specialty["fields"].get("code") #Присваивание переменной кода специальности
            specialty_pk = specialty.get("pk") #Присваивание переменной кода pk

            if skill_specialty == specialty_pk: #Оператор if для проверки равняются ли значения pk и кода специальности 
                specialty_title = specialty["fields"].get("title") #Присваивание переменной названия специальности
                specialty_educational = specialty["fields"].get("c_type") #Присваивание переменной типа образования 
                specialty_c = specialty["fields"].get("code") #Присваивание переменной кода специальности
    print("================== Найдено ==================") #Вывод на консоль
    print(f"{specialty_c} >> Специальность '{specialty_title}', {specialty_educational}") #Форматированный вывод на консоль 
    print(f"{id} >> Квалификация '{skill_title}'") #Форматированный вывод на консоль
