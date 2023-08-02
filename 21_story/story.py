story = ""
previous = ""

while True:
    word = input("Please type in a word: ")
    if word == previous or word == 'end':
        break
    story += word + ' '
    previous = word

print(story)