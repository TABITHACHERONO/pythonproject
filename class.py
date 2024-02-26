class Temperature:
    @staticmethod
    def convert_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

    @staticmethod
    def convert_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")


Temperature.convert_fahrenheit(25)  
Temperature.convert_celsius(98.6)  