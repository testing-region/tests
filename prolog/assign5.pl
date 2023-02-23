/*
mother(M, Y).   % M is the mother of Y
father(F, X).   % F is the father of X
*/

father("David", "Saah").
father("Saah", "Samuel").

/* X is the grandfather of Y if X is the parent of Z,
    and Z is the parent of Y
*/
grandfather(X, Y) :- father(X, Z), father(Z, Y).
