expense = {"jan": 243, "feb": 788, "mar": 798, "aprl":78}

keys = list(expense)
for index in range(len(keys)):
    if index == 0:
        target_key = keys[index + 1]
        previous_key = keys[index]
        diff = expense[target_key] - expense[previous_key]

        print(diff)
        break



# if expense['feb'] > expense['jan']:
#     diff = expense['feb'] - expense['jan']
#     print(f"February has higher spend than january and the amount is ${diff}")
# elif expense['jan'] > expense['feb']:
#     diff = expense['jan'] - expense['feb']
#     print(f"January has higher spend than february and the amount is ${diff}")