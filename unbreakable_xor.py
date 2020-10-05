"""Unbreakable XOR script
"""

def decode_message(input, key):
    """
    Takes an XOR ecoded hex string as input along with the key.
    Computes XOR for each hex with the key in a cyclic manner.
    Returns the decrypted message in ASCII.
    """
    hex_input_list = input.split()
    key = key.split()
    key_len = len(key)
    hex_input_len = len(hex_input_list)
    message = [chr(int(hex_input_list[i], 16) ^ int(key[i % key_len], 16)) 
                for i in range(hex_input_len)]
    return "".join(message)


if __name__ == "__main__":
    encrypted_message = """
    11 5a 01 3b 46 58 28 40 4e 3f 46 40 28 5c 58 74
    14 55 30 51 01 37 5a 44 75 40 48 35 51 01 28 55
    45 78 1c 6e 0c 64 08 78 5d 52 78 55 4f 78 51 4f
    3b 46 58 28 40 48 37 5a 01 2c 51 42 30 5a 48 29
    41 44 78 40 49 39 40 01 3b 55 4f 36 5b 55 78 56
    44 78 57 53 39 57 4a 3d 50 0d 78 56 54 2c 14 53
    3d 45 54 31 46 44 2b 14 55 30 51 01 2d 47 44 78
    5b 47 78 55 01 37 5a 44 75 40 48 35 51 01 28 46
    44 75 47 49 39 46 44 3c 14 4a 3d 4d 01 2c 5c 44
    78 47 40 35 51 01 2b 5d 5b 3d 14 40 2b 18 01 37
    46 01 34 5b 4f 3f 51 53 78 40 49 39 5a 0d 78 40
    49 3d 14 4c 3d 47 52 39 53 44 78 56 44 31 5a 46
    78 47 44 36 40 0f
    """
    key = "58 34 21"
    print("Dcrypted message:\n{0}".format(decode_message(encrypted_message,key)))
