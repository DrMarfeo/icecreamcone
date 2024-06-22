# Get input
# sdfdsfdsdsd

# from flask import flask
# app = Flask(name) # Flask Constructor

#Decorator, a function we can use on a function
# @app.route('/') # Decorator, that will take in another function
# def hello():
  #  return 'HELLO'

#app.route('/resume')
# def my_resume():
   # return 'This would be my resume'

# if __name__=='__main__':
   # app.run()




# Get user input
userinput = input("What is your word or phrase?")
print(userinput)

# Create top and Bottom Border
top_and_bottom_border = len(userinput) * '*'
print(top_and_bottom_border)
print('' +userinput +'')
 # Generate output

'''Strings Part 2'''
# Just applying the  method to the string won't change the original value
str_1 = 'BLUE'
str_1.lower()
str_1 = str_1.lower()
print(str_1)

day = ' TUESDAY' # Create a new string with no whitespace
new_day = day.strip()

print(len(day)) # 12 characters
print(len(new_day)) # 7 characters, white space is stripped

'''Indexing, with square brackets'''
word = 'Jasmine'
first_letter_of_word = word[0]
print(first_letter_of_word)
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[6])
print(word[7])
print(word[8])


# Create a variable to capture the first letter of this string
greeting = 'whatssup!'
first_position = greeting[0]

# Grab the last letter in a variable
last_position = greeting[len[-1]]

print(last_position)