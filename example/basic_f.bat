Rem disassemble integer basic.rom
python ..\udis.py -a 0xC000 -b basicblock.txt -n atom_basic.rom -c 6502_labels >basicasm.asm
rem python udis.py -a 0xC000 -b basicblock.txt  atom_basic.rom >basicasm.txt
pause
