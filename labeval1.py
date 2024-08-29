students = {
    "Kshitij": {"class": "B1" , "height" : 175 , "weight" : 80, "sport" : "tennis", "calorie": 2100}
    "aayush": {"class": "B1" , "height" : 178 , "weight" : 75, "sport" : "cricket", "calorie": 2400}
    "vandit": {"class": "B1" , "height" : 180 , "weight" : 55, "sport" : "Football", "calorie": 2800}
}

def calculated_diet_chart(students):
    if students["calorie"] < 2000:
        return "Red"

    if students["calorie"]> 2000 and students["calorie"]<2500:
        return "Orange"
    
    if students["calorie"] > 2500:
        return "Green"

for name, details in students.items():
    diet_chart = calculated_diet_chart(details)
    print(f"Student Name: {name}")
    print(f"Class: {class}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Sport: {sport}")
    print(f"Calorie intake: {calorie}")
