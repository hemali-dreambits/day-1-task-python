#Print odd numbers between 1 to 10 in reverse order using while.
number = 10
while number >= 1:
  if number % 2 !=0:
    print(number)
  number -= 1


#Get two lists ['a','b','c','d','e'],[1,2,3,4,5] and generate a single dictionary {'a':1,'b':2,'c':3,'d':4,'e':5} with the identical indexed items.
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
result = {}
for i in range(len(keys)):
  result[keys[i]] = values[i]
print(result) 


#Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False.
def letter(word):
    word = word.replace(" ", "").lower()  
    return len(word) != len(set(word))  

print(letter("abcd abcdef pqef")) 


#Write a function in Python to parse a string such that it accepts a parameter- an encoded string. 
#This encoded string will contain a first name, last name, and an id. You can separate the values in the string by any number of zeros.
#The id will not contain any zeros. The function should return a Python dictionary with the first name, last name, and id values.
#For example, if the input would be “John000Doe000123”. Then the function should return: { “first_name”: “John”, “last_name”: “Doe”, “id”: “123” }
def encode(string):
  part = string.split('0')
  part = [part for part in part if part]
  if len(part) == 3:
    return {
      "first_name": part[0],
      "last_name": part[1],
      "id": part[2]
    }
  else:
    print('not match')

string = "John000Doe000123"
result = encode(string)
print(result)      



#In a park, there are a certain number of buffaloes and cranes. Take the total number of heads and legs as input from the user to calculate the number of buffaloes and cranes in the park.
total_heads = 20
total_legs = 51
if total_legs % 2 != 0:
    print("legs must be an even number.")
else:
    x = (total_legs - 2 * total_heads) // 2 
    y = total_heads - x  
    print(f"Buffaloes: {x}, Cranes: {y}")

