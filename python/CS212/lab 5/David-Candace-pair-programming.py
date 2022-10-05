# Q1

def check_holiday(month, day):
    """Checks whether or not a date falls under a specific holiday

    Args:
        month (str): Month of the year
        day (int): day of the month
    """
    msg = "Oops! There is no holiday on this date"
    
    # Checking if entered date is valid for a holiday
    if month == "January":
        if day == 1:
            print("New Year's")
        elif day == 9:
            print("Constitution Day")
        else:
            print(msg)
    
    elif month == "April":
        if day >= 7 and day <= 10:
            print("Easter")
        elif day >= 21 and day <= 22:
            print("Eid al Fitr")
        else:
            print(msg)
    
    elif month == "May" and day == 1:
        print("May Day")
    
    elif month == "June":
        if day == 28 or day == 29:
            print("Eid al-Adha")
        else:
            print(msg)
    
    elif month == "August" and day == 4:
        print("Founder's Day")

    elif month == "September" and day == 21:
        print("Kwame Nkrumah Memorial Day")
    
    elif month == "December":
        if day == 1:
            print("Farmer's Day")
        elif day == 25:
            print("Christmas Day")
        else:
            print(msg)

    else:
        print(msg)


# tests for check_holiday
print("Testing for holiday")
print("-"*20)
check_holiday("May", 31)
check_holiday("July", 15)
check_holiday("November", 23)
check_holiday("December", 25)
check_holiday("January", 10)

# add gaps between the two functions
print()
print()

# Q2

def check_colour(wavelength):
    """Checks if an entered wavelength falls under the visible light spectrum

    Args:
        wavelength (int): wavelength of light
    """

    # Checking if entered wavelength falls in valid range
    if wavelength >= 380 and wavelength < 450:
        print("The colour is violet")
    elif wavelength >= 450 and wavelength < 495:
        print("The colour is blue")
    elif wavelength >= 495 and wavelength < 570:
        print("The colour is green")
    elif wavelength >= 570 and wavelength < 590:
        print("The colour is yellow")
    elif wavelength >= 590 and wavelength < 620:
        print("The colour is orange")
    elif wavelength >= 620 and wavelength <= 750:
        print("The colour is red")
    else:
        print("Sorry! Your wavelength is out of the range of visible light")


# tests for check_colour
print("Testing for colour")
print("-"*20)
check_colour(6000)
check_colour(500)
check_colour(-123450)
check_colour(430)
check_colour(700)