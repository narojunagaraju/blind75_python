# TC O(n)
# SC O(1)

def product_of_array(input):
    n = len(input)
    prefix_products = [0] * n
    suffix_products = [0] * n
    output = [0] * n

    prefix_product = 1
    for i in range(n):
        prefix_products[i] = prefix_product
        prefix_product *= input[i]

    suffix_product = 1
    for i in range(n - 1, -1, -1):
        suffix_products[i] = suffix_product
        suffix_product *= input[i]

    for i in range(n):
        output[i] = prefix_products[i] * suffix_products[i]

    return output

inputArray = [1, 2, 3, 4]
print(product_of_array(inputArray))