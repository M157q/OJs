#!/usr/bin/env python3

# https://py.checkio.org/mission/cipher-map2/


def recall_password(cipher_grille, ciphered_password):
    password = ''

    for _ in range(4):
        for flag_for_selected, password_char in zip(''.join(cipher_grille), ''.join(ciphered_password)):
            password += password_char if flag_for_selected == 'X' else ''

        # rotate 90 degrees clock-wise for cipher_grille
        cipher_grille = tuple(map(''.join, zip(*cipher_grille[::-1])))

    return password


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
