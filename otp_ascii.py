import secrets

# Function to count number of 0s and 1s
def count_bits(binary):
    zeros = binary.count('0')
    ones = binary.count('1')
    return zeros, ones

# Convert ASCII string to binary
def ascii_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Convert binary back to ASCII
def binary_to_ascii(binary):
    chars = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

# XOR operation for OTP
def xor_bits(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

# Generate random bit string
def generate_random_bits(n):
    return ''.join(str(secrets.randbelow(2)) for _ in range(n))

def main():

    # Ask user for security parameter
    n = int(input("Enter security parameter n: "))

    # Generate OTP key
    key = generate_random_bits(n)

    while True:
        message = input("Enter a message: ")
        binary_message = ascii_to_binary(message)

        if len(binary_message) <= n:
            break
        else:
            print("Message too long. Please enter a shorter message.")

    print("\nBinary message:")
    print(binary_message)

    zeros, ones = count_bits(binary_message)
    print("Zeros:", zeros, "Ones:", ones)

    # Encrypt
    ciphertext = xor_bits(binary_message, key[:len(binary_message)])

    print("\nEncrypted binary:")
    print(ciphertext)

    zeros, ones = count_bits(ciphertext)
    print("Zeros:", zeros, "Ones:", ones)

    # Convert encrypted bits to characters
    encrypted_chars = binary_to_ascii(ciphertext)
    print("\nEncrypted characters:")
    print(encrypted_chars)

    # Decrypt
    decrypted_bits = xor_bits(ciphertext, key[:len(ciphertext)])

    print("\nDecrypted binary:")
    print(decrypted_bits)

    zeros, ones = count_bits(decrypted_bits)
    print("Zeros:", zeros, "Ones:", ones)

    decrypted_message = binary_to_ascii(decrypted_bits)
    print("\nDecrypted message:")
    print(decrypted_message)


if __name__ == "__main__":
    main()
