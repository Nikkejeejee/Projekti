
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
        country = player_location['Country']  # Define 'country' here
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

        # Rest of the code remains the same
