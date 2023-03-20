import re

# text -> text

# meta symbols

# []
# [abc] -> a || b ||c => [a-c] => [a-zA-Z]
# [abc\] -> a || b || c || \

# \d => [0-9]
# \D => [^0-9]
# \s => [\t\n ]
# \S => [^ \n\t]
# \w => [a-zA-Z0-9_]
# \W => [^a-zA-Z0-9_]

# . => [^\n]
# $ - чи рядок закінчується відповідно до шаблону
# * -> >=0 matches
# + -> >=1 matches
# ? -> 0-1 matches
# {n} -> n matches


# |
# ^ - not , find from start

# re.compile()
pattern = re.compile('abc')
print(pattern)

# match()
res = pattern.match('abcdf')
print(res)
res = pattern.match('bacdf')
print(res)
res = pattern.match('cdfabc')
print(res)

# search()
pattern_2 = re.compile("msg")
res = pattern_2.search('msg1')
print(res)

res = pattern_2.search('another msg1')
print(res)

res = pattern_2.search('another msg1 msg')
print(res)

# findall()
pattern_3 = re.compile("msg")
res = pattern_3.findall('another msg1 msg')
print(res)

# finditer()
res = pattern_3.finditer('another msg1 msg')
print(res)
for i in res:
    print(i.span())
    print(i.group())
    print(i.start())
    print(i.end())


# split(str, maxsplit)

pattern = re.compile('\W')
result = pattern.split('this is a test string')
print(result)
result = pattern.split('this is a test string', 2)
print(result)
result = re.split('\W', 'this is a test string', 2)
print(result)

# sub(replace, str, count)
pattern = re.compile('(blue|red|yellow)')
res = pattern.sub('color', 'one red two yellow three green')
print(res)

res = re.sub('(blue|red|yellow)', 'color', 'one red two yellow three green' )
print(res)

# subn()
pattern = re.compile('(blue|red|yellow)')
res = pattern.subn('color', 'one red two yellow three green', count=1)
print(res)


pattern = 'a'
demo_str = "This is a demo string for count a"
result = re.findall(pattern, demo_str)
print(len(result))

demo_str = "test string to find test"
pattern = "test"

res = re.search('test$', demo_str)
print(res)
res = re.search('^test', demo_str)
print(res)
res = re.match('(^test.*test$)', demo_str)
print(res)
res = re.search('(^test|test$)', "string to find test")
print(res)


res = re.search('[0-9+]', "this is demo string 1 1")
print(res)

res = re.search('.*[0-9]*', "this is demo string 1")
print(res)

res = re.search('.*[0-9]?', "this is demo string 1")
print(res)

demo = "http://site.com"
pattern = "^http://.*\.com"

result = re.search(pattern, "http://demourl.comkjbhjb")
print(result)

demo_str= "date1 = 12-05-2022 date2= 21.09.2021"
pattern = '\d{2}[-./]\d{2}[-./]\d{4}'
result = re.findall(pattern, demo_str)
print(result)

demo_str = "This is a demo string to find all words"
result = re.findall(r'\b[aeioAEIO]\w*', demo_str)
print(result)

pattern = '[,.\/ ]'
demo_str = "this?is/string.to,split"
result = re.split(pattern, demo_str)
print(result)