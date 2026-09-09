#Into to Python (Redux)
#Single Line comment
'''
MultiLine Comment / Document comment

python is read top --> bottom, left to right - sequencing

loosely typed - we do not declere datatype

variable -container with a label on it. You can put any information inside you want and you use the name to grab the value/info

Naming conventions for varables:
- cannot START with a Number
- cannot include spaces
- cannot include most symbols (can use underscore)
- should be as clear as neccesary
- cannot use reserved keywords
-case sensitive
- must start with a letter or underscore
- Industry standar = use sanake_case or camelCase
'''

#To run python: python3 <name of file>
print("Hello World!")

#Primitive DataTyes
#Number:
# int - integer - whole numbers. discrete values
# float - Floating point decimal numbers
fav_number = 13

#Strings - text, always surrounded with quotes. Double or single quotes
name = 'Dylan'
cat_name = 'Thumbs'
text = 'Joey says,"Hello world", when he greats the day'
text_dos= "Joey says,\"Hello world\", when he greats the day"

#Boolean -bools True/False, 0/1
#Do not put quotes on a boolean,you will make a string, and all populated string are True
speak_french = False
speak_english = True

print(name,"favorite number", fav_number)

#Formatte string allow the direct injection of variables/values into a sting
#Use f'' to declare a string type,then curly braces {} to surround the dynamic values (variables)
print(f'{name} has a pet named {cat_name}')

#input() function - accepts input fromthe user in the terminal.To call (invoke, run). a function you use parenthesis
name = input("What is your name?")
print(f'Hello {name}')
age = input("how old are you?")
print(f'Your age {age} years old!')