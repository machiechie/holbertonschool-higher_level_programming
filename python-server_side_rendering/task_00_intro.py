import os

def generate_invitations(template, attendees):
    # Проверка типа template
    if not isinstance(template, str):
        print(f"Error: Template should be a string, got {type(template).__name__}")
        return
    
    # Проверка типа attendees
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees should be a list of dictionaries, got {type(attendees).__name__}")
        return
    
    # Проверка пустого шаблона
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Проверка пустого списка участников
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    # Обработка каждого участника
    for idx, attendee in enumerate(attendees, start=1):
        # Формируем словарь для подстановки значений, если что-то пропущено — N/A
        data = {
            "name": attendee.get("name") or "N/A",
            "event_title": attendee.get("event_title") or "N/A",
            "event_date": attendee.get("event_date") or "N/A",
            "event_location": attendee.get("event_location") or "N/A"
        }
        
        # Подставляем значения в шаблон
        content = template.format(**data)
        
        # Пишем в файл output_X.txt
        filename = f"output_{idx}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    
    print(f"{len(attendees)} invitation(s) generated successfully.")
