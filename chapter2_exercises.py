# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# 2.2

Type the following statements in the Python interpreter to see what they do:

5 – shows 5
x=5 – sets x to 5
x+1 – adds 5 to 1 resulting in 6
Now put the same statements into a script and run it. 
What is the output? Modify the script by transforming each expression 
into a print statement and then run it again.

Almost all of those above would work with print statement save for print x=5, apparently because we’re trying to do two things at once – set x to 5 and print out the resulting x. 

Proper way of doing it is:
x=5
print x

# 2.3

1.	width/2

    8 / integer


2.	width/2.0
    
    8.5 / float

3.	height/3

    4.0 / float

4.	1 + 2 * 5

    11 / integer

5.	Delimiter * 5

    ..... / string

# to find out the type of an expression we use type(expression)


# 2.4

1. The volume of a sphere with radius r is r = 4/3pr³.
What is the volume of a sphere with radius 5?
Hint: 392.7 is wrong!
We’ll use the example of equation: V = 4/3pr³. The "V" stands for volume and "r" stands for radius of the sphere.
Find the radius – in our case 5.
Cube the radius – 5 * 5 * 5 = 125
125 * the value of pi (3.14159265) = 392.69908125
392.69908125 * 4 / 3 = 523.598775
Final answer: 523.598775


2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the ?rst copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?
Cover price of a book – 24.95
Discount – 24.95 * 40 / 100 = 9.98
Price of a book without shipping – 24.95 – 9.98 = 14.97
First book with shipping – 14.97 + 3 = 17.97
Price of each book after the first one w/shipping – 14.97 + 0.75 = 15.72
Price of 59 books, not counting the first one – 15.72 * 59 = 927.48
Price of 60 books, including the first one = 927.48 + 17.97
Final Answer: 945.45  

3. 1 mile at easy pace – 8.15
2 miles at easy pace – 16 min 30 sec
3 miles at tempo – 21 min 36 sec
5 miles in total – 38 min 6 sec
6:52 + 38 min 6 sec – 7 hours 30 mins 6 seconds
Final Answer: 7 hours 30 mins 6 seconds
