import locale


def init_program():
    # decimal seperator in germany is , - useful for floats
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
