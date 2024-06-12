###Create an application that takes in list(use a dict inside a list ) 
# Dictorianaries and perform the following function join,split and replace

def process_text(Sentence,reolacemnet):
    words=sentence.split()
    print(f"slipt words:{words}")

words.reverse()
print(f"Reversed words :{words}")

reversed_words= " ".join(words)
print(f"Reversed sentence :{words}")

for old_word,new_word in replacements.items():
    reversed_sentence=reversed_sentence.replace(old_word,new_word)
print(f"Replaced words sentence: {reversed_sentence}")

return reversed_sentence
sentence=input("enter sentence :")
replacement_num = int(input("how many do you want to replace"))

replacements={}

for _ in range(replacement_num):
    old_word=input("Enter replacement word :")
    new_word=input("Enter the new word: ")
    replacement[old_word]=new_word

final_sentence=process_text(sentence,replacements)
print(f"Final sentence replaced : {final_sentence}")    

