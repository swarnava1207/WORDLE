from Words import *
def checking(submit_button,dic_labels,row,label,display_button):
    #chosen_word = ("".join(choose_word())).upper()
    #print(chosen_word)
    chosen_word = choose_word().upper()
    print(chosen_word)
    guess_word = ""
    def submit(guess_word,event = None ):
        for num in range(5):
            guess_word += dic_labels["lab"+str(row[0])+str(num)]['text']
        if (guess_word.lower()) not in words():
            for num in range(5):
                dic_labels["lab"+str(row[0])+str(num)]['text'] = ""
            guess_word = ""
            label[0] = dic_labels["lab"+str(row[0])+"0"]
            return

        row[0]+=1 
        

        for letter in range(len(guess_word)):
            if guess_word[letter] in chosen_word:
                if guess_word[letter] == chosen_word[letter]:
                    dic_labels["lab"+str(row[0]-1)+str(letter)].configure(background = "#00ff00")
                    dic_labels["lab"+str(row[0]-1)+str(letter)].configure(foreground = "#ffffff")
                else:
                   dic_labels["lab"+str(row[0]-1)+str(letter)].configure(background = "#ffff00")
                   dic_labels["lab"+str(row[0]-1)+str(letter)].configure(foreground = "#ffffff")
        if guess_word == chosen_word:
             display_button.configure(text = "Yayy! You Won")
             return
        if row[0] == 6:
            if guess_word != chosen_word:
                display_button.configure(text = f"Sorry! The word was {chosen_word}")

        else :
            display_button.configure(text = f"Only {6-row[0]} chances remaining")

    submit_button['command'] = lambda : submit(guess_word)


