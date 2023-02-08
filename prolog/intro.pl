/* Group related facts together */

% Facts related to the "male" predicate
male(hesed).
male(kwasi).


% Facts related to the "female" predicate
female(afua).
female(lovelace).


% Facts about the "likes" predicate
likes(lovelace, matoke).
likes(hesed, linux).
likes(lovelace, programming).
likes(hesed, quiet).
likes(lovelace, quiet).
likes(lovelace, wine).

% Rules
likes(hesed, X) :- likes(X, wine).
