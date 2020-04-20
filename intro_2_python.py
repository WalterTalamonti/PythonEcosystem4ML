# fun with Variables
x,y,z = 1,2,3
print(y)

# fun with Boolean
age = 45
is_older = age > 40 and age < 65
print(is_older)

san_francisco_pop_density = 4500000
rio_de_janeiro_pop_density = 5000000
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
# Other solutions are possible, like the one below, but appreciate the concise efficiency of the one line above!

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)

# fun with Strings
salesman = 'I think you\'re an encyclopedia salesman'
first_word = 'Hello'
second_word = 'There'
print(first_word + second_word) # HelloThere
print(first_word + " " + second_word) # Hello There
print(len(first_word))
print(len("ababa") / len("ab"))

# Strings Quiz
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count) # answer is 3415 bec both are strings!

# 13.37.islower()

print('hello world'.title())
print('"The sum of 1 + 2 is {0}"'.format(1+2))

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

# Version 1
print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))

# Version 2
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))

# fun with Lists and Members of
VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
print('GE' in VINIX)
print('F' in VINIX)

# fun with the join method
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
name = "-".join(["García", "O'Kelly"])
print(name)

#fun with the append method
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)






#fun with Iterators and Generators
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# fun with Iterators and Generators
sq_list = [x**2 for x in range(10)]  # this produces a list of squares
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares