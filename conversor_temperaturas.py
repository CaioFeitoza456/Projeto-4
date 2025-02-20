
def celsius_para_kelvin(temperatura):
    # CELSIUS PARA KELVIN
    resultado = temperatura + 273.15
    return resultado


def celsius_para_fahrenheit(temperatura):
    # CELSIUS PARA FAHRENHEIT
    resultado = temperatura * 9 / 5 + 32
    return resultado 


def fahrenheit_para_celsius(temperatura):
    # FAHRENHEIT PARA CELSIUS
    resultado = (temperatura - 32) * 5 / 9
    return resultado


def fahrenheit_para_kelvin(temperatura):
    # FAHRENHEIT PARA KELVIN
    resultado = (temperatura - 32) * 5 / 9 + 273.15
    return resultado


def kelvin_para_celsius(temperatura):
    # KELVIN PARA CELSIUS
    resultado = temperatura - 273.15
    return resultado


def kelvin_para_fahrenheit(temperatura):
    # KELVIN PARA FAHRENHEIT
    resultado = (temperatura - 273.15) * 9 / 5 + 32
    return resultado
