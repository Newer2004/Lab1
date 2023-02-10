def guess(number, name, cnt):
    if(number>19):
        print("Your guess is too high.")
        print("Take a guess.")
        number=int(input())
        cnt=cnt+1
        guess(number, name, cnt)
    elif(number<19):
        print("Your guess is too low.")
        print("Take a guess.")
        number=int(input())
        cnt=cnt+1
        guess(number, name, cnt)
    elif(number==19):
        cnt=cnt+1
        win="Good job, {} You guessed my number in {} guesses!"
        print(win.format(name, cnt))

print("Hello! What is your name?")
name=input()
print(name)
well="Well, {}, I am thinking of a number between 1 and 20."
print(well.format(name))
print("Take a guess")
number=int(input())
cnt=0
guess(number, name, cnt)