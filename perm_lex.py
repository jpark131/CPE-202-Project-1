def perm_gen_lex(a):
    list = []
    if a == '':
        return []
    for char in a:
        simple = char.replace(char, '')
        list += [[simple] + perm_gen_lex(simple)]
    return list

print(perm_gen_lex('abc'))
