# http://www.checkio.org/mission/vigenere-cipher/


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    repeated_key_chars = tuple(
        chr(ord('A') + ((ord(old_encrypted[i]) - ord(old_decrypted[i])) % 26))
        for i in range(len(old_encrypted))
    )
    repeated_key = ''.join(repeated_key_chars)

    for i in range(1, len(repeated_key)+1):
        key = repeated_key[:i]
        old_decrypted_chars = []
        for j in range(len(old_encrypted)):
            d = (ord(old_encrypted[j]) - ord(key[j % len(key)])) % 26
            old_decrypted_char = chr(ord('A') + d)
            old_decrypted_chars.append(old_decrypted_char)

        if ''.join(old_decrypted_chars) == old_decrypted:
            break

    new_decrypted_chars = []
    for i in range(len(new_encrypted)):
        d = (ord(new_encrypted[i]) - ord(key[i % len(key)])) % 26
        new_decrypted_char = chr(ord('A') + d)
        new_decrypted_chars.append(new_decrypted_char)
    new_decrypted = ''.join(new_decrypted_chars)

    return new_decrypted


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
