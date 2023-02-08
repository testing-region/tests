power(kufour, 2001, 2009).
power(mills, 2009, 2012).
power(mahama, 2012, 2016).

president(X, Y) :- power(X, A, B), Y >= A, Y < B.
