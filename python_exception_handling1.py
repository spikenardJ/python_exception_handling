# Question 1: Exceptional Weather Forecast

# Task 2: Temperature Conversion

def temperature_conversion(fahrenheit_input):
    try:
        result = (fahrenheit_input - 32) * 5/9
        result1 = "{:.2f}".format(result)
        return result1
    except ValueError:
        print("Please enter the temperature in Fahrenheit using only numbers.")

# Task 3: User Experience

def temperature_conversion_main():
    while True:
        try:
            # Task 1: Start
            fahrenheit_input = float(input("To convert to Celsius, please enter your temperature in Fahrenheit: "))
            result1 = temperature_conversion(fahrenheit_input)
            if fahrenheit_input < 60:
                print(f"Brrrrrr 🥶 {fahrenheit_input}◦ Fahrenheit is {result1}◦ Celsius.")
            elif 75 > fahrenheit_input >= 60:
                print(f"Nice! 😎 {fahrenheit_input}◦ Fahrenheit is {result1}◦ Celsius.")
            elif fahrenheit_input >= 75:
                print(f"Oh my! 🥵 {fahrenheit_input}◦ Fahrenheit is {result1}◦ Celsius.")
            continue_input = input("Would you like to convert another temperature from Fahrenheit to Celsius? (yes/no) ").lower()
            if continue_input != "yes":
                print("Have a great day! 👋")
                break
            else:
                fahrenheit_input1 = float(input("Please enter your next temperature in Fahrenheit: "))
                result2 = temperature_conversion(fahrenheit_input1)
                if fahrenheit_input1 < 60:
                    print(f"Brrrrrr 🥶 {fahrenheit_input1}◦ Fahrenheit is {result2}◦ Celsius.")
                elif 75 > fahrenheit_input1 >= 60:
                    print(f"Nice! 😎 {fahrenheit_input1}◦ Fahrenheit is {result2}◦ Celsius.")
                elif fahrenheit_input1 >= 75:
                    print(f"Oh my! 🥵 {fahrenheit_input1}◦ Fahrenheit is {result2}◦ Celsius.")
                    continue
        except ValueError:
                    print("Please enter the temperature in Fahrenheit using only numbers.")
        

# Task 4: Finally

        finally:
            print("🌤️ Thank you for using the weather forecast application! ⛈️")
                    
            
temperature_conversion_main()