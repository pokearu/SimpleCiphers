"""Vignere Cipher script
"""

def encode_message(message,key):
    """
    Takes a message and a cipher key as input.
    Uses the algebric expression Ci = (Mi + Ki) mod 26 to encrypt the message.
    Converts the characters to ASCII and returns the cipher.
    """
    message_len = len(message)
    key_len = len(key)
    cipher = [chr(ord('A') + ((ord(message[i]) + ord(key[i % key_len])) % 26)) 
                for i in range(message_len)]
    return "".join(cipher)


def decode_message(input,key):
    """
    Takes a encoded input and a cipher key as input.
    Uses the algebric expression Mi = (Ci - Ki + 26) mod 26 to decrypt the message.
    Converts the characters to ASCII and returns the message.
    """
    input_len = len(input)
    key_len = len(key)
    message = [chr(ord('A') + ((ord(input[i]) - ord(key[i % key_len]) + 26) % 26)) 
                for i in range(input_len)]
    return "".join(message)


if __name__ == "__main__":
    encrypted_input = 'WWPEJRJXEOETEDXHTSZGTDGLAAN'
    key = 'APPLE'
    message = decode_message(encrypted_input,key)
    print("Decoded message: {0}\nEncoded message: {1}".format(message,encode_message(message,key)))
