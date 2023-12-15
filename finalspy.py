#develop a py prg to sort hte contents of a text file n write thtat sorted contents in to separate file(txt)
filename=input("enyter the filename")
fileObj=open(filename,'r')
text=fileObj.read()
words=text.split()
fileObj.close()
print