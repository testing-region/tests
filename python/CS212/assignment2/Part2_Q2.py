from Part2_Q1 import country_names_dict
from Part2_Q1 import population_list
from Part2_Q1 import percent_literacy_rate
from Part2_Q1 import mobile_subs_num
from Part2_Q1 import net_users_num
from Part2_Q1 import electricity_prod_amt
from Part2_Q1 import electricity_consump_amt


def get_country_info(country):
    """Returns detailed information about selected country

    Args:
        country (str): African country

    Returns:
        str: detailed country information
    """
    index = country_names_dict[country]
    population = population_list[index]
    literacy_rate = percent_literacy_rate[index]
    mobile_sub_count = mobile_subs_num[index]
    internet_users_count = net_users_num[index]
    electricity_prod = electricity_prod_amt[index]
    electricity_consump = electricity_consump_amt[index]

    info = f"{country} has a population of {population:,} with a literacy rate of {literacy_rate}%. \nThe estimate of the number of mobile subscriptions is {mobile_sub_count:,}, while that of internet users is {internet_users_count:,}. \n{country} produces {electricity_prod} billion kWh of electricity annually, while it consumes {electricity_consump} billion kWh of electricity."

    return info


# A simple program to test the function
country = input("Hello! Which African country would you like information on?: ")

if country not in country_names_dict.keys():
    print("\nCountry information not found!.")
    print("[!] Perhaps, you forgot to capitalise the country name.")
else:
    print(get_country_info(country))
