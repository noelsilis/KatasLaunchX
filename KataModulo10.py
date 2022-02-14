#---------------------------------------------------------------------------------------------------------
#Uso de tracebacks para buscar errores
# - Tracebacks
#Intenta crear un archivo de Python y asígnale el nombre open.py, con el contenido siguiente:
# def main():
#     open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()
#---------------------------------------------------------------------------------------------------------
#Controlando las excepciones
# - Try y Except de los bloques
#Vamos a crear un archivo de Python denominado config.py. El archivo tiene código que busca y
#  lee el archivo de configuración del sistema de navegación:
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")


# if __name__ == '__main__':
#     main()
#---------------------------------------------------------------------------------------------------------
#Generación de excepciones

# def water_left(astronauts, water_left, days_left):
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     return f"Total water left after {days_left} days is: {total_water_left} liters"

# print(water_left(5, 100, 2))

# def water_left(astronauts, water_left, days_left):
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     if total_water_left < 0:
#         raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
#     return f"Total water left after {days_left} days is: {total_water_left} liters"

# print(water_left(5, 100, 2))

# try:
#     print(water_left(5, 100, 2))
# except RuntimeError as err:
#     alert_navigation_system(err)


def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print(water_left("3", "200", None))
#---------------------------------------------------------------------------------------------------------