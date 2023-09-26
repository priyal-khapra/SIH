import PyPDF2
a = PyPDF2.PdfReader('writ format.pdf')
print(len(a.pages))
str = " "
for i in range(0,len(a.pages)):
    str += a.pages[i].extract_text()
#print(str)
with open("text.txt","w",encoding='utf-8') as f:
    f.write(str)

