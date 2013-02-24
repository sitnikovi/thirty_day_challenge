# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

Exercise 3.1.
Move the last line of this program to the top, so the function call appears before the
definitions. Run the program and see what error message you get.
name 'repeat_lyrics' is not defined

Exercise 3.2. 
Move the function call back to the bottom and move the definition of print lyrics
after the de?nition of repeat lyrcs. What happens when you run this program?
Everything remains the same - no errors. 

Exercise 3.3 
Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
def right_justify(s):
         print (' '*(70-len(s))+s)
right_justify('allen')

Exercise 3.4
1. Type this example into a script and test it.
def do_twice(f):
   f()
   f()

def print_spam():
   print 'spam'
2. Modify do_twice so that it takes two arguments, a function object and
a value, and calls the function twice, passing the value as an argument.
nope = raw_input('What word')
def do_twice(f,nope):
    f(nope)
    f(nope)
def print_spam(nope):
    print 'nope'
do_twice(print_spam, nope)
3. Write a more general version of print_spam, called print_twice, that 
takes a string as a parameter and prints it twice.
string = 'string'
def print_twice(string):
    print string
    print string
print_twice (string)
4. Use the modified version of do_twice to call print_twice twice, passing 
'spam' as an argument.
def do_twice(f, word):
   f(word)
   f(word)

def print_spam(word):
   print word

string = "steven"

def print_twice(string):
   print string
   print string

print_twice(string)

newWord = "Spam"
do_twice(print_twice, newWord)
5. Define a new function called do_four that takes a function object and 
a value and calls the function four times, passing the value as a parameter.
There should be only two statements in the body of this function, not four.
def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')
print ''

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')
print ''
