import re
from datetime import datetime

mytext = str([
    '20080620033027/http://www.mrvc.indianrail.gov.in/overview.htm). _Official webpage of Mumbai Railway Vikas Corporation_. Archived from [the original](http://www.mrvc.indianrail.gov.in/overview.htm) on 2008-06-20. Retrieved 2008-12-11.'])

myregex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
x = re.findall(myregex, mytext)

result = []
for res in x:
    result.append(res.replace("www.", "").split('//')[-1].split('/')[0])

print(';'.join(result))

a = [x for x in range(3, 13)]
print(a)
value = []
print(value[0] if value else 0)

val = '2018,1'
date_object = datetime.strptime(val, '%Y,%m')

print(date_object.strftime("%b %y"))