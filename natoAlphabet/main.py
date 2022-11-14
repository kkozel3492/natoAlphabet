import pandas

natoData = pandas.read_csv('nato_phonetic_alphabet.csv')
natoDict = {row.letter:row.code for (index, row) in natoData.iterrows()}




word = input("enter a word: ").upper()
outputList = [natoDict[letter] for letter in word]
print(outputList)