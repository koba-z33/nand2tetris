// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/01/And.tst

load Nx.hdl,
output-file Nx.out,
compare-to Nx.cmp,
output-list x%B3.1.3 nx%B3.1.3 out%B3.1.3;

set x 0,
set nx 0,
eval,
output;

set x 0,
set nx 1,
eval,
output;

set x 1,
set nx 0,
eval,
output;

set x 1,
set nx 1,
eval,
output;
