
answer =["polar bear","cheetah","blue whale","aakash kumar","rahul kumar pathak","ankush","yes"]
questions_list =["Which bear lives at the North Pole? ","Which is the fastest land animal?","Which is the largest animal? ","Who is the most powerful person?","Who is Pathak ji","Who is chatur ?","Are you a fool?"]
counter =0
score =0
def check_answer(user_input):
    global counter
    global score
    x = 0
    while(user_input.lower() != answer[counter]):
        # giving chances for wrong answers 
        print("Sorry, wrong answer. Try again. ")
        user_input = input()
        x =x +1
        if x==2:
            break

    # reducing marks for wrong answers
    score = score-x
    if(user_input.lower() == answer[counter]):
        print("correct answer")
    else:
        print(f"correct anser is {answer[counter]}")

    counter+=1
    score +=1
    return counter

def questions():
    for i in questions_list:
        print(i)
        user_input = input()
        check_answer(user_input)
        
    return score

print("Guess the Animal!")
score = questions()
print(f"Your score is {score}")



