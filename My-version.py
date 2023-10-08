import mysql.connector
import random

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='projekti',
    user='root',
    password='sunmuts1s',
    autocommit=True
)

# Funktioiden määritelmät, joita on otettu tietokannalta
def fetch_nostalgic_foods():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Foodlist FROM food ORDER BY RAND() LIMIT %s", (random.randint(2, 5),))
    result = cursor.fetchall()
    return [row['Foodlist'] for row in result]

def fetch_places():
    sql = """SELECT Airport, Country FROM places;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def fetch_food(country):
    sql = f"""SELECT Foodlist FROM food WHERE Country = '{country}';"""
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
print("...nostalgiseen ruokapeliin!")

rules_ans = input("\nHaluatko käydä läpi pelin säännöt? Kyllä/Ei: ")

if rules_ans.lower() == "kyllä":
    rules = (" Sinulle annetaan vaikeustason mukaan tietty määrä lentolippuja.\n"
             " Pelin alussa sinulle kerrotaan nostalgiset ruuat, joita sinun tulee syödä.\n"
             " Kuolet, kun et saa syötyä nostalgisia ruokiasi ja/tai lentolippu on loppuun käytetty. ")
    print(bordered(rules))
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
        difficulty_level = int(input("Syötä vaikeustaso (1/2/3): "))
        if difficulty_level in (EASY, MEDIUM, HARD):
            break
        else:
            print("Virheellinen vaikeustaso. Valitse 1, 2 tai 3.")
    except ValueError:
        print("Virheellinen syöte. Anna kokonaisluku (1/2/3).")

# Minimi- ja maksimimäärä lippuja vaikeustason mukaan
if difficulty_level == EASY:
    min_tickets = 7
    max_tickets = 10
elif difficulty_level == MEDIUM:
    min_tickets = 5
    max_tickets = 7
elif difficulty_level == HARD:
    min_tickets = 3
    max_tickets = 5
else:
    # Oletusasetus on EASY, jos vaikeustaso on virheellinen
    min_tickets = 7
    max_tickets = 10

# Vaikeustaso ja lentolippujen määrä
initial_tickets = difficulty_level * 2 + 1
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

input("\nPaina Enter jatkaaksesi...")
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
            chosen_foods = random.sample(food_list, random.randint(1, 2))
        else:
            chosen_foods = food_list

        # Valitsee ruokavaihtoehdot
        other_countries = [place['Country'] for place in places if place['Country'] != country]
        random_country = random.choice(other_countries)
        other_food_list = fetch_food(random_country)
        chosen_foods.extend(random.sample(other_food_list, random.randint(1, 2)))

        print(f"Valitse ruoka, jota syöt: {', '.join(chosen_foods)}")

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

        # Vähentää lippumäärän
        initial_tickets -= 1

    elif choice == "3":
        # Pelaaja matkustaa toiseen lentokenttään
        print("Valitse seuraava lentokenttä:")
        for i, place in enumerate(places, start=1):
            print(f"{i}. {place['Airport']} ({place['Country']})")

        travel_choice = input("Valintasi (1/2/.../n): ")
        try:
            travel_choice = int(travel_choice)
            if 1 <= travel_choice <= len(places):
                player_location = places[travel_choice - 1]
                print(f"Saavuit lentokentälle {player_location['Airport']} ({player_location['Country']}).")
            else:
                print("Virheellinen valinta.")
        except ValueError:
            print("Virheellinen syöte.")

        # Vähentää lippumäärän
        initial_tickets -= 1

    elif choice == "4":
        # Pelaaja lopettaa pelin
        print("Kiitos pelaamisesta!")
        break

    else:
        print("Virheellinen valinta. Valitse 1, 2, 3 tai 4.")
