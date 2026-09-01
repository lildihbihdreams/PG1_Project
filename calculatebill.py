while True:
    patient_type = input("Please enter Patient Type (Subsidised or Private): ").strip().title()
    
    if patient_type in ["Subsidised", "Private"]:
        break
    else:
        print("Invalid type. Try again.")

while True:
    try:
        tests = int(input("Please enter Number of Tests Completed: "))
        
        if tests >= 0:
            break
        else:
            print("Invalid input. Please enter a positive whole number.")
    except ValueError:
        print("Invalid input. Please enter a positive whole number.")

subtotal = 100 + (tests * 10)

if patient_type == "Subsidised":
    total = subtotal * 0.70
else:
    total = subtotal

print("\n--- Final Bill ---")
print(f"Patient Type: {patient_type}")
print(f"Total to Pay: ${total:.2f}")
