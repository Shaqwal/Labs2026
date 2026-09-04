def xor_bytes(b1, b2):
    return bytes(b ^ k for b, k in zip(b1, b2))

print("=== ЛАБОРАТОРНАЯ РАБОТА № 7 ===")
text_lab7 = "С Новым Годом, друзья!"
b_text7 = text_lab7.encode('cp1251')

# Делаем ключ длиной ровно под весь текст (22 байта)
key_lab7 = b'\x05\x0c\x17\x7f\x0e\x4e\x37\xd2\x94\x10\x09\x2e\x22\x57\xff\xc8\x0b\xb2\x70\x54\xaa\xbb'

cipher_lab7 = xor_bytes(b_text7, key_lab7)
decrypted_lab7 = xor_bytes(cipher_lab7, key_lab7)

print("Исходный текст:      ", text_lab7)
print("Шифротекст (HEX):    ", cipher_lab7.hex())
print("Расшифровано:        ", decrypted_lab7.decode('cp1251', errors='ignore'))


print("\n=== ЛАБОРАТОРНАЯ РАБОТА № 8 ===")
p1 = "НаВашисходящийот1204".encode('cp1251')
p2 = "ВСеверныйфилиалБанка".encode('cp1251')

k = bytes([
    0x05, 0x0C, 0x17, 0x7F, 0x0E, 0x4E, 0x37, 0xD2, 0x94, 0x10,
    0x09, 0x2E, 0x22, 0x57, 0xFF, 0xC8, 0x0B, 0xB2, 0x70, 0x54
])

c1 = xor_bytes(p1, k)
c2 = xor_bytes(p2, k)

print("Открытый текст 1 (P1):", p1.decode('cp1251'))
print("Открытый текст 2 (P2):", p2.decode('cp1251'))
print("Шифротекст 1 (C1):   ", c1.hex())
print("Шифротекст 2 (C2):   ", c2.hex())

# Анализ уязвимости без ключа: C1 XOR C2 = P1 XOR P2
c1_xor_c2 = xor_bytes(c1, c2)
recovered_p2 = xor_bytes(c1_xor_c2, p1)

print("Восстановленный P2:  ", recovered_p2.decode('cp1251', errors='ignore'))
