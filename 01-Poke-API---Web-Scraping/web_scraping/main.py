import requests
import pandas as pd
from tqdm import tqdm
import time

# Função para obter dados de um Pokémon específico da PokeAPI
def get_pokemon_data(pokemon_name):
    try:
        # Endpoint principal do Pokémon
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(api_url, timeout=10)

        if response.status_code != 200:
            return None

        poke_data = response.json()

        # Extração de dados
        number = poke_data.get('id')
        name = poke_data.get('name')
        types = [t['type']['name'].capitalize() for t in poke_data.get('types', [])]
        type_1 = types[0] if len(types) >= 1 else None
        type_2 = types[1] if len(types) >= 2 else None
        height = poke_data.get('height')
        weight = poke_data.get('weight')
        category = poke_data.get('species', {}).get('name')
        abilities = [a['ability']['name'] for a in poke_data.get('abilities', [])]

        # Dados adicionais via species
        habitat = color = evolution_chain = None
        is_legendary = is_mythical = False

        species_url = poke_data.get('species', {}).get('url')
        if species_url:
            species_response = requests.get(species_url, timeout=10)
            if species_response.status_code == 200:
                species_data = species_response.json()

                habitat_data = species_data.get('habitat')
                habitat = habitat_data.get('name') if habitat_data else None

                color_data = species_data.get('color')
                color = color_data.get('name') if color_data else None

                is_legendary = species_data.get('is_legendary', False)
                is_mythical = species_data.get('is_mythical', False)

                evolution_data = species_data.get('evolution_chain')
                evolution_chain = evolution_data.get('url') if evolution_data else None

        return {
            'id': number,
            'name': name,
            'type_1': type_1,
            'type_2': type_2,
            'height': height,
            'weight': weight,
            'category': category,
            'abilities': abilities,
            'habitat': habitat,
            'color': color,
            'is_legendary': is_legendary,
            'is_mythical': is_mythical,
            'evolution_chain': evolution_chain
        }

    except Exception as e:
        print(f"Erro ao extrair dados de {pokemon_name}: {e}")
        return None


# Obter a lista de nomes de Pokémon
try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1200", timeout=10)
    response.raise_for_status()
    pokemon_names = [item['name'] for item in response.json()['results']]
except Exception as e:
    print(f"Erro ao obter lista de pokémons: {e}")
    pokemon_names = []

# Lista para armazenar os dados
pokemon_data_list = []

# Loop principal com tqdm
for idx, name in enumerate(tqdm(pokemon_names, desc="Coletando Pokémon Data"), start=1):
    data = get_pokemon_data(name)

    if data:
        pokemon_data_list.append(data)
        tqdm.write(f"{idx}/{len(pokemon_names)} - {name} - Data Retrieved!")
    else:
        tqdm.write(f"{idx}/{len(pokemon_names)} - {name} - Failed to retrieve")

    # Salvamento de backup a cada 100 Pokémon
    if idx % 100 == 0:
        pd.DataFrame(pokemon_data_list).to_csv('backup_pokemon.csv', index=False)
        print("Backup salvo em 'backup_pokemon.csv'")

    time.sleep(1)  # Espera para evitar rate limiting

# Salvamento final
df = pd.DataFrame(pokemon_data_list)
df.to_csv("pokemon_data.csv", index=False)
print("Todos os dados salvos em 'pokemon_data.csv'")
