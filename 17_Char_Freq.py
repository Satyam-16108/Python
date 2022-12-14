def calcFreqOfLetters(sentence):
    freq = {}
    for i in range(0, len(sentence), 1):
        letter = sentence[i].lower()
        if letter not in [' ', '.', ',', '\'', '\"', '!', ';']:
            if letter in freq.keys():
                freq[letter] += 1
            else:
                freq[letter] = 1
    return freq

if __name__ == "__main__":
    sentence = input('\nEnter a sentence:\n')
    freq = calcFreqOfLetters(sentence)
    
    print('\nFrequencies of each letter in the given sentence: ')
    for letter in freq:
        print('\'{}\' --> {}'.format(letter, freq[letter]))