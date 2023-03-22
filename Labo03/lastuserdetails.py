#!/usr/bin/python3
# Voer het commando uit om de laatste gebruiker uit /etc/passwd te halen
last_user = subprocess.check_output("tail -n 1 /etc/passwd", shell=True)
last_user = last_user.decode("utf-8").strip()

# Splits de gebruikersinformatie in afzonderlijke velden
last_user_fields = last_user.split(":")

# Haal de gewenste informatie uit de velden
username = last_user_fields[0]
userid = last_user_fields[2]
home_dir = last_user_fields[5]

# Print de gebruikersinformatie
print("Gebruikersnaam: ", username)
print("User ID: ", userid)
print("Home directory: ", home_dir)
