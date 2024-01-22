# Universal Disassembler program for 8-bit microprocessors

Note:
This is a fork of https://github.com/jefftranter/udis. This fork contains the
following updates:
- Support for blocks of memory/rom data which isn't executable code, like strings, tables etc
- Support for Windows OS
- Starting address may be given as a hexadecimal address
- Checked with pylint tooling
- Prelimanairy support for labels for 6502 processor binary files

This is a simple disassembler for various 8-bit microprocessors. It
reads a binary file specified on the command line and produces a
disassembly. It requires Python 3. It has been tested on Linux but
should work on any platform that supports Python. See the source code
for more details.

The following CPUs are either supported or planned to be supported:

CPU    Status
---    ------

6502    done

65816   done

65C02   done

6800    done

6801/6803    done

6809    done (incomplete)

6811    done

8080    done

8085    done

8051    done (incomplete)

Z80     done

F8      possible

1802    done

TMS9900 possible


usage:
-----
udis.py [-h] [-c CPU] [-n] [-a ADDRESS] [-b file] [-i] filename

positional arguments:
---------------------

filename &ensp;&ensp;Binary file to disassemble

optional arguments:
------------------

| Argument                | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| `-h, --help`        | show this help message and exit                                  |
| `-c CPU, --cpu CPU` | `CPU` type (defaults to 6502)                                      |
| `-n, --nolist`     | Don't list instruction bytes (make output suitable for assembler)|
| `-a ADDRESS, --address ADDRESS` | Specify decimal starting address (defaults to 0) or hexadecimal address (use 0x....)                          |
| `-i, --invalid`     | Show invalid opcodes as ??? rather than constants                |
| `-b file, --block  file` | Use the `file` for code blocks containing bytes/ascii values/strings/words |
|                   | The `file` must be a text file in the same dir as `filename` containing per line: `<start address in hex>, <end address in hex>, <type>` |
|                   | types are: |
|                   | `b` &ensp; single bytes; (default) mnemonic ".byte" |
|                   | `a` &ensp; single ascii codes if printable, otherwise byte reprensentation; mnemonic ".ascii"
|                   | `s` &ensp; string reprensentation; mnemonic ".string"
|                   |&ensp;&ensp;&ensp; Note: single quotes are not yet correctly implemented
|                   | `w` &ensp; words, 2 bytes with second byte as most significant; mnemonic ".word"
|                   | `W` &ensp; words, 2 bytes with first byte as most significant; mnemonic ".dw"


Support for labels:
Use of the processor file '6502_labels.py' (use in the command line "-c 6502_labels") will give some support for labels. 
The location/value of labels should be defined in a file named equal to the binary file but with extension '.lbl'. It
must be a plain ascii text file containing the label name followed ba a comma and the hexadecimal value
of the label. On the code address of the label an extra line in the result is ginen with the label followed by a colon. Futher 
all mnenomics using the labeladdress is replaced with the mnenomic using the label name.

In the examples map you will find an example for the ROMs as contained in the Acorn Atom.
