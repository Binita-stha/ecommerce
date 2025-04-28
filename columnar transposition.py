import math

key = "security"


# Encryption
def encryptMessage(msg):
    cipher = ""
    # Track key indices
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # Calculate column of the matrix
    col = len(key)

    # Calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # Add padding character '_' in empty cells
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # Create matrix and insert message and padding row-wise
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    # Read matrix column-wise using key order
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher


# Decryption
def decryptMessage(cipher):
    msg = ""

    # Track key indices
    k_indx = 0
    # Track message indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # Calculate column and row
    col = len(key)
    row = int(math.ceil(msg_len / col))

    # Convert key into sorted list
    key_lst = sorted(list(key))

    # Create an empty matrix to store decrypted message
    dec_cipher = [[None] * col for _ in range(row)]

    # Arrange the matrix column-wise according to the key order
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # Convert decrypted message matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))  # Flatten the matrix
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    # Remove padding characters '_'
    null_count = msg.count('_')
    if null_count > 0:
        return msg[:-null_count]

    return msg


# Example Usage
message = "Hello World"
print("Original Message:", message)

encrypted_text = encryptMessage(message)
print("Encrypted Message:", encrypted_text)

decrypted_text = decryptMessage(encrypted_text)
print("Decrypted Message:", decrypted_text)
