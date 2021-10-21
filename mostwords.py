#program that counts the most common words in a text file.
file=open(input('enter file name: '))
list_words=list()
dict_words=dict()
for line in file:
    line=line.rstrip()
    line=line.split()
    for word in line:
        dict_words[word]=dict_words.get(word,0)+1
for k,v in dict_words.items():
    list_words.append((v,k))
list_words.sort(reverse=True)
for v,k in list_words:
    print(k,v)
