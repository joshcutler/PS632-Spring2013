param n;
param cost{i in 1..n, j in 1..n};
var matched{i in 1..n, j in 1..n}; 

minimize incompatibility: sum{i in 1..n, j in 1..n} cost[i,j]*matched[i,j];

s.t. left_matched{i in 1..n}: sum{j in 1..n} matched[i,j]=1;
s.t. right_matched{j in 1..n}: sum{i in 1..n} matched[i,j]=1;
s.t. nonnegative{i in 1..n, j in 1..n}: matched[i,j] >= 0;

data;

param n := 3;
param cost:  1 2 3 :=
         1   3 4 5
         2   2 1 6
         3   1 3 7;
end;