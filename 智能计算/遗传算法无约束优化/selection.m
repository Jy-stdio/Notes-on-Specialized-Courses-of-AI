function [YY1 YY2] = selection(P1,B,p,s)
% P1 - population
% B - fitness value 
% p - population size
% s = select top s chromsomes
%-------------------------------------------------------------------------
% Top selection operation
B=B';
for i =1:s
[r1 c1]=find(B==max(B));
Y1(i,:)=P1(max(c1),:);
Fn(i)=B(max(c1));
P1(max(c1),:)=[];
B(max(c1))=[];
clear r1 c1
end
%=======================================================
% Determine total fitness for the population
C=sum(B);
% Determine selection probability
D=B/C;
% Determine cumulative probability 
E= cumsum(D);
% Generate a vector constaining normalised random numbers
N=rand(1);
d1=1;
d2=s;
while d2 <= p-1
    if N <= E(d1)
       Y1(d2+1,:)=P1(d1,:); 
       Fn(d2+1)=B(d1);
       P1(d1,:)=[];
       B(d1)=[];
       C=sum(B);
       D=B/C;
       E= cumsum(D);
       N=rand(1);
       d2 = d2 +1; 
       d1=1;
     else
        d1 = d1 + 1;
    end
end
YY1=Y1;
YY2=Fn;
end
