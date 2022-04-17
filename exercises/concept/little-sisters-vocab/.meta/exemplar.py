"""Functions for checking little sister's vocabulary homework."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix to the start of it.

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Take a list containing a prefix at the first index, words as the rest, and prepend each word with it.

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """

    prefix = vocab_words[0]
    joiner = ' :: ' + prefix

    return joiner.join(vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix 'ness' from the word while considering resulting words that end in 'y'.

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    word = word[:-4]
    if word[-1] == 'i':
        word = word[:-1] + 'y'

    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    word = sentence.split()[index]

    if word[-1] == '.':
        word = word[:-1] + 'en'
    else:
        word = word + 'en'

    return word
