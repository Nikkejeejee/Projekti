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
    # Default to EASY if difficulty level is invalid
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
