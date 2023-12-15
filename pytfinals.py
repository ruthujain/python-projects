#develop a prg to print 10 most frequently appearing words in a text file.use dictionaries with distinct words n their frequencys of occurance in reverse order of frewuency n display dictionary slic of 10
filename=input("enter filename")
file=open(filename,'r')
text=file.read()
words=text.split()
word_freq={}
for word in words:
    word_freq=[word]=word_freq.get(word,0)+1
print(word_freq)
sorted_dict=sorted([(value,key) for (key,value) in word_freq.iterms()],reversed==True)
print(sorted_dict[0:10])
#ye  mane freq of 10 aur zip files ka baad mein karenge abhi ke liye ham sirf ye sorting of twxt from one text file and the printing it to another well do and then complex nos air fir student then we'll do this whole step revising kinda like codin ka blurting and then we'll figure it out i m so lucky to be able to learn theses stuff