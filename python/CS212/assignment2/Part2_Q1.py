# initialise lists for data storage
country_names = []
population_list = []
percent_literacy_rate = []
mobile_subs_num = []
net_users_num = []
electricity_prod_amt = []
electricity_consump_amt = []


# open csv and store corresponding data into lists
with open("CountryData.csv") as file:
    for item in file.readlines():
        item_ = item.strip()
        data = item_.split(',')

        # add condition to not include headers in the lists
        if "Population" not in data:
            country_names.append(data[0])
            population_list.append(int(data[1]))
            percent_literacy_rate.append(int(data[2]))
            mobile_subs_num.append(int(data[3]))
            net_users_num.append(int(data[4]))
            electricity_prod_amt.append(int(data[5]))
            electricity_consump_amt.append(int(data[6]))


# make a dictionary to have the country names as keys and their indices as values
country_names_dict = {}
for index, country in enumerate(country_names):
    country_names_dict[country] = index
