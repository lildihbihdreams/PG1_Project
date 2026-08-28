def register_patient():
    while True:
        name = input("Enter patient name: ").strip()
        if name == "":
            print("Error: Name cannot be blank.")
        else:
            break

    while True:
        age = input("Enter patient age: ").strip()
        if not age.isdigit() or int(age) < 1 or int(age) > 110:
            print("Error: Age must be between 1 and 110.")
        else:
            age = int(age)
            break

    while True:
        patient_id = input("Enter patient ID: ").strip()
        if len(patient_id) != 9 or not patient_id[:8].isdigit() or not patient_id[8].isalpha():
            print("Error: ID must be 9 characters long, with the first 8 as digits and the last as a letter.")
        else:
            break

    print("\nPatient Registered Successfully!")
    print("Name:", name)
    print("Age:", age)
    print("ID:", patient_id)


while True:
    register_patient()