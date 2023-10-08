import mysql.connector
import random

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='p3',
    user='root',
    password='sunmuts1s',  # LAITA TÄHÄN SALASANAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    autocommit=True
)

airplane = """                      
            ____
  |        | ___\          /~~~|
 _:_______|/'(..)`\_______/  | |
<_|``````  \__~~__/RYHMÄ G___|_|
  :\_____(=========,(*),--\__|_/
  |       \       /---'
           | (*) /
           |____/
"""
intro_banner = """
████████ ███████ ██████  ██    ██ ███████ ████████ ██    ██ ██       ██████   █████     ██
   ██    ██      ██   ██ ██    ██ ██         ██    ██    ██ ██      ██    ██ ██   ██    ██
   ██    █████   ██████  ██    ██ █████      ██    ██    ██ ██      ██    ██ ███████    ██
   ██    ██      ██   ██  ██  ██  ██         ██    ██    ██ ██      ██    ██ ██   ██ 
   ██    ███████ ██   ██   ████   ███████    ██     ██████  ███████  ██████  ██   ██    ██
"""
# Funktioiden määritelmät, joita on otettu tietokannalta
def fetch_nostalgic_foods():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Foodlist FROM food")
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


def fetch_foodprice(country):
    sql = f"""SELECT Cost FROM food WHERE Country = '{country}';"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    food_Cost = [row['Cost'] for row in result]
    return food_Cost


def fetch_work():
    sql = """SELECT work_places FROM work;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    work_list = [row['work_places'] for row in result]
    return work_list


