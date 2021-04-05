words = int(input())

for i in range(0, words):
    word = input()

    if(len(word) <= 10):
        print (word)

    else:
        print(word[0] + str(len(word) - 2) + word[-1])