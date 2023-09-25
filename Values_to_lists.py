def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for values in aDict.values():
        result += len(values)
    return result

        
# Example dictionary where all values are lists
my_dict = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': [6]
}

# Call the how_many function with the example dictionary
result = how_many(my_dict)

# Print the result
print(result)

        
        