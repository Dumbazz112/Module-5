


if __name__ == "__main__":
    
    # colors = ('red', 'yellow', 'blue', 'green')
    # colors = list(colors)
    # print(type(colors))
    # print(colors)
    
    
    # hello_list = list('hello there')
    # print(hello_list)
    
    # my_tuple = (1, 2, 3)
    # print(my_tuple)
    # my_list = list(my_tuple)
    # print(my_list)
    
    # for elem in my_list:
    #     print(elem)

    #REPLACING IN LIST
    # colors[0] = 'cyan'
    # print(colors)
    
    #SORTING
    # colors.sort()
    # print(colors)
    
    #APPENDING - ADDING TO LIST
    # colors.append('red')
    # print(colors)
    
    # numbers = []
    # print(type(numbers))
    # for i in range(5):
    #     numbers.append(i ** 2)
        
    # print(numbers)
    
    #POP - Removing last number
    
    # numbers.pop()
    # print(numbers)
    
    #COMBINDING
    # first = list(range(5))
    # second = list(range(5,10))
    # combined = first + second
    # print(first)
    # print(second)
    # print(combined)
    
    # print(max(combined))
    # print(min(combined))
    # print(sum(combined))
    
    # total = 0
    # for i in combined:
    #     total += i
        
    # print(total)
    
    #SPLITTING
    pokemon = 'pikachu,bulbasaur,charmander'
    my_pokemon = pokemon.split(',')
    print(my_pokemon)
    
    pokedex = my_pokemon[:]
    print(pokedex)
    print(my_pokemon)
    
    pokedex.append('mew')
    
    print(pokedex)
    print(my_pokemon)