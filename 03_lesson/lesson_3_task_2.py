from smartphone import Smartphone
catalog =[Smartphone("LG", "3344", "+79995556600"), Smartphone("Nokia", "3310", "+79298810000"),
          Smartphone("Jira", "007", "+79120010101"), Smartphone("Imo", "904", "+79015509283"),
          Smartphone("Huawey", "Mottal", "+79113482929")]
for item in catalog:
    print(f'Марка: {item.type} - модель {item.model}. Номер телефона :{item.phone_number}')