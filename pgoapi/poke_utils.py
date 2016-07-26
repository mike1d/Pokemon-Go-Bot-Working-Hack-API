import os

def pokemonIVPercentage(pokemon):
    return ((pokemon.get('individual_attack', 0) + pokemon.get('individual_stamina', 0) + pokemon.get(
        'individual_defense', 0) + 0.0) / 45.0) * 100.0

def get_pokemon_num(res):
    inventory_delta = res['responses']['GET_INVENTORY'].get('inventory_delta', {})
    inventory_items = inventory_delta.get('inventory_items', [])
    inventory_items_dict_list = map(lambda x: x.get('inventory_item_data', {}), inventory_items)
    inventory_items_pokemon_list = filter(lambda x: 'pokemon_data' in x and 'is_egg' not in x['pokemon_data'], inventory_items_dict_list)
    return len(inventory_items_pokemon_list)

def get_inventory_data(res, poke_names):
    inventory_delta = res['responses']['GET_INVENTORY'].get('inventory_delta', {}) 
    inventory_items = inventory_delta.get('inventory_items', []) 
    inventory_items_dict_list = map(lambda x: x.get('inventory_item_data', {}), inventory_items)
    inventory_items_pokemon_list = filter(lambda x: 'pokemon_data' in x and 'is_egg' not in x['pokemon_data'],
                                          inventory_items_dict_list)
    inventory_items_pokemon_list_sorted = sorted(inventory_items_pokemon_list, key=lambda x: poke_names[str(x['pokemon_data']['pokemon_id'])].encode('ascii', 'ignore'))

    inventory_items_pokemon_list_sorted = sorted(
        inventory_items_pokemon_list,
        key=lambda pokemon: pokemon['pokemon_data']['cp']
    )   
    return (os.linesep.join(map(lambda x: "{0}, CP {1}, IV {2:.2f}".format(
        poke_names[str(x['pokemon_data']['pokemon_id'])].encode('ascii', 'ignore'),
        x['pokemon_data']['cp'],
<<<<<<< HEAD
        pokemonIVPercentage(x['pokemon_data'])), inventory_items_pokemon_list_sorted)))
=======
        pokemonIVPercentage(x['pokemon_data'])), inventory_items_pokemon_list)))

def get_inventory_candy(res, poke_names):
    inventory_delta = res['responses']['GET_INVENTORY'].get('inventory_delta', {})
    inventory_items = inventory_delta.get('inventory_items', [])
    inventory_items_dict_list = map(lambda x: x.get('inventory_item_data', {}), inventory_items)
    inventory_items_family_list = filter(lambda x: 'pokemon_family' in x,
                                          inventory_items_dict_list)

    return (os.linesep.join(map(lambda x: "{0}, candy {1}".format(
        poke_names[str(x['pokemon_family']['family_id'])].encode('ascii', 'ignore'),
        x['pokemon_family']['candy']), inventory_items_family_list)))
>>>>>>> 0e08b51ca4ea20cf5f17a0f0d7b1495766761eeb
