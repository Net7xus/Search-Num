import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import os

os.system("clear")
print("        \033[1;37m ____   ____")
print("        /  _ \ / _  \ ")
print("        | |_) | (_| |")
print("        |_.__  ___,_|")
print("             | |")
print("     __      (_)      __")
print("    /  \_____| |_____/  \ ")
print("    |   |||||||||||||   |")
print("     \                 /")
print("")
print("   \033[1;31m==>[\033[1;33mCode by: \033[1;37mNet7xus\033[1;31m]<==")
print("")
def obtener_informacion(numero):
    try:
        numero = phonenumbers.parse(numero)
        
        internacional = phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nacional = phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.E164)
        
        ubicacion = geocoder.description_for_number(numero, 'es')
        operador = carrier.name_for_number(numero, 'es')
        zona_horaria = timezone.time_zones_for_number(numero)
        
        print("")
        os.system("sleep 2")
        print("\033[1;32m------------------------------------") 
        print("Información del número:")
        print("------------------------------------")
        print("Número Internacional:", internacional)
        print("Número Nacional:", nacional)
        print("Número E164:", e164)
        print("Ubicación:", ubicacion)
        print("Operador:", operador)
        print("Zona horaria:", zona_horaria)
        
    except phonenumbers.phonenumberutil.NumberParseException:
        print("\033[1;31mEl número ingresado no es válido.")


numero_telefono = input("\033[1;33m[+]Número de tlf (+57): \033[1;37m")
obtener_informacion(numero_telefono)
