import time
import numpy as np
import scipy
import scipy.io as sio

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
h_polarity_lovebot = []
h_polarity_hikari  = []

h_subjectivity = []
h_subjectivity_lovebot = []
h_subjectivity_hikari  = []

ii = 0
ii_total = 0
for i in msg:
  ii += 1
  t     = None
  t_sec = None

  n_str = i[0]
  n_num = None
  n_polarity = None
  n_polarity_lovebot = None
  n_polarity_hikari  = None
  n_subjectivity = None
  n_subjectivity_lovebot = None
  n_subjectivity_hikari  = None

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
 
  bb = i[1]

#  print(bb)

  if(do_flag):
    try:
      t       = time.strptime(bb,'%a %b %d %Y %I:%M:%S %p %z')
      #t       = time.strptime(bb,'%a %b %d %Y %I:%M:%S %p %z')
      t_sec   = time.mktime(t)
      do_flag = False
    except:
      pass

 
  if(do_flag):
    try:
      t       = time.strptime(bb,'%a %d %b %Y %I:%M:%S %p %z')
      #t       = time.strptime(bb,'%a %d %b %Y %I:%M:%S %p %z')
      t_sec   = time.mktime(t)
      do_flag = False
    except:
      pass 

  if(do_flag):
    try:
      t       = time.strptime(bb,'%a %d %b %Y %H:%M:%S %z')
      #t       = time.strptime(bb,'%a %d %b %Y %I:%M:%S %p %z')
      t_sec   = time.mktime(t)
      do_flag = False
    except:
      pass 

  if(do_flag):
    try:
      t       = time.strptime(bb,'%a %b %d %Y %H:%M:%S %z')
      #t       = time.strptime(bb,'%a %d %b %Y %I:%M:%S %p %z')
      t_sec   = time.mktime(t)
      do_flag = False
    except:
      pass 

  if(do_flag):
    try:
      t       = time.strptime(bb,'%a %d %b %H:%M:%S %z %Y')
      #t       = time.strptime(bb,'%a %d %b %Y %I:%M:%S %p %z')
      t_sec   = time.mktime(t)
      do_flag = False
    except:
      pass 

  if(do_flag):
    try:
      t       = time.strptime(bb,'%a %b %d %H:%M:%S %z %Y')
      #t       = time.strptime(bb,'%a %d %b %Y %I:%M:%S %p %z')
      t_sec   = time.mktime(t)
      do_flag = False
    except:
      pass 

  if(do_flag == False):
    pass
#    print(bb)

  if ( (t != None) & (t_sec != None) & (n_num != None) & (n_polarity != None) & (n_subjectivity != None) ):
    h_time.append(t)
    h_time_sec.append(t_sec)
    h_name_str.append(n_str)
    h_name_num.append(n_num)
    h_polarity.append(n_polarity)
    h_subjectivity.append(n_subjectivity)
    if (n_num == ENUM_HIKARI):
      h_polarity_hikari.append(n_polarity)
      h_subjectivity_hikari.append(n_subjectivity)
    elif (n_num == ENUM_LOVEBOT):
      h_polarity_lovebot.append(n_polarity)
      h_subjectivity_lovebot.append(n_subjectivity)




##  print('------------')
  if t == None:
    print('ii = ',end='')
    print(ii,end='')
    print(' - ',end='')
    print('fail t');
    ii_total += 1
  if t_sec == None:
    print('ii = ',end='')
    print(ii,end='')
    print(' - ',end='')
    print('fail t_sec');
    ii_total += 1
  if n_num == None:
    print('ii = ',end='')
    print(ii,end='')
    print(' - ',end='')
    print('fail n_num')
    ii_total += 1
  if n_polarity == None:
    print('ii = ',end='')
    print(ii,end='')
    print(' - ',end='')
    print('fail n_polarity')
    ii_total += 1
  if n_subjectivity == None:
    print('ii = ',end='')
    print(ii,end='')
    print(' - ',end='')
    print('fail n_subjectivity')
    ii_total += 1

##print(b)

##t = time.strptime(b,'%a %d %b %Y %I:%M:%S %p %z')
#t = time.strptime(b,'%a %d %b %Y %I:%M:%S %p %Z')

sio.savemat('./lovebot20221012Time.mat',                mdict={'lovebotTime': h_time_sec})
sio.savemat('./lovebot20221012Name.mat',                mdict={'lovebotName': h_name_num})
sio.savemat('./lovebot20221012Polarity.mat',            mdict={'lovebotPolarity': h_polarity})
sio.savemat('./lovebot20221012Subjectivity.mat',        mdict={'lovebotSubjectivity': h_subjectivity})

sio.savemat('./lovebot20221012PolarityLoveBot.mat',     mdict={'lovebotLoveBotPolarity':h_polarity_lovebot})
sio.savemat('./lovebot20221012PolarityHikari.mat',      mdict={'lovebotHikariPolarity':h_polarity_hikari})
sio.savemat('./lovebot20221012SubjectivityLoveBot.mat', mdict={'lovebotLoveBotSubjectivity':h_subjectivity_lovebot})
sio.savemat('./lovebot20221012SubjectivityHikari.mat',  mdict={'lovebotHikariSubjectivity':h_subjectivity_hikari})


print('Total errors = ',end='')
print(ii_total)
print(len(h_time))
print(len(h_time_sec))
print(len(h_name_str))
print(len(h_name_num))
print(len(h_polarity))
print(len(h_subjectivity))


lstart = 0
lend   = 50000

lb = h_subjectivity_lovebot[lstart:lend]
hi = h_subjectivity_hikari[lstart:lend]

cc = np.corrcoef(lb,hi)
print(cc)

crossc = np.correlate(lb,hi,mode='valid')
print(crossc)

print(np.max(crossc))