def fetch_work_pay():
    sql = """SELECT Money_earned FROM work;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    money_list = [row['Money_earned'] for row in result]
    return money_list


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
print(intro_banner)
print("...nostalgiseen ruokapeliin! ")
print(airplane)

rules_ans = input("\nHaluatko käydä läpi pelin säännöt? Kyllä/Ei: ")

while rules_ans.lower() not in ["kyllä", "ei"]:
    print("Virheellinen syöte. Anna 'Kyllä' tai 'Ei'.")
    rules_ans = input("\nHaluatko käydä läpi pelin säännöt? Kyllä/Ei: ")

if rules_ans.lower() == "kyllä":
    rules = (" Sinulle annetaan vaikeustason mukaan tietty määrä lentolippuja.\n"
             " Pelin alussa sinulle kerrotaan nostalgiset ruuat, joita sinun tulee syödä.\n"
             " Kuolet, kun et saa syötyä nostalgisia ruokiasi ja/tai lentolippu on loppuun käytetty. ")
    print(bordered(rules))
else:
    print("𝐍𝐨𝐰 𝐥𝐨𝐚𝐝𝐢𝐧𝐠. . .(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")

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

# Vaikeustaso ja lentolippujen määrä
initial_tickets = tickets * 2 + 1
print(f"\n   Valitsit vaikeustason {difficulty_level}. Sinulla on alussa {initial_tickets} lentolippua.\n")

intro_text = f" ZZUPP {username}! Oletko valmis pelaamaan nostalgia ruokapeliä?\n" \
             "\n Olet sairas.\n" \
             "\n Kyllä luit oikein. Olet sairas.\n" \
             "\n Sairastat tautia nimeltään muistimakutauti.\n" \
             f" Hyvä asia on kuitenkin se, että olet voittanut {initial_tickets} lentolippua. \n" \
             " Haluat syödä nostalgista ruokaa ennen kuin sairaus syö sinut. \n" \
             " Matkustat siis ympäri maailmaa syödäksesi nämä ruuat."
print(bordered(intro_text))

places = fetch_places()
visited_places = []
game_won = False
player_location = random.choice(places)
money = 50

input("\nPaina 'Enter' aloittaaksesi pelin...(☉౪ ⊙)")
print("\nTässä ovat nostalgiset ruokasi:")

nostalgic_foods = fetch_nostalgic_foods()
foods = difficulty_level + 1
chosen_foods = random.sample(nostalgic_foods, foods)
nostalgiaruokalista = chosen_foods
for i, food in enumerate(chosen_foods, start=1):
    print(f"{i}. {food}")
print(f"- Aloituspaikkasi on {player_location['Airport']} ({player_location['Country']}). Sinulla on {money}€ -")

nostalgic_foods_eaten = set()
print("Peli alkaa!")
# Pelilööppi
while initial_tickets > 0:
    if nostalgic_foods_eaten == set(chosen_foods):
        game_won = True
        break
    print("\nEtsitään töitä ja ruokapaikkoja...")
    print("\nMitä haluaisit tehdä?")
    print("1. Syö ravintolassa")
    print("2. Työskentele")
    print("3. Tarkista tilanteesi")

    choice = input("\nValintasi (1/2/3): ")

    if choice == "1":
        # Pelaaja haluaa syödä
        country = player_location['Country']
        food_list = fetch_food(country)

        if len(food_list) >= 2:
            # Valitsee ruokavaihtoehdot
            ravintola_foods = []
            food_on_sale = random.randint(2, 3)
            food_sold = 0
            other_countries = [place['Country'] for place in places if place['Country'] == country]
            random_country = random.choice(other_countries)
            other_food_list = fetch_food(random_country)
            ravintola_foods.extend(random.sample(other_food_list, 1))
            while food_sold < food_on_sale:
                other_countries = [place['Country'] for place in places if place['Country'] != country]
                random_country = random.choice(other_countries)
                other_food_list = fetch_food(random_country)
                valittu_ruoka = random.choice(other_food_list)
                if valittu_ruoka not in ravintola_foods:
                    ravintola_foods.extend(random.sample(other_food_list, 1))
                    food_sold += 1
            ravintola_foods.append("Lähde syömättä")

        print("\nValitse ruoka, jota syöt:")
        for i, food in enumerate(ravintola_foods, start=1):
            print(f"{i}. {food}")

        food_choice = int(input("\nAnna numerosi: "))
        selected_food = ravintola_foods[food_choice - 1]
        if selected_food == "Lähde syömättä":
            print("Et syönyt mitään.")
        else:
            if selected_food in nostalgiaruokalista:
                nostalgic_foods_eaten.add(selected_food)
                if nostalgic_foods_eaten == set(chosen_foods):
                    game_won = True
                    break
            print(f"Valitsit syödä: {selected_food}")

        satunnainen_tapahtuma = random.randint(1, 3)
        if satunnainen_tapahtuma == 1:
            events = fetch_event()
            print("Syömisen jälkeen kohtasit satunnaisen tapahtuman!")
            print("Tapahtuma: " + random.choice(events))

        input("\nMatkusta seuraavalle kentälle jatkaaksesi... (paina enter)")
        random_places = random.sample([place for place in places if place not in visited_places], random.randint(3, min(5, len(places))))
        print("Valitse seuraava lentokenttä:")
        for i, place in enumerate(random_places, start=1):
            print(f"{i}. {place['Airport']} ({place['Country']})")

        travel_choice = input("Valintasi (1/2/.../n): ")
        try:
            travel_choice = int(travel_choice)
            if 1 <= travel_choice <= len(random_places):
                player_location = random_places[travel_choice - 1]
                print(f"Saavuit lentokentälle {player_location['Airport']} ({player_location['Country']}).")
                visited_places.append(player_location)
            else:
                print("Virheellinen valinta.")
        except ValueError:
            print("Virheellinen syöte.")

        # Vähentää lippumäärän
        initial_tickets -= 1

    elif choice == "2":
        # Pelaaja haluaa tehdä töitä
        work_list = fetch_work()
        money_list = fetch_work_pay()
        if len(work_list) >= 2:
            chosen_jobs_indices = random.sample(range(len(work_list)), 2)
        else:
            chosen_jobs_indices = list(range(len(work_list)))

        chosen_jobs = [work_list[i] for i in chosen_jobs_indices]
        chosen_money = [money_list[i] for i in chosen_jobs_indices]

        print("Valitut työvaihtoehdot:")
        for i, (job, money_earned) in enumerate(zip(chosen_jobs, chosen_money), start=1):
            print(f"{i}. {job} (Palkka: {money_earned}€)")

        job_choice = input("Valitse työ (1/2): ")

        if job_choice == "1":
            print("Työskenetelet...")
            money += chosen_money[0]
        elif job_choice == "2":
            print("Työskenetelet...")
            money += chosen_money[1]

        print(f"Ansaitsit rahaa! Sinulla on nyt yhteensä {money}€!")

        satunnainen_tapahtuma = random.randint(1, 3)
        if satunnainen_tapahtuma == 1:
            events = fetch_event()
            print("Tapahtuma: " + random.choice(events))

        input("\nMatkusta seuraavalle kentälle jatkaaksesi... (paina enter)")
        random_places = random.sample([place for place in places if place not in visited_places],
                                      random.randint(3, min(5, len(places))))
        print("Valitse seuraava lentokenttä:")
        for i, place in enumerate(random_places, start=1):
            print(f"{i}. {place['Airport']} ({place['Country']})")

        travel_choice = input("Valintasi (1/2/.../n): ")
        try:
            travel_choice = int(travel_choice)
            if 1 <= travel_choice <= len(random_places):
                player_location = random_places[travel_choice - 1]
                print(f"Saavuit lentokentälle {player_location['Airport']} ({player_location['Country']}).")
                visited_places.append(player_location)
            else:
                print("Virheellinen valinta.")
        except ValueError:
            print("Virheellinen syöte.")
    elif choice == "3":
        print("- Tämänhetkinen tilanteesi -")
        print("Ruoat jotka sinun täytyy syödä:")
        for i, food in enumerate(chosen_foods, start=1):
            print(f"{i}. {food}")
        print(f"Lippuja jäljellä: {initial_tickets}")
        print(f"Rahaa jäljellä: {money}")
        print(f"Nostalgisia ruokia syöty {nostalgic_foods_eaten}")

    else:
        print("Virheellinen valinta.")

if game_won:
    print("Voitit pelin, onneksi olkoon!")
else:
    print("Et löytänyt nostalgisia ruokiasi ajoissa... kuolit.")