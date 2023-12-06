with open("parole.txt", "r") as file:
    possible_words = [line[0:-1] for line in file]

search_word = possible_words[1780]
