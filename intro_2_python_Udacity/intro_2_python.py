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

# Quiz
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count) # answer is 3415 bec both are strings!

# 13.37.islower()

print('hello world'.title())
print('"The sum of 1 + 2 is {0}"'.format(1+2))