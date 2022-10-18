close all
clear all
load lovebot20221012Name.mat
load lovebot20221012Polarity.mat
load lovebot20221012Subjectivity.mat
load lovebot20221012Time.mat
load lovebot20221012PolarityLoveBot.mat
load lovebot20221012PolarityHikari.mat
load lovebot20221012SubjectivityLoveBot.mat
load lovebot20221012SubjectivityHikari.mat


dt = diff(lovebotTime);

plot(dt,'.')

ylim([0,200])
xlabel('Response (n)');
ylabel('Delay Time (sec)');
title('Time Difference Between Responses');
shg

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






shg
