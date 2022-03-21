## numbers 1 - 9 

x = [i for i in range(10) ]
print(x)


## adding an expression - square of each number 


squares = [i**2 for i in range(10)]
print(squares)


## multiply each element by 3 

list1 = [3,4,5]
multiply = [item*3 for item in list1]
print(multiply)


## word manipulation 

listofwords = ["this", "is", "a", "list", "of", "words"]
first_letter = [item[0] for item in listofwords]
print(first_letter)


letter = ["A", "B", "C"]
lowercase = [x.lower() for x in letter]
print(lowercase)
## x.upper() would put it into uppercase


## adding an IF condition 
# gets the even numbers from 1-4 squared 
new_range = [i*i for i in range(5) if i%2 == 0]
print(new_range)

# gets just the numbers
string = "Hello 12345 World"
just_numbers=[x for x in string if x.isdigit()]
just_letters = [x for x in string if x.isalpha()]
print(just_numbers)
print(just_letters)


## using a file 

myfile = open('test.txt', 'r')
result =[i.rstrip("\n") for i in myfile if "line3" in i]
print(result)


## using functions
# double every number in range 10 
def double(x):
    return x*2

print(double(10))

mynumbers =[double(x) for x in range(10)]
print(mynumbers)

# for even numbers only 
mynumbers =[double(x) for x in range(10) if x%2 == 0]
print(mynumbers)


## you can add more than one argument 

result = [x+y for x in [10,30,50] for y in [20,40,60]]
print(result)