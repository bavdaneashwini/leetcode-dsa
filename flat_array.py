input = [1,[4,[6]], 2, [3, [5, [7],7]]]

#Python function to flatten a nested array
def flat_array(input_array):
    ans = []
    for item in input_array:
        if isinstance(item, int):
            ans.append(item)
        else:
            ans.extend(flat_array(item))
    return ans

res = flat_array(input)
print(res)