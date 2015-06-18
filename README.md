Universal Disassembler program for 8-bit microprocessors

This is a simple disassembler for various 8-bit microprocessors. It
reads a binary file specified on the command line and produces a
disassembly. It requires Python 3. It has been tested on Linux but
should work on any platform that supports Python. See the source code
for more details.

The following CPUs are either supported or planned to be supported:

CPU    Status
---    ------

1802   planned

6502   done

65816  planned

65C02  planned

6800   done

6809   planned

6811   planned

8008   planned

8051   planned

F8     planned

Z80    planned



usage: udis.py [-h] [-c CPU] [-n] [-a ADDRESS] [-i] filename

positional arguments:

  filename              Binary file to disassemble

optional arguments:

  -h, --help            show this help message and exit

  -c CPU, --cpu CPU     Specify CPU type (defaults to 6502)

  -n, --nolist          Don't list instruction bytes (make output suitable for assembler)

  -a ADDRESS, --address ADDRESS
                        Specify decimal starting address (defaults to 0)

  -i, --invalid         Show invalid opcodes as ??? rather than constants
