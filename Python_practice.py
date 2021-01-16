#print("Hello World")
#How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
# Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
#Calculate the percentage of votes you received.
#percentage_votes = (my_votes/total_votes) *100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#print(f"I received {my votes/total_votes *100}% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# #What is the score?
# score = int(input("what is your test score? "))
# #Determine the grade
# if score >= 90:
#     print('Your grade is an A')
# elif score >= 80:
#     print('Your grade is a B')
# elif score >= 70:
#     print('Your grade is a C')
# elif score >= 60:
#     print('Your grade is a D')
# else:
#     print('Your grade is an F')

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

#range function
# for i in range(len(counties)):
#     print(counties[i])

#dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#keys
# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

#values
# for voters in counties_dict.values():
#     print(voters)

# for county, voters in counties_dict.items():
#     print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
#print just registered voters
for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)