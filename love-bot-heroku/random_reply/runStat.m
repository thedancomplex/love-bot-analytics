close all
clear all
%load lovebot20221012Name.mat
%load lovebot20221012Polarity.mat
%load lovebot20221012Subjectivity.mat
%load lovebot20221012Time.mat
%load lovebot20221012PolarityLoveBot.mat
%load lovebot20221012PolarityHikari.mat
%load lovebot20221012SubjectivityLoveBot.mat
%load lovebot20221012SubjectivityHikari.mat
%load lovebot20221012ReplyTimeHikari.mat
%load lovebot20221012ReplyTimeLoveBot.mat
%load lovebot20221012Dt.mat
load lovebot20221012.mat
dt = diff(lovebotTime);

figure
plot(dt,'.')
ylim([0,200])
xlabel('Response (n)');
ylabel('Delay Time (sec)');
title('Time Difference Between Responses');


figure
plot(lovebotDt,'r.')
ylim([0,200])
xlabel('Response (n)');
ylabel('Delay Time (sec)');
title('Time Difference Between Responses (python)');


figure
hist(dt,10);

figure
hist(lovebotPolarity)
xlabel('Polarity')
ylabel('Number of Occurances')
title('Polarity of Conversitions')

figure
hist(lovebotLoveBotPolarity)
xlabel('Polarity')
ylabel('Number of Occurances')
title('Polarity of Conversitions Sent by Love-Bot')

figure
hist(lovebotHikariPolarity)
xlabel('Polarity')
ylabel('Number of Occurances')
title('Polarity of Conversitions Sent by Hikari')






figure
hist(lovebotSubjectivity)
xlabel('Subjectivity')
ylabel('Number of Occurances')
title('Subjectivity of Conversations')

figure
hist(lovebotLoveBotSubjectivity)
xlabel('Subjectivity')
ylabel('Number of Occurances')
title('Subjectivity of Conversations Sent by Love-Bot')

figure
hist(lovebotHikariSubjectivity)
xlabel('Subjectivity')
ylabel('Number of Occurances')
title('Subjectivity of Conversations Sent by Hikari')


figure
hist(lovebotHikariReplyTime,100000)
xlabel('Delay Time (ms)')
ylabel('Number of Occurances')
xlim([0,200])
title('Delay Time of Messages from Love-Bot to Hikari')


figure
hist(lovebotLoveBotReplyTime,1000000)
xlabel('Delay Time (ms)')
ylabel('Number of Occurances')
title('Delay Time of Messages from Hikari to Love-Bot')
xlim([0,200])
shg
