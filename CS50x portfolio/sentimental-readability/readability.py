# TODO
from cs50 import get_string

count_words = 1
count_letters = 0
count_sentences= 0

text= get_string("Text: ").upper()

for words in text:

    if ord(words)>= 65 and ord(words)<= 90:
        count_letters += 1

    if words == " " or words.isspace == True:
        count_words += 1


    if (words == "." or words == "!" or words == "?"):
        count_sentences += 1


L =  (count_letters /count_words * 100)
S = (count_sentences /count_words * 100)

grade =  (0.0588 * L -  0.296 * S - 15.8)

if grade >= 16:
    print ("Grade 16+")
elif grade <= 1:
    print ("Grade before 1")
else:
    print (f"Grade {round(grade)}")



