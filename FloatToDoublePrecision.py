import struct

def float_to_double_precision_bits(value):
    # Use 'd' format for double-precision floating-point number.
    # '>' indicates big-endian byte order.
    packed = struct.pack('>d', value)
    print(f"Packed value: {packed}")
    
    # Convert each byte to its corresponding binary representation.
    bits = ''.join(format(byte, '08b') for byte in packed)
    print(f"Binary representation: {bits}")
    
    return bits

def convert_and_display():
    value = float(input("Enter a number to convert: "))
    print(f"Original value: {value}")
    
    bits = float_to_double_precision_bits(value)
    
    # Display the original value and its IEEE 754 double-precision representation.
    print(f"IEEE 754 double-precision format (64 bits): {bits}")

# Example usage
convert_and_display()