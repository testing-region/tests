day = int(input())
month = int(input())
year = int(input())
months = {
   1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'
}

print('{0}th {1} {2}'.format(day, months[month], year))