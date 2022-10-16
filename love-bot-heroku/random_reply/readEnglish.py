import time

the_name = 'upto_20221012/conversation.english.log.fix'

lines = None
with open(the_name) as f:
  lines = f.readlines()

print(len(lines))
print(lines[0])


msg = []
for i in lines:
  msg.append(i.split(' : '))

#msg = lines.split(' : ')

b = msg[1000][1]

print(b)

t = time.strptime(b,'%a %d %b %Y %I:%M:%S %p %z')
#t = time.strptime(b,'%a %d %b %Y %I:%M:%S %p %Z')

print(t)

print(time.mktime(t))
