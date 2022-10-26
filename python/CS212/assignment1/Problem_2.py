chocobars_num = 213
students_num = 133

# even distribution = what to be shared / num of people to share with
chocolate_per_student = chocobars_num // students_num
remaining_chocolates = chocobars_num % students_num

# message
print("Each student would receive", chocolate_per_student, "chocolate bar(s).")
print("There would be", remaining_chocolates, "chocolate bars left over.")
