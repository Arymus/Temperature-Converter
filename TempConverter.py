print("Temperature Converter: F° & C°")
while True:
  choice = input("Choose your unit: ")
  if choice == "1":
    print("You chose fahrenheit to celsius!")
  elif choice == "2":
    print("You chose celsius to fahrenheit!")
  else:
    print("Invalid input. Type 1 for fahrenheit to celsius, or pick 2 for celsius to fahrenheit.")
  input_temperature = input("Enter the number you'd like to convert: ")
  if choice == "1":
    fahrenheit = float(input_temperature)
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")
  elif choice == "2":
    celsius = float(input_temperature)
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")