function Y=mutation(P,n)
% P = population
% n = chromosomes to be mutated
[x1 y1]=size(P);
Z=zeros(n,40);
for i = 1:n
    r1=randi(x1);
    A1=P(r1,:);
    r2=randi(40,1,2);
    while r2(1)==r2(2)
        r2=randi(40,1,2);
    end
    B1=A1(1,r2(1));
    A1(1,r2(1))=A1(1,r2(2));
    A1(1,r2(2))=B1;
    Z(i,:)=A1;
end
Y=Z;