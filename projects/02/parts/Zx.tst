// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/01/And.tst

load Zx.hdl,
output-file Zx.out,
compare-to Zx.cmp,
output-list x%B3.1.3 zx%B3.1.3 out%B3.1.3;

set x 0,
set zx 0,
eval,
output;

set x 0,
set zx 1,
eval,
output;

set x 1,
set zx 0,
eval,
output;

set x 1,
set zx 1,
eval,
output;
