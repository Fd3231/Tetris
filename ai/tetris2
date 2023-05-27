row(0..19). col(0..9).

piece(P,2) :- nextpiece(P).
piece(P,1) :- currentpiece(P).

in(X,Y,PIECE,ROTATION,N) | out(X,Y,PIECE,ROTATION,N) :- cell(X,Y,0), piece(PIECE,N), rotation(PIECE,ROTATION), minCellPerColumn(X1,Y), X>=X1-4.
:- in(X,Y,V,ROTATION,N), in(X1,Y1,V,ROTATION1,N), ROTATION!=ROTATION1. % non ci possono essere due blocchi con rotazione diversa
:- in(X,Y,V,_,N), in(X,Y,V,_,N1), N!=N1.

minCellPerColumn(X,Y):- col(Y), #min{R : cell(R,Y,1)} = X, cell(_,Y,1).
minCellPerColumn(X,Y) :- col(Y), X=19, not pres(Y).
pres(Y) :- cell(_,Y,1).

:- piece(PIECE,N), #count{X,Y : in(X,Y,PIECE,ROTATION,N)} != 4.

:- piece(PIECE,N), not sameshape(PIECE,N).
sameshape(PIECE,N):- rotation(PIECE,ROTATION), in(X1,Y1,PIECE,ROTATION,N), in(X2,Y2,PIECE,ROTATION,N), block(1,PIECE,ROTATION,R1,C1), X2=X1+R1, Y2=Y1+C1,
in(X3,Y3,PIECE,ROTATION,N), block(2,PIECE,ROTATION,R2,C2), X3=X2+R2, Y3=Y2+C2, in(X4,Y4,PIECE,ROTATION,N), block(3,PIECE,ROTATION,R3,C3), X4=X3+R3, Y4=Y3+C3.

% un pezzo inserito non può avere un blocco sopra.
:- in(X,Y,PIECE,ROTATION,N), cell(X1,Y,1), X1<X.

% un pezzo deve poggiare su un blocco
:- piece(PIECE,N), not hasbelow(PIECE,N).
hasbelow(PIECE,N) :- in(X,Y,PIECE,ROTATION,N), X=19.
hasbelow(PIECE,N) :- in(X,Y,PIECE,ROTATION,N), cell(X+1,Y,1).
hasbelow(PIECE,N) :- in(X,Y,PIECE,_,N), in(X+1,Y,PIECE1,_,N1), piece(PIECE,N), piece(PIECE1,N1), currentpiece(PIECE1), nextpiece(PIECE).

% currentpiece non può avere sotto nextpiece
:- currentpiece(PIECE), piece(PIECE,N), sotto(PIECE,N).
sotto(PIECE,N) :- in(X,Y,PIECE,_,N), in(X1,Y,PIECE1,_,N1), X1>X, nextpiece(PIECE1), piece(PIECE1,N1), N<N1.

% matrice su cui si applicheranno i weak constraints
newcell(X,Y,1) :- in(X,Y,PIECE,ROTATION,N), piece(PIECE,N).
newcell(X,Y,PIECE) :- cell(X,Y,PIECE), not ceunacella(X,Y).
ceunacella(X,Y):- in(X,Y,PIECE,_,N), piece(PIECE,N).

minCol(M) :- #min{Y,X : in(X,Y,PIECE,R,1), currentpiece(PIECE)} = M.
output(M,R) :- minCol(M), in(X,M,PIECE,R,1), currentpiece(PIECE). 

% non fare buchi, almeno che non sia tetris
:~ newcell(X,Y,0), newcell(X1,Y,1), X1<X. [9@2,X,Y]
numFullRows(N) :- #count{X : fullRows(X)} = N.

% lascia uno spazio alla fine, almeno che non sia una pulizia
:~ newcell(X,9,1), not fullRows(X). [3@2,X]

% fai tetris 3
:~ numFullRows(N), N!=4. [1@3]

% non alzare troppo
:~ newcell(X,Y,1), X<12. [5@2,X,Y]

% pulisci riga solo nel caso in cui non dovessi riuscire a non creare un buco
fullRows(X) :- row(X), #count{Y : newcell(X,Y,1)} = 10.
:~ row(X), newcell(X,_,1), fullRows(X). [4@1,X]

minRow(R) :- #min{X : newcell(X,Y,1)} = R.

numero(-10..10).
% differenza tra le altezze delle colonne
minNewCell(V,Y):- col(Y), presente(Y), #min{R : newcell(R,Y,1)} = V.
minNewCell(V,Y) :- col(Y), V=19, not presente(Y).
presente(Y) :- newcell(_,Y,1).
:~ numero(V), minNewCell(V1,Y1), minNewCell(V2,Y2), Y2=Y1+1, &abs(V;S), V=V1-V2, V1!=V2, Y2!=9. [S@2,Y1,Y2] %3

:~ newcell(X,0,0), minRow(R), X>R. [1@2,X]