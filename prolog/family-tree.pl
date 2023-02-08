male(X).                % X is a male
female(Y).              % Y is a female
parent(X, Y).           % X is a parent of Y

/* BIOLOGICAL RULES */
is_mother(X) :- mother(X, Y).           % X is a mother if there exists Y such that X is a mother of Y
is_father(X) :- father(X, Y).           % X is a father if there exists Y such that X is a father of Y
is_child(X, Y) :- parent(Y, X).         % X is a child if Y is a parent of X.

% X is the grandparent of Y if X is the parent of Z, and Z is the parent of Y
is_grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% X is the sister of Y if Z is the parent of X and Y and X is a female.
is_sister_of(X, Y) :- parent(Z, X), parent(Z, Y), female(X).
