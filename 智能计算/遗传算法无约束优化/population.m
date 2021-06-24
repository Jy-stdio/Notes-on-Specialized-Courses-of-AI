function Y = population(n)
% n = population size
% 40 = number of bits to express the number. Why? It depends on
% the required accuracy (the number of digits after comma) that we want
Y=round(rand(n,40));