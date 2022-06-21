def greet_student():
    students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
    i = 0
    while i < len(students):
        year = 2022 - students[i]["age"]
        name = students[i]["name"]
        print(f"Hello {name}, you were born in the year {year}")
        i+=1 
greet_student()   