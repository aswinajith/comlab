import matplotlib.pyplot as plt
import numpy as np
# Convert a decimal number to BCD
def decimal_to_bcd(n):
    return " ".join(f"{int(digit):04b}" for digit in str(n))

# Convert BCD to Excess-3
def bcd_to_excess3(bcd):
    return " ".join(f"{int(group, 2) + 3:04b}" for group in bcd.split())

# Input number
num = 19223

# Convert to BCD
bcd_code = decimal_to_bcd(num)

# Convert BCD to Excess-3
excess3_code = bcd_to_excess3(bcd_code)

# Print Results
print(f"BCD of {num}: {bcd_code}")
print(f"Excess-3 Code: {excess3_code}")

