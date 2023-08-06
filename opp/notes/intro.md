# Intro

This is where we start. There are a few things that you will need to know before we can really get going. 

1. Variables
2. Simple Types
3. If's
4. Functions
5. Loops

Each of these has a bit more to it, and we will break it all down. But if you can get these basics down, on paper, you can do anything.

## Variables
```python
print("Hello, world!")
name = "opp"
print("Hello " + name + "!")
```
Variables are here to help declare things. We can assign a variable a value and it will keep track of it for us.
Recall that this concept is just the "left" side of the equals sign (`=`).

Variables are the stepping stone to everything. See how they can help us do math too:
```python
x = 10
print(x * 3)
```
But it can also store other things if we need to.

## Simple Types
What are the other things that can be stored?
Recall that this is the "right" side of the equals sign (`=`).

Well, let's start simple
1. `int`
3. `str`
4. `bool`

For now, there are only three (3) things you care about. Integers, Strings and Booleans. 
Let's take 'em one at a time.

### int's
Numbers. These are numbers. You can do math.
```python
x = 10
print(x * 3)
x = x + 1
y = 5
z = x / y
```

#### float's
Okay. I lied before. There is another type but it didn't feel like you needed to know this explicitly up-front.
If you do division, you might run into something like `2.2`. When a number has a decimal, that's called a `float`.

Note that `//` is how to divide with ints to get ints. `/` will get you a `float`.

### bool's
True. False. That's all there is to it.
```python
t = True
f = False
print(t and f)
print(f and f)
print(t or f)
print(t or t)
print(f or f)
```

#### Addition???
Recall that computers are just 1's and 0's. All the way down to the core.
That will always be true. And you can see that:
```python
print(2 + True + True + True)
```

### str's
Strings. These are, well, strings. Words.
There's a lot you can do with strings, but we are going to start with just adding them.
```python
name = 'Mr.'
last_name = 'Sir'
print(name + last_name)
```
Note how you might need to include a space sometimes when you add strings.
```python
name = 'Mr.'
last_name = 'Sir'
print(name + ' ' + last_name)
```

#### Random Access
We didn't unlock this yet. See loops.

## If's
Programming is about inherently about logic. If statements help define that logic.

There are three types of ifs.

### if
The standard lone `if`. This checks if some condition is true.

If the `if` statement evaluates to `True`, the indented block will be run.
```python
name = "jake"
if name == "jake":
  print("Hello " + name)
```

Note that you can do different types of logical conditions in the if statement.
```python
if name != "jake":
  print("This will not be printed.")

if not name == "jake":
  print("What do we think this will do? How is this different?")
```

### else
`Else` is a default. If this is true, do this. Otherwise, do this.
```python
x = 10
if x <= 0:
  print("X is a negative number")
else:
  print("X must be positive")
```

### elif
You are allowed to specify multiple if conditions back to back to back. You can do this with an else if, or `elif`.
```python
x = 10

if x < 0:
  print("X is less than 0")
elif x == 5:
  print("X is EXACTLY 5")
elif x > 10:
  print("X is greater than 10")
else:
  print("hmmmm. I wonder what X can be?")
```

## Functions
A function is just defining a smaller unit of work.
Functions take input and produce and output.

Let's start with a math example
```
f(x) = x + 1
f(5) = 6
```

Functions in code work in a very similar way. They take input `parameters` and `return` a result.

```python
def add_five(x):
  return x + 5

print(add_five(1))
print(add_five(5))
```

Remember! Don't get confused between `print` and `return`!
`return` is the output of the smaller unit of work, the output of the function.
`print` is telling the human who is using the computer this is the current state of this variable.
Printing is NOT a returning.

You can have functions with multiple inputs
```python
def add(x, y):
  return x + y

def mult(x, y):
  return x * y
```

Remember that you can also use if's inside functions. You can even call functions inside other functions.
You can also return anything that you want.
```python
def fun_math(x, y):
  x = add(x, y)
  y = mult(x, y)
  if mult(x, y) > 100:
    return True
  elif add(x, y) > 25:
    return True
  else:
    return False
```

### Args & Kwargs
You did not unlock this yet. This is not part of the intro.

## Loops
Before we can even start loops, we need to learn a bit about lists.

### Lists
A list is a collection of elements.
```python
list_1 = [1, 2, 3, 4]
```

You can put anything in a list if you wanted to. Items can repeat themselves or by any type.
```python
confusing_list = ["Mr. Sir", 1, True, 2, -1, None, None, "Mr. Sir"]
```

You can even put lists inside of lists.
```python
list_of_list = [[1, 2, 3,], [2, 4, 6], [3, 5, 8]]
```

Now we are gearing up for loops. 
Here's a formal definition that I stole off the internet:
Loops are a way to specify a sequence of instructions that are continually repeated until a certain condition is met.

In English, do something a whole buncha times in a row.

### For
```python
for number in list_1:
  print(number)

for number in range(10):
  print(number)

for i in ["jake", "was", "here"]:
  print(i)

for i in "jake was here":
  print(i)
```

### While
```python
start = 0
while start < 10:
  start = start + 1
```

