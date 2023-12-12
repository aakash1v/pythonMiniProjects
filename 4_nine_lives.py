
print("------------ This is a program to guess the word -----------\n")
word = ['p','i','z','z','a']
li = ['?','?','?','?','?']
num = 9



def guess_word():
    global num
    lives = '💗'*num
    # Printing lives and answers 
    print(li)
    print("lives left :"+lives)
    # asking for the letter /word 
    print("Guess a letter or the whole word: ")
    user_input = input()
    if any(letter in user_input.lower() for letter in word):
        a=0
        for i in word:
            if i ==user_input.lower():
                index = a
            a+=1
        li[index]= user_input.lower()
    else:
        num=num-1

while num !=0:
    guess_word()