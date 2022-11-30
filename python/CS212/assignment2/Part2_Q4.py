from Part1 import max_index
from Part1 import min_index
from Part2_Q1 import population_list
from Part2_Q1 import country_names
from Part2_Q1 import percent_literacy_rate
from Part2_Q1 import mobile_subs_num
from Part2_Q1 import net_users_num
from Part2_Q1 import electricity_consump_amt
from Part2_Q1 import electricity_prod_amt
from Part1 import pairwise_product
from Part1 import smaller_indices


def report_total_population():
    total = sum(population_list)
    print(f"The total population of Africa is {total:,}.")


def report_populous_countries():
    min_country_index = min_index(population_list)
    max_country_index = max_index(population_list)

    print(f"The most populated country is {country_names[max_country_index]}.")
    print(f"The least populated country is {country_names[min_country_index]}.")


def report_literacy_rates():
    min_literacy_index = min_index(percent_literacy_rate)
    max_literacy_index = max_index(percent_literacy_rate)

    print(f"The country with the highest literacy rate is {country_names[max_literacy_index]}.")
    print(f"The country with the lowest literacy rate is {country_names[min_literacy_index]}.")


def report_average_literacy_rate():
    average_literacy = pairwise_product(percent_literacy_rate, population_list)

    average_literacy_rate = sum(average_literacy) / sum(population_list)

    print(f"The average literacy rate in Africa is {average_literacy_rate:.2f}%.")


# Create lists to store new data
mobile_subs_per_cap = []
net_users_per_cap = []

for index in range(len(country_names)):
    # per capita means value divided my the population
    mobile_per_cap = mobile_subs_num[index] / population_list[index]
    net_per_cap = net_users_num[index] / population_list[index]

    mobile_subs_per_cap.append(round(mobile_per_cap, 3))
    net_users_per_cap.append(round(net_per_cap, 3))


def report_mobile_subs_per_cap():
    min_mobile_subs_per_cap_index = min_index(mobile_subs_per_cap)
    max_mobile_subs_per_cap_index = max_index(mobile_subs_per_cap)

    print(f"The country with the highest number of mobile subscriptions per capita is {country_names[max_mobile_subs_per_cap_index]}.")
    print(f"The country with the lowest number of mobile subscriptions per capita is {country_names[min_mobile_subs_per_cap_index]}.")


def report_net_users_per_cap():
    min_net_users_per_cap_index = min_index(net_users_per_cap)
    max_net_users_per_cap_index = max_index(net_users_per_cap)

    print(f"The country with the highest number of internet users per capita is {country_names[max_net_users_per_cap_index]}.")
    print(f"The country with the lowest number of internet users per capita is {country_names[min_net_users_per_cap_index]}.")


def report_power_exporters():
    countries_list = smaller_indices(electricity_consump_amt, electricity_prod_amt)

    print("The countries who produce more electricity than they consume are:", end="")
    for index in range(len(countries_list) - 1):
        print(f" {country_names[index]},", end="")

    print(f" and {country_names[countries_list[-1]]}.")


def report_power_importers():
    countries_list = smaller_indices(electricity_prod_amt, electricity_consump_amt)

    print("The countries who consume more electricity than they produce are:", end="")
    for index in range(len(countries_list) - 1):
        print(f" {country_names[index]},", end="")

    print(f" and {country_names[countries_list[-1]]}.")


# Calling functions
report_total_population()
print()

report_populous_countries()
print()

report_literacy_rates()
print()

report_average_literacy_rate()
print()

report_mobile_subs_per_cap()
print()

report_net_users_per_cap()
print()

report_power_exporters()
print()

report_power_importers()
print()
