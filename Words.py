import random
def words():
    file = open("5letters.txt",'r')
    list_words = []
    for word in file :
        list_words.append(word[:-1])
    return list_words
def choose_word():
    words_list = words()
    rand_i = random.randint(0,len(words_list)-1)
    return (words_list[rand_i])

    

