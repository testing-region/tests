# load the dataset
load("./Ghana_r8");

# assign the variables to be used
vars = c("Q41N_GHA", "Q41O_GHA", "Q41P_GHA", "Q41M_GHA");

# create a new data frame with the variables
my_data = data.frame(Ghana_r8[vars]);

# save the data frame
save(my_data, file = "./my_data.RData");

load("./my_data.RData");
my_data;

library(descr);
freq(my_data$Q41N_GHA);


# Encode data values
# 0 = "Not at all"
# 1 = "Just a little"
# 2 = "Somewhat"
# 3 = "A lot"
# 8 = "Refused"
# 9 = "Don't know"
# -1 = "Missing"

my_data$Q41N_GHA[my_data$Q41N_GHA == "Refused"] = NA;
my_data$Q41N_GHA[my_data$Q41N_GHA == "Missing"] = NA;
freq(my_data$Q41N_GHA);

my_data$Q41O_GHA[my_data$Q41O_GHA == "Refused"] = NA;
my_data$Q41O_GHA[my_data$Q41O_GHA == "Missing"] = NA;
freq(my_data$Q41O_GHA);

my_data$Q41P_GHA[my_data$Q41P_GHA == "Refused"] = NA;
my_data$Q41P_GHA[my_data$Q41P_GHA == "Missing"] = NA;
freq(my_data$Q41P_GHA);

my_data$Q41M_GHA[my_data$Q41M_GHA == "Refused"] = NA;
my_data$Q41M_GHA[my_data$Q41M_GHA == "Missing"] = NA;
freq(my_data$Q41M_GHA);

my_data = data.frame(my_data);
save(my_data, file = "./my_data.RData");

my_data;
View(my_data)
