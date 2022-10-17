close all
clear all
load lovebot20221012Name.mat
load lovebot20221012Polarity.mat
load lovebot20221012Subjectivity.mat
load lovebot20221012Time.mat

dt = diff(lovebotTime);

plot(dt,'.')

ylim([0,200])
xlabel('Response (n)');
ylabel('Delay Time (sec)');
title('Time Difference Between Responses');
shg

figure

hist(dt,10);
shg
