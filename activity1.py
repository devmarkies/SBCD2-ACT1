# # Single Quote
# print('\'Yes,\' they said  this is bootcamp')
# #Double Quote
# print("BOOT CAMP")
# print(69)//

#slicing
#text = "hello world"
#print(text[:-5])

#string method

#word = "hello mama"
#print =(word.isalpha())
#print =(word.upper())
#print =(word.lower())
#print =(word.istitle())
#print =(word.capitalize())
#print =(word.isalpha())
#print =(word.isnumeric())
#print =(word.isalnum())




#string methods

#word = summer bootcamp
#the outputs
#Summer Bootcamp
#Summer bootcamP
#Loot
#camE
#AR
#TRUE
word = "summer bootcamp"

output1 = word.title()
print(output1) 
output2 = word.capitalize()[:-1] + word[-1].upper()
print(output2) 
output3 = word.replace("summer bootcamp", "Loot")
print(output3)  
print(word[-4:-1]+"E")
print(f"{word[-3].capitalize()}{word[5]}")
aha = word.replace(" ", "")
print(aha.isalpha())

