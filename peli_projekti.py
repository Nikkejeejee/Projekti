import mysql.connector
import random

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='projekti',
    user='root',
    password='3965',
    autocommit=True
)


def paikat():
    sql = """SELECT Country, Airport FROM places;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def ruoka():
    sql = """SELECT Country, Foodlist FROM food;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    country_list = [row['Country'] for row in result]
    food_list = [row['Foodlist'] for row in result]
    return country_list, food_list

def tarina():
    story = ("Tervehdys, vaeltaja! Tehtävänäsi on pelastaa maailma ruokalajien kadolta!"
             " Sinulla on taito oppia valmistamaan mitä tahansa ruokalajeja pelkästään syömällä niitä kerran!"
             )
    return story

def pelinpituus():
    pituus = "none"
    while pituus not in ("10", "20", "30"):
        pituus = input(f"Kuinka monta ruokaa haluat etsiä? (10, 20, 30)")
        if pituus in ("10", "20", "30"):
            print(f"Pituus valittu!")
            return pituus
        else:
            print("Tuntematon arvo! Anna yksi mainituista numeroista.")

def difficulty():
    if Goal == "10":
        return "Vaikeustaso: helppo"
    elif Goal == "20":
        return "Vaikeustaso: Normaali"
    elif Goal == "30":
        return "Vaikeustaso: Vaikea"
    else:
        print("Goal error?!")

introduction = tarina()
print(introduction)
Goal = pelinpituus()
print(f"- Vaikeustaso: Helppo" if Goal == "10" else "- Vaikeustaso: Normaali" if Goal == "20" else "- Vaikeustaso: Vaikea")
print("Ladataan peliä...")
print("████████ ███████ ██████  ██    ██ ███████ ████████ ██    ██ ██       ██████   █████  ")
print("   ██    ██      ██   ██ ██    ██ ██         ██    ██    ██ ██      ██    ██ ██   ██ ")
print("   ██    █████   ██████  ██    ██ █████      ██    ██    ██ ██      ██    ██ ███████ ")
print("   ██    ██      ██   ██  ██  ██  ██         ██    ██    ██ ██      ██    ██ ██   ██ ")
print("   ██    ███████ ██   ██   ████   ███████    ██     ██████  ███████  ██████  ██   ██ ")
print("")
print(f"- Syötävien ruokien määrä: {Goal}!")

sijainnit = paikat()
alkupaikka = sijainnit[random.randint(0, 29)]
money = 50
energy = 7
print(f"Aloituspaikkasi on: {alkupaikka})")

ruoat = ruoka()
alkuruoka = ruoat[random.randint(0, 29)]
print(f"testiruokasi on {alkuruoka}")