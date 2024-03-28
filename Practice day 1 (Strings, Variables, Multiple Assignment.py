#1 Strings
print("i love pizza")
print("its extremely good")


#2 Variables
## string variables/data types
first_name = 'Feng'
last_name = 'wei'
full_name = (first_name + " " + last_name)

print("Hello" + ' ' + full_name)

## Integer Variables/data types
age = 35
age = age + 1
print(age)
print(type(age))
print("You are age" + " " + str(age))

## Float Variables/data types
height = 250.9
print(height)
print(type(height))
print("Your height is " + " " + str(height) + "cm")

## Boolean Variables/data types
human = True
print(human)
print(type(human))
print("Are you human:" + " " + str(human))


#3 Multiple assignment = Allows us to assign multiple variables at the same time in one line of code
## Standard assignment example
name = 'D'
age = 30
fresh = True

print(name)
print(age)
print(fresh)

### Muliple assignment example (All at once)
name, age, fresh = 'D', 30, True
print(name, age, fresh)

### Another Example
Kazuya = 30
Law = 30
Lee = 30
Paul = 30

Kazuya = Law = Lee = Paul = 30

#4 String Methods
## Bunch of examples
name = "Miguel"
print(len(name))
print(name.find('M'))
print(name.capitalize())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('e'))
print(name.replace('g', 'l'))
print(name*3)

#5 Type Casting = Convert the data type of a value into another
## examples

n = 4 #integer (int)
d = 3.5 #float
s = '5' #string (str)

### changing s
s = int(s)
s = float(s)
print(s)
print(type(s))
### changing d
d = int(d)
d = str(d)
print(d)
print(type(d))
### changing n
n = str(n)
n = float(n)



