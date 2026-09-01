def triage_patient():
    valid_input = False

    while valid_input == False:
        try:
            severity = int(input("Enter severity level (1-10): "))

            if severity >= 1 and severity <= 10:
                valid_input = True
            else:
                print("Error! Please enter a whole number from 1 to 10.")

        except ValueError:
            print("Error! Please enter a whole number from 1 to 10.")

    if severity >= 1 and severity <= 4:
        room = "Waiting Room"

    elif severity >= 5 and severity <= 7:
        room = "Room 1"

    else:
        room = "Room 2"

    print("\nTriage Summary")
    print("Severity Level:", severity)
    print("Assigned Room:", room)


triage_patient()
