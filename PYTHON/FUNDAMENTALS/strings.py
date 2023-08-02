## Note: Strings are arrays ##
letters = "Hello!!" 
value = "word"
phrase = "I love you"
number = 143
##Remove characters
print(letters.strip("!"))

##Print every letter
for letter in letters:
    print(letter)

##Get the length
print(len(letters))

if "love" in phrase:
    print(phrase)

if "Hello" not in phrase:
    print("True")

##Slice
print(letters[1:5]) #returns ello

##Upper and Lower Case
print(letters.upper())
print(letters.lower())

#replace character
print(letters.replace("H", "B"))

#combine strings and numbers
print(phrase + " " + str(number))

print(letters.find("e"))