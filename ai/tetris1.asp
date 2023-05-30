row(0..19). col(0..9).

in(X,Y,PIECE,ROTATION) | out(X,Y,PIECE,ROTATION) :- cell(X,Y,0), currentpiece(PIECE), rotation(PIECE,ROTATION), minCellPerColumn(X1,Y), X>=X1-4.
:- in(X,Y,V,ROTATION), in(X1,Y1,V,ROTATION1), ROTATION!=ROTATION1. % non ci possono essere due pezzi con rotazione diversa

% restituisce il blocco posizionato più in alto per ogni colonna
minCellPerColumn(X,Y):- col(Y), #min{R : cell(R,Y,1)} = X, cell(_,Y,1).
minCellPerColumn(X,Y) :- col(Y), X=19, not pres(Y).
% verifica se la colonna è occupata
pres(Y) :- cell(_,Y,1).

% un pezzo è formato da quattro blocchi
:- #count{X,Y : in(X,Y,PIECE,ROTATION)} != 4.

:- currentpiece(PIECE), not sameshape(PIECE).
sameshape(PIECE):- rotation(PIECE,ROTATION), in(X1,Y1,PIECE,ROTATION), in(X2,Y2,PIECE,ROTATION), block(1,PIECE,ROTATION,R1,C1), X2=X1+R1, Y2=Y1+C1,
in(X3,Y3,PIECE,ROTATION), block(2,PIECE,ROTATION,R2,C2), X3=X2+R2, Y3=Y2+C2, in(X4,Y4,PIECE,ROTATION), block(3,PIECE,ROTATION,R3,C3), X4=X3+R3, Y4=Y3+C3.

% un pezzo inserito non può avere un blocco sopra.
:- in(X,Y,PIECE,ROTATION), cell(X1,Y,1), X1<X.

% un pezzo deve poggiare su un blocco
:- currentpiece(PIECE), not hasbelow(PIECE).
hasbelow(PIECE) :- in(X,Y,PIECE,ROTATION), X=19.
hasbelow(PIECE) :- in(X,Y,PIECE,ROTATION), cell(X+1,Y,1).

% matrice su cui si applicheranno i weak constraints
newcell(X,Y,1) :- in(X,Y,PIECE,ROTATION).
newcell(X,Y,V) :- cell(X,Y,V), not newblock(X,Y). % scarta le celle che prima di mettere il nuovo pezzo erano vuote
newblock(X,Y):- in(X,Y,PIECE,_).

minCol(M) :- #min{Y,X : in(X,Y,PIECE,R)} = M.
output(M,R) :- minCol(M), in(X,M,_,R).

%preferisci posizione piu bassa quando l'altezza è superiore a 8
:~ newcell(X,Y,1), X<8. [1@3,X,Y]

% linee completate
fullRows(X) :- row(X), #count{Y : newcell(X,Y,1)} = 10.
:~ row(X), not fullRows(X). [2@3,X] %2

% numero di buchi
:~ newcell(X,Y,0), newcell(X1,Y,1), X1<X, not fullRows(X1). [5@3,X,Y]

number(-20..20).
% differenza tra le altezze delle colonne
minNewCell(V,Y):- col(Y), exists(Y), #min{R : newcell(R,Y,1)} = V.
minNewCell(V,Y) :- col(Y), V=19, not exists(Y).
exists(Y) :- newcell(_,Y,1).
:~ number(V), minNewCell(V1,Y1), minNewCell(V2,Y2), Y2=Y1+1, &abs(V;S), V=V1-V2, V1!=V2. [S@3,Y1,Y2] %3

% La prima colonna deve essere più alta
:~ newcell(X,0,0), minRow(R), X>R. [1@3,X]
minRow(R) :- #min{X : newcell(X,Y,1)} = R.
