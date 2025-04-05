# TC O(n * m)
# SC O(1)

def main():
    input_list = ["Hello", "World"]
    encoded_string = encode(input_list)
    print(encoded_string)
    decoded_list = decode(encoded_string)
    print(decoded_list)

def encode(strs):
    encoded = []
    for s in strs:
        encoded.append(f"{len(s)}/{s}")
    return "".join(encoded)

def decode(s):
    decoded = []
    i = 0
    while i < len(s):
        slash_index = s.find('/', i)
        length = int(s[i:slash_index])
        str_part = s[slash_index + 1: slash_index + 1 + length]
        decoded.append(str_part)
        i = slash_index + 1 + length
    return decoded

if __name__ == "__main__":
    main()
