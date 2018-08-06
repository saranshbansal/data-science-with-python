import re

str = '101010'
pattern = '0'
repl_str = '2'

result = re.sub(pattern, repl_str, str)

print(result)