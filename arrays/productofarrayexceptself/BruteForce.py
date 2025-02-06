# TC O(n^2)
# SC O(1)

def product_of_array(input_array):
    if not input_array:
        return []

    output_array = [0] * len(input_array) # initializing wih zeros

    for i in range(len(input_array)):
        running_product = 1
        for j in range(len(input_array)):
            if i != j:
                running_product *= input_array[j]
        output_array[i] = running_product

    return output_array

inputArray = [1, 2, 3, 4]
print(product_of_array(inputArray))
