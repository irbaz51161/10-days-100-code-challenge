def main():
    temperature = int(input("Enter the temperature: "))
    conversion = input("In which type the user temperature was?\nFahrenheit or Celcius? (F or C)").upper()
    convert(temperature, conversion)

def convert(temp, con):
    if con == "F":
        c = (temp -32) * 5/9
        print(f"Your temperature in Celcius is {int(c)}C")
    elif con == "C":
        f = (temp * 9/5) + 32
        print(f"Your temperature in Fahrenheit is {int(f)}F.")

main()