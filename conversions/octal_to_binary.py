def octal_to_binary(octal_num):
    binary_str = ""
    octal_to_bin_map = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }

    for digit in str(octal_num):  # Convert each octal digit to binary
        binary_str += octal_to_bin_map[digit]

    return binary_str.lstrip('0')  # Remove leading zeros

# Example usage
octal_num = input("Enter an octal number: ")
binary_result = octal_to_binary(octal_num)
print(f"Binary equivalent: {binary_result}")
