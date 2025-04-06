def smallest_average(person1: dict, person2: dict, person3: dict):
    average1 = (person1['result1'] + person2['result2'] + person3['result3']) / 3
    average2 = (person1['result1'] + person2['result2'] + person3['result3']) / 3
    average3 = (person1['result1'] + person2['result2'] + person3['result3']) / 3
    if average1 < average2 and average1 < average3:
        return person1
    elif average2 < average1 and average2 < average3:
        return person2
    else:
        return person3
person1 = {'name': 'Alice', 'result1': 8, 'result2': 6, 'result3': 9}
person2 = {'name': 'Bob', 'result1': 7, 'result2': 9, 'result3': 8}
person3 = {'name': 'Charlie', 'result1': 5, 'result2': 6, 'result3': 7}
print(smallest_average(person1, person2, person3))