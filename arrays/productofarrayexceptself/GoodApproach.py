# TC O(n)
# SC O(1)

def product_of_array(input):
    if not input:
        return []

    result = [0] * len(input)

    running_product = 1
    # Left pass
    for i in range(len(input)):
        result[i] = running_product
        running_product *= input[i]

    running_product = 1
    # Right pass
    for i in range(len(input) - 1, -1, -1):
        result[i] *= running_product
        running_product *= input[i]

    return result


inputArray = [1, 2, 3, 4]
print(product_of_array(inputArray))
