sentence = "the quick brown fox jump over the lazy dog. The dog smiles"

new_sentence = sentence.replace("dog", "Mastiff")
print("Original: ",sentence)
print("new: ", new_sentence)


name = "monty"
money = 73.6

print("{} has ${:.2f}".format(name , money))


my_text = "Anya Josephine Marie Taylor Joy"
name = my_text.split()

for index , name in enumerate(name):
    print("Index {} contains {} with {} in length ". format(index, name, len(name)))