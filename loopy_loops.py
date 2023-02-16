



if __name__ == "__main__":
    
    # pokemon = ('picachu','charmander','bulbasaur')
    # print(pokemon[1])
    
    # starter1 = pokemon[0]
    # starter2 = pokemon[1]
    # starter3 = pokemon[2]
    
    # print(starter1)
    # print(starter2)
    # print(starter3)
    
    # name1 = tuple('ROBERT')
    # indexi = name1.index('i')
    # indexi

    # for i in range (2, 10, ):
    #     print(i)
    
    # num_range = (2,10)
    # i = 0
    # while i < len(num_range):
    #     print(i)
    #     i += 1
        
    simple_string = 'This is a simple string'
    string_tuple = tuple(simple_string)
    
    # for letter in string_tuple:
    #     print(letter)
    
    for i in range(3):
        print('pre nested loop')
        for j in range(5,8):
            print(f'i = {i}; j = {j}')
        