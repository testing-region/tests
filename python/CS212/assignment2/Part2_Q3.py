import sys
from Part2_Q1 import country_names
from Part2_Q1 import mobile_subs_num
from Part2_Q1 import net_users_num
from Part2_Q1 import population_list


def store_info():
    """Stores the country name, mobile subscriptions per capita and internet users per capita data into a file"""

    # Create lists to store new data
    mobile_subs_per_cap = []
    net_users_per_cap = []

    for index in range(len(country_names)):
        # per capita means value divided my the population
        mobile_per_cap = mobile_subs_num[index] / population_list[index]
        net_per_cap = net_users_num[index] / population_list[index]

        mobile_subs_per_cap.append(round(mobile_per_cap, 3))
        net_users_per_cap.append(round(net_per_cap, 3))

    # Files are streams of data.
    # Using the `print` function writes its arguments to the system's standard output.
    # If the standard output is changed to a file, then the print function displays the value inside the file rather than the default standard output

    # setting the standard output to a file
    sys.stdout = open("country info.txt", "w")

    print("{0:^100}".format("COUNTRY DATA"))
    print('-'*100)
    print(
        "{0:^35}{1:^35}{2:^30}"
        .format("Country Name", 
        "Mobile subscriptions per capita", "Internet users per capita")
    )
    print('-'*100)

    for index in range(len(country_names)):
        print(
            "{0:<35}{1:^35}{2:^30}"
            .format(country_names[index], 
            mobile_subs_per_cap[index], net_users_per_cap[index])
        )

    sys.stdout.close()


# calling function
store_info()
