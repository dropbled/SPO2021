%#####################some needed shit##################################
myev3 = legoev3('wifi','IP','ID');
motorA = motor(myev3,'A')
motorB = motor(myev3,'B')
motorC = motor(myev3,'C') %#ѕоднимать/опускать
motorD = motor(myev3,'D') %#ƒва мотора другого направлени€ в 1 порт
%motorD.Speed = 10;
%start(motorA)
%pause(1)
%stop(motorA)









%# ѕопытка в мультисрединг если 2 мотора одного направлени€ всунуть в
%разные порты
%MotorList = {motorA,motorB};
%matlabpool open 

%parfor i=1:length(MotorList)
    %# run the motors
    %MotorList{i}.Speed = 50;
%end


%start(motorC)
%pause(0.2)
%stop(motorC)









%##################Making 0,1 array pic 500x500############################
I = imread('test1.jpg');
Gray=rgb2gray(I)
BW=im2bw(Gray)
New=imresize(BW,[500 500])
mean(Array)









%###########################отсюда начинаетс€ код#########################
%#Ќажимаем и идем по пр€мым
for i=1:500
    for j=1:500
        if (New(i,j)>0 and New(i,j-1)=0) do
            start(motorC)
            pause(0.2)
            stop(motorC)
            parfor i=1:length(MotorList)
                %# run the motors
                MotorList{i}.Speed = 10;
                pause(0.01)
                stop(MotorList{i})                
            end
        else
            if (New(i,j)>0 and New(i,j-1)>0)  do
                parfor i=1:length(MotorList)
                    %# run the motors
                    MotorList{i}.Speed = 10;
                    pause(0.01)
                    stop(MotorList{i})                
                end
            end
        else
            if (New(i,j)=0 and New(i,j-1)>0)  do
                start(motorC)
                pause(0.2)
                stop(motorC)
                parfor i=1:length(MotorList)
                    %# run the motors
                    MotorList{i}.Speed = 10;
                    pause(0.01)
                    stop(MotorList{i})    
                end
            end
        else
            if (New(i,j)=0 and New(i,j-1)=0)  do
                parfor i=1:length(MotorList)
                    %# run the motors
                    MotorList{i}.Speed = 10;
                    pause(0.01)
                    stop(MotorList{i})    
                end
            end
        end
    end
    start(motorD)
    pause(0.01)
    stop(motorD)
end