import phonenumbers
from phonenumbers import geocoder, carrier, phonenumberutil, timezone


title = """
 ###                      ######                              
 #  #    # ######  ####  #     # #    #  ####  #    # ###### 
 #  ##   # #      #    # #     # #    # #    # ##   # #      
 #  # #  # #####  #    # ######  ###### #    # # #  # #####  
 #  #  # # #      #    # #       #    # #    # #  # # #      
 #  #   ## #      #    # #       #    # #    # #   ## #      
### #    # #       ####  #       #    #  ####  #    # ###### 
                                                   
"""
 
print("___________________________________________________________________")

print("\033[1;31;40m" + title + "\033[m")
print("___________________________________________________________________")
print("\n")
print("_________________________________________________")
print("\033[1;32;40m⌬ Extractor de detalles de números de teléfono📞\n\n⌖Canal De Telegram: t.me/BoxPrey\n⌖BY: @PreBoyx \033[m")
print("_________________________________________________")
print("\n")

print("\033[1;32;40m ⌬ Recuerda Ingresar el numero de teléfono con el prefijo del pais\033[m ")


phone_number = input("\033[1;32;40m ⌬ Por favor ingrese el número de teléfono aqui :  \033[m")

try:
    number = phonenumbers.parse(phone_number, None)
    country_code = phonenumbers.region_code_for_number(number)
    location = geocoder.description_for_number(number, "en")
    carrier_name = carrier.name_for_number(number, "en") if carrier.name_for_number(number, "en") else "Unknown Carrier"
    
    number_type = phonenumberutil.number_type(number)
    number_type_description = "Mobile" if number_type == phonenumberutil.PhoneNumberType.MOBILE else (
        "Fixed-line" if number_type == phonenumberutil.PhoneNumberType.FIXED_LINE else (
            "Toll-free" if number_type == phonenumberutil.PhoneNumberType.TOLL_FREE else (
                "Premium rate" if number_type == phonenumberutil.PhoneNumberType.PREMIUM_RATE else (
                    "Shared cost" if number_type == phonenumberutil.PhoneNumberType.SHARED_COST else (
                        "VOIP" if number_type == phonenumberutil.PhoneNumberType.VOIP else "Other"
                    )
                )
            )
        )
    )
    
    validity = "Valid" if phonenumbers.is_valid_number(number) else "Invalid"
    formatted_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    possible_lengths = [len(str(number)) for number in phonenumbers.PhoneNumberMatcher(phone_number, "ZZ")]
    possible_lengths_description = f"Possible lengths: {', '.join(str(length) for length in possible_lengths)}"
    country_name = geocoder.country_name_for_number(number, "en")
    is_possible = "Possible" if phonenumbers.is_possible_number(number) else "Not possible"
    
    time_zones = timezone.time_zones_for_number(number)
    time_zones_description = f"Time Zones: {', '.join(time_zones)}" if time_zones else "Time zone information not available"
    
    national_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
    extension = number.extension if number.extension else "No extension"

    latitude, longitude = None, None
    administrative_area = None
    possible_geocoding = None
    

    if location != "Unknown":
        info = geocoder.description_for_number(number, "en", region=None)
        location_info = info.split(', ')
        if len(location_info) >= 2:
            latitude, longitude = location_info[-1].split('/')
            administrative_area = location_info[-2]
            possible_geocoding = geocoder.description_for_number(number, "en", region='US')

    is_possible_emergency_number = "Yes" if phonenumbers.is_possible_number_for_type(number, "001") else "No"


    if hasattr(carrier, 'name_for_number'):
        carrier_name = carrier.name_for_number(number, "en") or "Unknown Carrier"
    else:
        carrier_name = "Carrier information not available"


    valid_in_region = phonenumbers.is_valid_number_for_region(number, country_code)
    is_possible_number_type = "Possible" if phonenumbers.is_possible_number_for_type(number, "MOBILE") else "Not possible"
    is_possible_short_code = "Possible" if phonenumbers.is_possible_short_number(number) else "Not possible"
    is_valid_number_in_region = "Valid" if phonenumbers.is_valid_number_for_region(number, country_code) else "Not valid"
    

    time_zone_name = None
    if len(time_zones) > 0:
        time_zone_info = timezone.time_zones_for_number(number)
        if time_zone_info:
            time_zone_name = ', '.join(time_zone_info)


    possible_lengths = len(phonenumbers.PhoneNumberMatcher(phone_number, "ZZ").next().raw_string)
    national_significant_number = phonenumbers.national_significant_number(number)
    e164_format = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
    rfc3966_format = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.RFC3966)
    possible_types = str(number_type)

    details = {
        "◈Código de País": country_code,
        "◈Nombre del País": country_name,
        "◈Ubicación": location,
        "◈Latitud": latitude,
        "◈Longitud": longitude,
        "◈Área Administrativa": administrative_area,
        "◈Posible Geocodificación (EE. UU.)": possible_geocoding,
        "◈Nombre de la SIM": carrier_name,
        "◈Tipo de Número": number_type_description,
        "◈Validez": validity,
        "◈Válido en la Región": valid_in_region,
        "◈Número Formateado": formatted_number,
        "◈Longitudes Posibles": possible_lengths_description,
        "◈Es posible número": is_possible,
        "◈Número Nacional": national_number,
        "◈Extensión": extension,
        "◈Posible número de emergencia": is_possible_emergency_number,
        "◈Posible número de móvil": is_possible_number_type,
        "◈Posible código corto": is_possible_short_code,
        "◈Número válido en la región": is_valid_number_in_region,
        "◈Nombre de zona horaria": time_zone_name,
        "◈Longitudes posibles": possible_lengths,
        "◈Número Nacional Significativo": national_significant_number,
        "◈Formato E164": e164_format,
        "◈Formato RFC3966": rfc3966_format,
        "◈Tipos Posibles": possible_types
    }
    
    print("\n\n🌐 Detalles del número de teléfono📞")
    for key, value in details.items():
        print(f"{key}: {value}")
        
except phonenumbers.phonenumberutil.NumberParseException as e:
    print("❌ No se pudo analizar el número:", e)
