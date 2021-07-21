#THE LONG WAY
words = input("Enter a string: \n ")
print(words)
g = ""
for i in words:
    if i==" ":
      continue 
    else:
       g = g+i
print("without spaces: ")
print(g)

# THE EASY WAY
# print(input( "Enter a string: \n" ).replace(" ",""))
