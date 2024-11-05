# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:50:26 2024
"""
from datetime import datetime
from geopy.geocoders import Nominatim  
import requests

# déterminer l'hémisphère de la ville 
def determiner_hemisphere(ville):
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(ville)
    if location.latitude > 0:
        return 'nord'
    else :
        return 'sud'
    
# déterminer la saison en fonction de l'hémisphère
def determiner_saison(ville):
    # obtenir la date actuelle
    date_actuelle = datetime.now()
    mois_ville = date_actuelle.month
    hemisphere = determiner_hemisphere(ville)
    print(f'la ville de {ville} se trouve dans l\'hémisphère {hemisphere}')
    if hemisphere == 'nord':
        if 3 <= mois_ville <= 5 :
            saison = 'Printemps'
        elif 6 <= mois_ville <= 8:
            saison ='Eté'
        elif 9 <= mois_ville <= 11:
            saison ='Automne'
        else:
            saison ='Hiver'
    else :                   # hémisphere sud
        if 3 <= mois_ville <= 5:
           saison ="Automne"
        elif 6 <= mois_ville <= 8:
           saison  ="Hiver"
        elif 9 <= mois_ville <= 11:
            saison = "Printemps"
        else:
           saison ="Été"
    return saison


# 4) Génération aléatoire de météo &  5) Affichage du bulletin meteo

def determiner_meteo(ville, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={ville}&appid={api_key}&units=metric&lang=fr"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        wind_speed = wind["speed"]
        
        bulletin = (f"Bulletin météo pour {ville}:\n"
                    f"Température: {temp}°C\n"
                    f"Pression: {pressure} hPa\n"
                    f"Humidité: {humidity}%\n"
                    f"Conditions: {description}\n"
                    f"Vitesse du vent: {wind_speed} m/s")
        return bulletin
    else:
        return f"Ville {ville} non trouvée."

        
if __name__ == '__main__':
    ville = input('Entrez le nom de la ville : ' )
    api_key = "48e05aba61a3ae06ac003e32066b289d"
    determiner_meteo(ville, api_key)
    saison = determiner_saison(ville)
    print('la ville de {ville} se trouve en {saison}')
   
    
determiner_saison('quito')

