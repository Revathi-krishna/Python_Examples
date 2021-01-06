# Print the names in ascending order who tweeted the most along with the count
from collections import Counter

# No of test cases
no_of_test_cases = int(input())
# each test case input- list in list like- [[arun,arun,balu,chintu],[arun,dravid,dravid,goutham,jhony]]
input_list = [[]] * no_of_test_cases
for i in range(0, no_of_test_cases):
    # count of the persons who tweeted
    y = int(input())
    m = []
    for j in range(0, y):
        # Persons tweeted
        m.append(input())
    input_list[i].append(m)
# actual code
for i in range(0, no_of_test_cases):
    # loop through each test case
    tweet_names = input_list[i][i]
    unique_names = []
    for pref_names in tweet_names:
        # splitting name with other data and storing in list
        unique_names.append(pref_names.split()[0])

    # store unique_names in times variable
    times = Counter(unique_names)
    # fetch values from dict
    repeat = times.values()
    # convert dict values to list
    some = list(repeat)
    # sort the values
    some.sort()
    # getting max count
    s = max(some)
    k = []
    # converting times to dict
    mtg = dict(times)
    for key, value in mtg.items():
        if value is s:
            # fetching the name of the maximum tweeted person and putting in list
            k.append(key)
    # sort the names in ascending order
    k.sort()
    for u in k:
        # print the list of names who tweeeted the most with thier maximum count
        print(u + ' ' + str(s))
