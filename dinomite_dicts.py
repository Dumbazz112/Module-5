

if __name__ == "__main__":
    
    pokedex = {
        'Venosaur': ['grass','poison'],
        'Charizard': ['flying','fire'],
        'Blastoise': 'water'
    }
    
    print(pokedex)
    
    del pokedex['Blastoise']
    
    print(pokedex)