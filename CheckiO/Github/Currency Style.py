# https://checkio.org/mission/currency-style/


def checkio(text):
    "Convert Euro style currency in dollars to US/UK style"
    import re
    pattern = re.compile(
        r'''
            (
                \$\d{1,3}
                (\.\d{3})*
                (\,\d{1,2})?
            )
            (\ |$|\.|,|\n)
        ''',
        re.X,
    )
    s = re.sub(
        pattern,
        lambda x: x.group(1).translate(str.maketrans('.,', ',.')) + x.group(4),
        # r'(\$\d{1,3}(\.\d{3})*(\,\d{1,2})?)(?!\d)',
        # lambda x: x.group(0).translate(str.maketrans('.,', ',.')),
        text,
    )
    return s

if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing

    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
        "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
        "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
        "$1,234, $5,678 and $9", "Dollars without cents"
