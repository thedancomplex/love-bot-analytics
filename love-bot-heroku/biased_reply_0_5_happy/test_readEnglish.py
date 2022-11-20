import time

ENUM_HIKARI  = 1
ENUM_LOVEBOT = 2

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
n = msg[1000][0]
print(n)

h_time         = []
h_time_sec     = []
h_name_num     = []
h_name_str     = []
h_polarity     = []
h_subjectivity = []
for i in msg:
  t     = -1
  t_sec = -1

  n_str = i[0]
  n_num = None
  n_polarity = None
  n_subjectivity = None

  n_score = i[2]

  try:
    n_score_split = n_score.split(' ')
    n_polarity = float(n_score_split[0])
    n_subjectivity = float(n_score_split[1])
  except:
    pass

  if ( n_str == 'Hikari' ):
    n_num = ENUM_HIKARI
  elif ( n_str == 'Love-Bot'):
    n_num = ENUM_LOVEBOT


  do_flag = True
  
  if(do_flag):
    try:
      t     = time.strptime(i[1],'%a %d %b %Y %I:%M:%S %p %z')
      t_sec = time.mktime(t)
      do_flag = False
    except:
      pass 

  if(do_flag):
    try:
      t     = time.strptime(i[1],'%a %b %d %Y %I:%M:%S %p %z')
      t_sec = time.mktime(t)
      do_flag = False
    except:
      pass

  if(do_flag == False):
#    print(i[1]i)
    pass

  if ( (t != None) & (t_sec != None) & (n_num != None) & (n_polarity != None) & (n_subjectivity != None) ):
    h_time.append(t)
    h_time_sec.append(t_sec)
    h_name_str.append(n_str)
    h_name_num.append(n_num)
    h_polarity.append(n_polarity)
    h_subjectivity.append(n_subjectivity)

##print(b)

##t = time.strptime(b,'%a %d %b %Y %I:%M:%S %p %z')
#t = time.strptime(b,'%a %d %b %Y %I:%M:%S %p %Z')


bb = 'Sat 25 Jun 2022 09:30:10 AM -0400'
bbb = 'Sat 25 Jun 2022 09:30:10 AM +0900'
t     = time.strptime(bb,'%a %d %b %Y %I:%M:%S %p %z')
tb     = time.strptime(bbb,'%a %d %b %Y %I:%M:%S %p %z')
t_sec = time.mktime(t)
tb_sec = time.mktime(tb)
print('--------------')
print(t)
print(tb)
print(t_sec)
print(tb_sec)
print('--------------')

print(h_time[100])

print(time.mktime(h_time[100]))

print(len(h_time))
print(len(h_time_sec))
print(len(h_name_str))
print(len(h_name_num))
print(len(h_polarity))
print(len(h_subjectivity))
