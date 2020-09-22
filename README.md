# coding-workshop

Hello!

Welcome to the repository for the Coding Workshop.

You can find all the code that we've done and explained in the session here.

Let's summarise all the basic points that we've covered:

## Datatypes

As the name suggests, a datatype is a name for the type of data.

`1` is of type `integer`.

`2.5` is of type `float` or `double`.

`"this is a word"` is of type `string`.

To learn more about datatypes, you can check [here](https://realpython.com/python-data-types/).

## Variables

A variable is a storage for a value.
The value can be a number, a word or a sentence, or even a collection of the said items.

In Python we can directly define a variable without having to explicitly specify the datatype.

For example, a statement:
```python
variable1 = "this is a string"
``` 

This will create a variable called `variable1` which would store a `string` value of `this is a string`.

**NOTE:** String values should always be surrounded with quotation marks.

```python
number = 5
decimal = 4.67
```

This would create a variable called `number` which would store the value of `5`, `decimal` which would store the value of `4.67`.

### What if we want to specify a type or convert to a type?
If you want to specify a value as an `integer`, we can do it like this:
```python
number = int(57)
```   

This would store it as an integer.

However, this would also store it as an integer.
```python
number = 57
```

If you want to convert an integer to a string:
```python
number = int(57)
string = str(number)
```

Now, the variable `string` would hold the value `"57"`.

And it works vice-versa as well.

To learn more about variables, check [this](https://realpython.com/python-variables/).

## User Inputs:
To get an input from user, Python has the functionality of `input()`.

```python
user = input("Enter a value:")
```

This would print `Enter a value:` on the users screen/terminal, and on pressing enter,
the value entered by the user will be stored in the variable `user`.

## Printing Data:
In Python, we use `print` statements to print data onto the users terminal/screen.

```python
print("Hello world!")
```

This would print `Hello world!`.

**NOTE**: Print function always accepts a string value. So please make sure when passing
data to print, they have been converted to string.

**NOTE AGAIN**: If you a pass a single integer or a double or a float value, print will print the value as it is.
But if you want to print an integer with a string, you'll have to convert the integer
into a string. 

## Conditional Statements:
In python (and 99% of other programming languages as well..), conditional statements
are done through `if` statements.

We provide a condition for the if statement.

```python
if 5 > 3:
    print("5 is greater than 3")
```

```python
if variable1 != variable2:
    print("Variable 1 is not equal to variable 2.")
```

### What about an else?
If the condition is not met, then what will happen?

This scenario we can provide using an else statement.

```python
if 5 > 3:
    print("5 is greater than 3")
else:
    print("5 is not greater than 3")
```

### But what if an else with an if?
Don't worry, this scenario is also handled.

```python
user = 5
if user < 2:
    print("Less than 2")
elif user < 4:
    print("Less than 4")
else:
    print("Greater than 4")
```

To learn more about if statements, check [this](https://realpython.com/python-conditional-statements/).

## Loops
Loops, as the name suggests, is to loop through stuff.

We can provide a loop to loop through stuff or for a certain range.

For each loop, we have to provide an end condition and an increment/decrement statement.
What are they?

#### Conditions
Conditions are used to provide an end case for the loop, so that the loop doesn't 
go on infinitely.

#### Increment / Decrement
Increment / Decrement is to update a specific value which is being looped over.

For example:

If we want to loop through the numbers from 0 to 9. We would need to start at 0 and after every
iteration of the loop, increase the counter. Till the point we reach the count 9. And that's when
the end condition will get triggered, and the loop will stop.

### How can we make loops then?

In python there are two methods to do loops:
1. For loops.
2. While loops.

#### For loops
```python
for i in range(10):
    print(i)
```

This would print the numbers from 0 to 9.
```
0
1
2
3
4
5
6
7
8
9
```

```python
for i in ['a','b','c','d','e']:
    print(i)
```

This would print:
```
a
b
c
d
e
```

To learn more about for loops, check [this](https://realpython.com/python-for-loop/).

#### While loops
```python
i = 0
while i<=9:
    print(i)
```

This would print:
```
0
1
2
3
4
5
6
7
8
9
```

To learn more about while loops, check [this](https://realpython.com/python-while-loop/).

## Functions
A function is a collective of code which we can reuse.

Let's say we want to add two numbers. It would be annoying if we had to write the add statements
again and again, multiple times.

That's where a function would come into play!

We can create a function to add the two numbers and then just call the function.

Some basic concepts around functions:

### Parameters
Parameters are the values that you provide the function with, to perform the task.

In the case of an "add" function. The parameters would be the two numbers that you have to add.

### Return
Now a function after performing the task, can either output the results there itself, in the function.
Or it can send the result back to whoever called it.

To send the result back, we have to use a `return` statement.

```python
def add(value1, value2):
    sum = value1 + value2
    return sum
```

Here we are creating a function called `add`, which accepts two parameters:
`value1` and `value2`.

It will add the two values and return the sum.

How can you invoke this function?
```python
sum = add(5, 10)
```

Here, we are calling the function `add` and passing the values as 5 and 10. 
And we are storing the result in a variable called `sum`.

To learn more about functions, check [this](https://realpython.com/defining-your-own-python-function/).


## Conclusion
These are the basic concepts of coding. All languages utilise these. All programs utilise this.
The world runs on these.

If you want to learn more, please do explore.

Happy Coding!