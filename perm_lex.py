def perm_gen_lex(a):
    '''Generates all the permutations of the characters in a string and puts them in
    Lexicographic order'''
    if a == '': #base case
        return []
    if len(a) ==  1: #base case
        return [a]
    finlist = []
    for char in a:
        simple = a.replace(char,'') #remove a character to create a simpler string
        for perm in perm_gen_lex(simple): #generate all permutations
            finlist.append(char + perm) #add the character back to the permutations and append them to a list
    return finlist

