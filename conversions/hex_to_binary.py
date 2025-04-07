# Function to convert Hexadecimal to Binary
def hex_to_binary(hex_num):
    # Convert hex to integer, then to binary, and remove the '0b' prefix
    binary_num = bin(int(hex_num, 16))[2:]
    return binary_num

# Example usage
hex_number = input("Enter a hexadecimal number: ")
binary_output = hex_to_binary(hex_number)

print(f"Binary equivalent: {binary_output}")
