def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char  # non-alpha stays the same
    return decrypted

# Try all 25 shifts
cipher = "XRPCTCRGNEI"
for s in range(1, 26):
    print(f"Shift {s:2d}: {caesar_decrypt(cipher, s)}")

