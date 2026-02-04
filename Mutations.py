def mutate_string(string, p, character):
    mutate = string[:p] + character + string[p+1:]
    return mutate

