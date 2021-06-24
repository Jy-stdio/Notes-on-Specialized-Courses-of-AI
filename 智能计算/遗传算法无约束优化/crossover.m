function Y=crossover(P,n)
% P = population
% n = pair of chromosomes to be crossovered
[x1 y1]=size(P);
Z=zeros(2*n,40);
for i = 1:n
    r1=randi(x1,1,2);
    while r1(1)==r1(2)
        r1=randi(x1,1,2);
    end
    A1=P(r1(1),:);
    A2=P(r1(2),:);
    r2=1+randi(39);
    B1=A1(1,r2:40);
    A1(1,r2:40)=A2(1,r2:40);
    A2(1,r2:40)=B1;
    Z(2*i-1,:)=A1;
    Z(2*i,:)=A2;
end
Y=Z;