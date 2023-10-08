import mysql.connector
import random

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='p3',
    user='root',
    password='sunmuts1s',  # Add your database password here
    autocommit=True
)

# Define functions to fetch data from the database
def fetch_nostalgic_foods():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Foodlist FROM food ORDER BY RAND() LIMIT %s", (random.randint(2, 5),))
    result = cursor.fetchall()
    return [row['Foodlist'] for row in result]

def fetch_places():
    sql = """SELECT Lyhenne AS Country_Code, Country_Name AS Country, Airport FROM places;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def fetch_food(country):
    sql = f"""SELECT Lyhenne AS Country_Code, Country_Name AS Country, Foodlist, Cost FROM food WHERE Country_Name = '{country}';"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    food_list = [row['Foodlist'] for row in result]
    return food_list

def fetch_work():
    sql = """SELECT work_places FROM work;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    work_list = [row['work_places'] for row in result]
    return work_list

def fetch_event():
    sql = """SELECT Satunnaiset_tapahtumat FROM event""";
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    event_list = [row['Satunnaiset_tapahtumat'] for row in result]
    return event_list

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

# Pelin intro
print("████████ ███████ ██████  ██    ██ ███████ ████████ ██    ██ ██       ██████   █████  ")
print("   ██    ██      ██   ██ ██    ██ ██         ██    ██    ██ ██      ██    ██ ██   ██ ")
print("   ██    █████   ██████  ██    ██ █████      ██    ██    ██ ██      ██    ██ ███████ ")
print("   ██    ██      ██   ██  ██  ██  ██         ██    ██    ██ ██      ██    ██ ██   ██ ")
print("   ██    ███████ ██   ██   ████   ███████    ██     ██████  ███████  ██████  ██   ██ ")
print("...nostalgiseen ruokapeliin! ")

rules_ans = input("\nHaluatko käydä läpi pelin säännöt? Kyllä/Ei: ")

if rules_ans.lower() == "kyllä":
    intro_text = f" ZZUPP {username}! Oletko valmis pelaamaan nostalgia ruokapeliä?\n" \
                 "\n Olet sairas.\n" \
                 "\n Kyllä luit oikein. Olet sairas.\n" \
                 "\n Sairastat tautia nimeltään ₘᵤᵢₛₜᵢₖₘₐₖᵤₜₐᵤₜᵢ.\n" \
                 f" Hyvä asia on kuitenkin se, että olet voittanut {initial_tickets} lentolippua. \n" \
                 "\n ┌( ಠ_ಠ )┘  WOOOHOOOO  ₍₍ ◝(・ω・)◟ ⁾⁾ \n" \
                 "\n Haluat syödä nostalgista ruokaa ennen kuin sairaus syö sinut. \n" \
                 " Matkustat siis ympäri maailmaa syödäksesi nämä ruuat."
else:
    print("Ladataan peliä...")

# Pelin alussa kysyy nimeä ja vaikeustasoa

# Vaikeustason koodi
EASY = 1
MEDIUM = 2
HARD = 3

username = input("Syötä pelaaja nimesi: ")

while True:
    try:
        difficulty_level = int(input("Syötä vaikeustaso (1 = helppo / 2 = keskivaikea / 3 = vaikea): "))
        if difficulty_level in (EASY, MEDIUM, HARD):
            break
        else:
            print("Virheellinen vaikeustaso. Valitse 1, 2 tai 3.")
    except ValueError:
        print("Virheellinen syöte. Anna kokonaisluku (1/2/3).")

# Minimi- ja maksimimäärä lippuja vaikeustason mukaan
if difficulty_level == EASY:
    tickets = random.randint(7, 10)
elif difficulty_level == MEDIUM:
    tickets = random.randint(5, 7)
elif difficulty_level == HARD:
    tickets = random.randint(3, 5)
else:
    # Oletusasetus on EASY, jos vaikeustaso on virheellinen
    min_tickets = 7
    max_tickets = 10

# Vaikeustaso ja lentolippujen määrä
initial_tickets = tickets * 2 + 1
print(f"\nValitsit vaikeustason {difficulty_level}. Sinulla on alussa {initial_tickets} lentolippua.")

intro_text = f" ZZUPP {username}! Oletko valmis pelaamaan nostalgia ruokapeliä?\n"\
             "\n Olet sairas.\n"\
             "\n Kyllä luit oikein. Olet sairas.\n"\
             "\n Sairastat tautia nimeltään muistimakutauti.\n"\
             f" Hyvä asia on kuitenkin se, että olet voittanut {initial_tickets} lentolippua. \n"\
             " Haluat syödä nostalgista ruokaa ennen kuin sairaus syö sinut. \n"\
             " Matkustat siis ympäri maailmaa syödäksesi nämä ruuat."
print(bordered(intro_text))

places = fetch_places()
player_location = random.choice(places)
money = 50

input("Paina Enter jatkaaksesi...")
print(f"Tervetuloa! Aloituspaikkasi on {player_location['Airport']} ({player_location['Country']}).")
print(f"Rahasi: {money}€")
print("\nTässä ovat nostalgiset ruokasi:")

nostalgic_foods = fetch_nostalgic_foods()
for i, food in enumerate(nostalgic_foods, start=1):
    print(f"{i}. {food}")

nostalgic_foods_eaten = []

# Tauotus
input("\nPaina Enter jatkaaksesi...")

# Pelilööppi
while initial_tickets > 0:
    input("\nTutkitaan lentokenttää... Paina Enter jatkaaksesi.")
    satunnainen_tapahtuma = random.randint(1, 2)
    if satunnainen_tapahtuma == 1:
        events = fetch_event()
        print("Tapahtuma: " + random.choice(events))
        input("\nPaina Enter jatkaaksesi...")
    elif satunnainen_tapahtuma == 2:
        print("Tutkit lentokenttää mutta et löytänyt mitään erikoista.")
        input("\nPaina Enter jatkaaksesi...")

    input("\nEtsitään töitä ja ruokapaikkoja... Paina Enter jatkaaksesi...")
    print("\nMitä haluaisit tehdä?")
    print("1. Syö ravintolassa")
    print("2. Etsi työtä")
    print("3. Matkusta uuteen lentokenttään")
    print("4. Lopeta peli")

    choice = input("\nValintasi (1/2/3/4): ")

    if choice == "1":
        # Pelaaja haluaa syödä
        country = player_location['Country']
        food_list = fetch_food(country)

        if len(food_list) >= 2:
            # Valitsee 1-2 maan ruoat
            max_nostalgic_foods = min(len(food_list), 2)
            chosen_foods = random.sample(food_list, random.randint(1, max_nostalgic_foods))
        else:
            chosen_foods = food_list

        # Valitsee ruokavaihtoehdot
        other_countries = [place['Country'] for place in places if place['Country'] != country]
        random_country = random.choice(other_countries)
        other_food_list = fetch_food(random_country)
        chosen_foods.extend(random.sample(other_food_list, random.randint(1, 2)))

        print("\nValitse ruoka, jota syöt:")
        for i, food in enumerate(chosen_foods, start=1):
            print(f"{i}. {food}")

        food_choice = int(input("\nAnna numerosi: "))
        selected_food = chosen_foods[food_choice - 1]

        print(f"Valitsit syödä: {selected_food}")
        input("\nMatkusta seuraavalle kentälle jatkaaksesi... (paina enter)")
        random_places = random.sample(places, random.randint(3, min(5, len(places))))
        print("Valitse seuraava lentokenttä:")
        for i, place in enumerate(random_places, start=1):
            print(f"{i}. {place['Airport']} ({place['Country']})")

        travel_choice = input("Valintasi (1/2/.../n): ")
        try:
            travel_choice = int(travel_choice)
            if 1 <= travel_choice <= len(random_places):
                player_location = random_places[travel_choice - 1]
                print(f"Saavuit lentokentälle {player_location['Airport']} ({player_location['Country']}).")
            else:
                print("Virheellinen valinta.")
        except ValueError:
            print("Virheellinen syöte.")

        # Vähentää lippumäärän
        initial_tickets -= 1

    elif choice == "2":
        # Pelaaja haluaa tehdä töitä
        work_list = fetch_work()

        if len(work_list) >= 2:
            chosen_jobs = random.sample(work_list, 2)
        else:
            chosen_jobs = work_list

        print("Valitut työvaihtoehdot:")
        for i, job in enumerate(chosen_jobs, start=1):
            print(f"{i}. {job}")

        job_choice = input("Valitse työ (1/2): ")

        if job_choice == "1":
            print("Teet työtä 1.")
        elif job_choice == "2":
            print("Teet työtä 2.")

        input("\nMatkusta seuraavalle kentälle jatkaaksesi... (paina enter)")
        random_places = random.sample(places, random.randint(3, min(5, len(places))))
        print("Valitse seuraava lentokenttä:")
        for i, place in enumerate(random_places, start=1):
            print(f"{i}. {place['Airport']} ({place['Country']})")

        travel_choice = input("Valintasi (1/2/.../n): ")
        try:
            travel_choice = int(travel_choice)
            if 1 <= travel_choice <= len(random_places):
                player_location = random_places[travel_choice - 1]
                print(f"Saavuit lentokentälle {player_location['Airport']} ({player_location['Country']}).")
            else:
                print("Virheellinen valinta.")
        except ValueError:
            print("Virheellinen syöte.")

    elif choice == "3":
        # Pelaaja matkustaa toiseen lentokenttään
        input("\nMatkusta seuraavalle kentälle jatkaaksesi... (paina enter)")
        random_places = random.sample(places, random.randint(3, min(5, len(places))))
        print("Valitse seuraava lentokenttä:")
        for i, place in enumerate(random_places, start=1):
            print(f"{i}. {place['Airport']} ({place['Country']})")

        travel_choice = input("Valintasi (1/2/.../n): ")
        try:
            travel_choice = int(travel_choice)
            if 1 <= travel_choice <= len(random_places):
                player_location = random_places[travel_choice - 1]
                print(f"Saavuit lentokentälle {player_location['Airport']} ({player_location['Country']}).")
            else:
                print("Virheellinen valinta.")
        except ValueError:
            print("Virheellinen syöte.")

    elif choice == "4":
        # Pelaaja lopettaa pelin
        print("Kiitos pelaamisesta!")
        break

    else:
        print("Virheellinen valinta. Valitse 1, 2, 3 tai 4.")
