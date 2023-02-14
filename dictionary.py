

if __name__ == "__main__":
    
    pokemon_types = {
        #KEY     :   VALUE
        'Pikachu': 'electric',
        'Bulbasaur': 'grass',
        'Charmander': 'fire'
    }
    
    # print(pokemon_types)
    
    # pokemon_type_pair = (
    #     ('Pikachu', 'electric'),
    #     ('Bulbasaur', 'grass'),
    #     ('Charmander', 'fire')
    # )
    
    # print(pokemon_type_pair)
    
    # pokemon_type_pair_tuple = dict(pokemon_type_pair)
    # # print(pokemon_type_pair_tuple)
    
    #GETTING DEFINITION OF VALUE
    # print(pokemon_types['Pikachu'])
    # print(pokemon_types.get('Pikachu'))
    
    # print(pokemon_types.get['Pikachu', 'Unknown'])
    
    #ADDING
    
    pokemon_types['Mew'] = 'pyschic'
    pokemon_types['Squritle'] = 'water'
    # print(pokemon_types)
    
    #DELETING
    # del pokemon_types['Squritle']
    # print(pokemon_types)
    
    # for key in pokemon_types.keys():
        # print(key)
        
    # for item in pokemon_types.items():
        # print(item)
        
    # for key, value in pokemon_types.items():
        # print(f'Pokemon {key} is of type {value}')
        
    pokedex = {
        25: {
            'name': 'Pikachu',
            'type': 'electric'
        },
        1: {
            'name': 'Blubasaur',
            'type': 'grass'
        },
        4: {
            'name': 'Charmander',
            'type': 'fire'
        }
    }
        
    # print(pokedex)
    print(pokedex[25]['name'])