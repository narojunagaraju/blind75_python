# TC O(n * m)
# SC O(1)

def main():
    input_list = ["Hello", "World"]
    encoded_string = encode(input_list)
    print(encoded_string)
    decoded_list = decode(encoded_string)
    print(decoded_list)

def encode(input_list):
    return "|".join(input_list)

def decode(encoded_string):
    return encoded_string.split("|")

if __name__ == "__main__":
    main()
