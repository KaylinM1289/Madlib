from PyDictionary import PyDictionary

dictionary = PyDictionary()


def partOfSpeechChecker(word, wordMeaning):
    try:
        wordDefinition = dictionary.meaning(word)
        print(wordDefinition)
        if wordMeaning in wordDefinition:
            return 't'
        wordCheck = 't'
        while wordCheck == 't':
            word = input(f"That word is not correct, please type a(n) {wordMeaning} ").strip()
            wordDefinition = dictionary.meaning(word)
            print(wordDefinition)
            if wordMeaning in wordDefinition:
                return 't'
    except:
        word = input(f"That word is not a word, please type a(n) {wordMeaning} ").strip()
        partOfSpeechChecker(word, wordMeaning)


def madLibGenerator():
    continueMadLib = 'y'

    while continueMadLib.lower() == 'y' or continueMadLib.lower() == 'yes':
        noun1 = input("Please type a Noun ").strip()
        partOfSpeechChecker(noun1, "Noun")

        verb1 = input("Please type an Verb ").strip()
        partOfSpeechChecker(verb1, "Verb")

        noun2 = input("Please type another noun ").strip()
        partOfSpeechChecker(noun2, "Noun")

        adjective1 = input("Please type an Adjective ").strip()
        partOfSpeechChecker(adjective1, "Adjective")

        evilGenius1 = f'Little Timmy went down to the {noun1} to {verb1}. When he got there he found a {noun2} laying next to the {adjective1} river.'
        print(evilGenius1)
        continueMadLib = input("Keep mad-libbing? (y/n) ")
