words = input("Type something: ")
words_arr = list(words)

for i in words_arr:
    if(i == " "):
        print("-\n")
    else:
        print(i+"\n")
