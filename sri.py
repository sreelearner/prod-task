def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def convert_temperature(value, unit):
    unit = unit.lower()

    if unit == 'c' or unit == 'celsius':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"{value}°C is equal to {f:.2f}°F and {k:.2f}K.")
    elif unit == 'f' or unit == 'fahrenheit':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"{value}°F is equal to {c:.2f}°C and {k:.2f}K.")
    elif unit == 'k' or unit == 'kelvin':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"{value}K is equal to {c:.2f}°C and {f:.2f}°F.")
    else:
        print("Invalid temperature unit. Please use Celsius (C), Fahrenheit (F), or Kelvin (K).")


def main():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")
        convert_temperature(value, unit)
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")


if __name__ == "__main__":
    main()
