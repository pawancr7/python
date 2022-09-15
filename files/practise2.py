def game():

    return 5212


score = game()
with open("another.txt") as f:
    hiscore = int(f.read())

if hiscore < score or hiscore == " ":
    with open("another.txt", "w") as f:
        f.write(str(score))
