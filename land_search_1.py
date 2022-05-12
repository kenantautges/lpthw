#Starting to write code for finding land for sale in the great land of Tennessee

# minimum number of acres I'd like to purchase
acres = 50
# maximum price I'm willing to pay for raw land
price = 99999.99
# number of counties I'm willing to consider surrounding the target county
counties = 2
# minimum acre of land space per human
human_space = 5
# how many tractors will be needed?
tractors_needed = acres / human_space
# how many chickens we expect to have
chickens = acres - human_space


# prints a statement and includes the defined variable in between the text strings.
print("There are", acres, "acres available for sale for $", price, ".")
print("Approximately", counties, "counties have", acres, "acre plots for sale on a regular basis.")
print("Tractors are a necessity, approximately", tractors_needed, "due to total number of humans,", human_space, "on the plot.")
print("We obviously need", chickens, "chickens +", tractors_needed, "tractors in order for this farm to be sustainable.")
