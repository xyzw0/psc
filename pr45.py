#1
import re
str="The name of college is Indus"
x=re.findall("^The.*Indus$",str)
print(x)
['The name of college is Indus']
#2
import re
str="Good day"
x=re.findall(".*\s.*",str)
print(x)
['Good day']
#3
import re
str = "Abbbb ABBBB ABBB"
x = re.findall("AB{3}",str)
print(x)
['ABBB', 'ABBB']
#4
import re
str = "many moon massive mine"
x = re.findall(r"\b[m]\w{3}\b",str)
print(x)
['many', 'moon', 'mine']
#5
import re
str = "alive is okay aware all"
x = re.findall(r"\b[a]\w*\b",str)
print(x)
['alive', 'aware', 'all']
#6
import re
str="9times aaa 5bb"
x=re.findall(r"\b[\d]\w*\b",str)
print(x)
['9times', '5bb']
#7
import re
str = "man moon massive dam me makes"
x = re.findall(r"\b\w{5}\b",str)
print(x)
['makes']
#8
import re
str = "man moon massive dam me makes"
x = re.findall(r"\b\w{3,5}\b",str)
print(x)
['man', 'moon', 'dam', 'makes']
#9
import re
str="9times aaa 5bb"
x=re.findall(r"\d",str)
print(x)
['9', '5']
#10
import re
str = "Hello world hii"
x=re.findall(r"\w+\Z",str)
print(x)
['hii']
#11
import re
str = "annotation about akk"
x=re.findall(r"\bak\w*|an\w*\b",str)
print(x)
['annotation', 'akk']
#12
import re
str = "01/11/1999 born 10/12/1999"
x=re.findall("\d{2}/\d{2}/\d{4}",str)
print(x)
