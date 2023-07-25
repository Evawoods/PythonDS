def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    # without built in method
    return phrase[0].upper() + phrase[1:]

    # built in method
    # return phrase.capitalize()
