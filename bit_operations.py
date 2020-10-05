"""Bit operations script
"""

def nibble_swap(ele):
    """
    Take an integer as input and returns the nibbles swapped.
    """
    return (ele & 0x0F)<<4 | (ele & 0xF0)>>4

def decode_message(input):
    """
    Takes an encoded string as input.
    XOR each byte with '0x47' and nibble swaps each result.
    Returns the decrypted message in ASCII.
    """
    hex_input_list = input.split()
    hex_input_len = len(hex_input_list)
    message = [chr(nibble_swap(int(hex_input_list[i], 16) ^ int('0x47', 16)))
                for i in range(hex_input_len)]
    return "".join(message)
    

if __name__ == "__main__":
    encrypted_message = """
    02 30 b1 45 a1 d1 61 61 81 11 70 45 91 51 f1 11
    45 51 45 61 d0 00 11 a5
    """
    print("Decoded message:\n{0}".format(decode_message(encrypted_message)))
