import json

id = input("Введите номер квалификации: ")
find = False

with open("dump.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    for skill in data:
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == id:
                skill_code = skill["fields"].get("code")
                skill_title = skill["fields"].get("title")
                find = True

                for specialty in data:
                    if specialty.get("model") == "data.specialty":
                        specialty_code = specialty["fields"].get("code")
                        if specialty_code in skill_code:
                            specialty_title = specialty["fields"].get("title")
                            specialty_educational = specialty["fields"].get("c_type")
                            specialty_id = specialty["fields"].get("code")

if not find:
    print("=============== Не найдено ===============")
else:
    print("=============== Найдено ===============")
    print(f"{specialty_id} >> Специальность '{specialty_title}', {specialty_educational}")
    print(f"{id} >> Квалификация '{skill_title}'")