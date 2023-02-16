

if __name__ == "__main__":
    
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    #WHILE LOOP
    # i = 0
    # while i < len(vowels):
    #     print(vowels[i])
    
    #FOR LOOP
    # for letter in vowels:
    #     print(letter)
        
    #RANGE
    # for i in range(10, 21, 2):
    #     print(i)
        
    #NESTING
    for i in range(5):
        print('pre nested loop')
        for j in range(5,8):
            print(f'i = {i}; j = {j}')
        
        print ('script complete')