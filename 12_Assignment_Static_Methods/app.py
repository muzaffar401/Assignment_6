# TemperatureConverter class banayi hai
class TemperatureConverter:

    @staticmethod  # ye batata hai ke ye static method hai (na self chahiye, na cls)
    def celsius_to_fahrenheit(c):  # sirf input le raha hai, object se kuch lena dena nahi
        return (c * 9/5) + 32  # formula lagaya Celsius ko Fahrenheit me convert karne ka

# direct class ke naam se static method call karte hain
temp_in_f = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"25°C is equal to {temp_in_f}°F")  # Output: 25°C is equal to 77.0°F
