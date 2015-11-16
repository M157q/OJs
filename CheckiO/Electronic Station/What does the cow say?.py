# http://www.checkio.org/mission/cowsay/

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

import re

def cowsay(text):
    text = re.sub(r'(\s+)', ' ', text)
    words = text.split(' ')

    def split_text_to_lines():
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(' ') + len(word) > 39:
                if len(current_line):
                    lines.append(current_line)
                current_line = word

                while len(current_line) > 39:
                    lines.append(current_line[:39])
                    current_line = current_line[39:]
            else:
                if word == '' or len(current_line) and current_line[-1] != ' ':
                    current_line += ' '
                current_line += word
        lines.append(current_line)

        return lines

    template = '{lq}{0:{padding}<{number}}{rq}'.format
    def get_text_and_max_chars():
        lines = split_text_to_lines()
        max_chars = max(map(len, lines))

        if len(lines) == 1:
            first_line = [template(lines[0], lq='< ', padding=' ', number=max_chars, rq=' >')]
            middle_lines = []
            last_line = []
        else:
            first_line = [template(lines[0], lq='/ ', padding=' ', number=max_chars, rq=' \\')]
            middle_lines = [template(line, lq='| ', padding=' ', number=max_chars, rq=' |') for line in lines[1:-1]]
            last_line = [template(lines[-1], lq='\\ ', padding=' ', number=max_chars, rq=' /')]

        return '\n'.join(first_line + middle_lines + last_line), max_chars


    text, max_chars = get_text_and_max_chars()
    top = template('', lq=' ', padding='_', number=max_chars+2, rq='')
    bottom = template('', lq=' ', padding='-', number=max_chars+2, rq='')

    return '''\n{}\n{}\n{}{}'''.format(top, text, bottom, COW)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
