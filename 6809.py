##########################################################################
#
# Processor specific code

# CPU = "6809"
# Description = "Motorola 6809 8-bit microprocessor."
# DataWidth = 8 # 8-bit data
# AddressWidth = 16 # 16-bit addresses

# Maximum length of an instruction (for formatting purposes)
maxLength = 4

# Leadin bytes for multbyte instructions
leadInBytes = [0x10, 0x11]

# Notes:
# Not all addressing modes are implemented.

# Addressing mode table
addressModeTable = {
"inherent"    : "",
"imm8"        : "#${0:02X}",
"imm16"       : "#${0:02X}{1:02X}",
"direct"      : "${0:02X}",
"indexed"     : "${0:02X},x",
"extended"    : "${0:02X}{1:02X}",
"rel8"        : "${0:04X}",
"rel16"       : "${0:02X}{1:02X}",
"r1,r2"       : "${0:02X}",  # Not fully implemented
# Extended Indirect
# Relative Indirect
# Zero-offset Indexed
# Zero-offset Indexed Indirect
# Constant-offset Indexed
# Constant-offset Indexed Indirect
# Accumulator-offset Indexed
# Accumulator-offset Indexed Indirect
# Auto-Increment Indexed
# Auto-Increment Indexed Indirect
# Auto-Decrement Indexed
# Auto-Decrement Indexed Indirect
}

# Op Code Table
# Key is numeric opcode (possibly multiple bytes)
# Value is a list:
#   # bytes
#   mnemonic
#   addressing mode.
#   flags (e.g. pcr)
opcodeTable = {

0x3a   :  [ 1, "abx",  "inherent"        ],
0x89   :  [ 2, "adca", "imm8"            ],
0x99   :  [ 2, "adca", "direct"          ],
0xa9   :  [ 2, "adca", "indexed"         ],
0xb9   :  [ 3, "adca", "extended"        ],
0xc9   :  [ 2, "adcb", "imm8"            ],
0xd9   :  [ 2, "adcb", "direct"          ],
0xe9   :  [ 2, "adcb", "indexed"         ],
0xf9   :  [ 3, "adcb", "extended"        ],
0x8b   :  [ 2, "adda", "imm8"            ],
0x9b   :  [ 2, "adda", "direct"          ],
0xab   :  [ 2, "adda", "indexed"         ],
0xbb   :  [ 3, "adda", "extended"        ],
0xcb   :  [ 2, "addb", "imm8"            ],
0xdb   :  [ 2, "addb", "direct"          ],
0xeb   :  [ 2, "addb", "indexed"         ],
0xfb   :  [ 3, "addb", "extended"        ],
0xc3   :  [ 3, "addd", "imm16"           ],
0xd3   :  [ 2, "addd", "direct"          ],
0xe3   :  [ 2, "addd", "indexed"         ],
0xf3   :  [ 3, "addd", "extended"        ],
0x84   :  [ 2, "anda", "imm8"            ],
0x94   :  [ 2, "anda", "direct"          ],
0xa4   :  [ 2, "anda", "indexed"         ],
0xb4   :  [ 3, "anda", "extended"        ],
0xc4   :  [ 2, "andb", "imm8"            ],
0xd4   :  [ 2, "andb", "direct"          ],
0xe4   :  [ 2, "andb", "indexed"         ],
0xf4   :  [ 3, "andb", "extended"        ],
0x1c   :  [ 2, "andcc","imm8"            ],
0x48   :  [ 1, "asla", "inherent"        ],
0x58   :  [ 1, "aslb", "inherent"        ],
0x08   :  [ 2, "asl",  "direct"          ],
0x68   :  [ 2, "asl",  "indexed"         ],
0x78   :  [ 3, "asl",  "extended"        ],
0x47   :  [ 1, "asra", "inherent"        ],
0x57   :  [ 1, "asrb", "inherent"        ],
0x07   :  [ 2, "asr",  "direct"          ],
0x67   :  [ 2, "asr",  "indexed"         ],
0x77   :  [ 3, "asr",  "extended"        ],
0x85   :  [ 2, "bita", "imm8"            ],
0x95   :  [ 2, "bita", "direct"          ],
0xa5   :  [ 2, "bita", "indexed"         ],
0xb5   :  [ 3, "bita", "extended"        ],
0xc5   :  [ 2, "bitb", "imm8"            ],
0xd5   :  [ 2, "bitb", "direct"          ],
0xe5   :  [ 2, "bitb", "indexed"         ],
0xf5   :  [ 3, "bitb", "extended"        ],
0x4f   :  [ 1, "clra", "inherent"        ],
0x5f   :  [ 1, "clrb", "inherent"        ],
0x0f   :  [ 2, "clr",  "direct"          ],
0x6f   :  [ 2, "clr",  "indexed"         ],
0x7f   :  [ 3, "clr",  "extended"        ],
0x81   :  [ 2, "cmpa", "imm8"            ],
0x91   :  [ 2, "cmpa", "direct"          ],
0xa1   :  [ 2, "cmpa", "indexed"         ],
0xb1   :  [ 3, "cmpa", "extended"        ],
0xc1   :  [ 2, "cmpb", "imm8"            ],
0xd1   :  [ 2, "cmpb", "direct"          ],
0xe1   :  [ 2, "cmpb", "indexed"         ],
0xf1   :  [ 3, "cmpb", "extended"        ],
0x1083 :  [ 4, "cmpd", "imm16"           ],
0x1093 :  [ 3, "cmpd", "direct"          ],
0x10a3 :  [ 3, "cmpd", "indexed"         ],
0x10b3 :  [ 4, "cmpd", "extended"        ],
0x118c :  [ 4, "cmps", "imm16"           ],
0x119c :  [ 3, "cmps", "direct"          ],
0x11ac :  [ 3, "cmps", "indexed"         ],
0x11bc :  [ 4, "cmps", "extended"        ],
0x1183 :  [ 4, "cmpu", "imm16"           ],
0x1193 :  [ 3, "cmpu", "direct"          ],
0x11a3 :  [ 3, "cmpu", "indexed"         ],
0x11b3 :  [ 4, "cmpu", "extended"        ],
0x8c   :  [ 3, "cmpx", "imm16"           ],
0x9c   :  [ 2, "cmpx", "direct"          ],
0xac   :  [ 2, "cmpx", "indexed"         ],
0xbc   :  [ 3, "cmpx", "extended"        ],
0x108c :  [ 4, "cmpy", "imm16"           ],
0x109c :  [ 3, "cmpy", "direct"          ],
0x10ac :  [ 3, "cmpy", "indexed"         ],
0x10bc :  [ 4, "cmpy", "extended"        ],
0x43   :  [ 1, "coma", "inherent"        ],
0x53   :  [ 1, "comb", "inherent"        ],
0x03   :  [ 2, "comb", "direct"          ],
0x63   :  [ 2, "comb", "indexed"         ],
0x73   :  [ 3, "comb", "extended"        ],
0x3c   :  [ 2, "cwai", "imm8"            ],
0x19   :  [ 1, "daa",  "inherent"        ],
0x4a   :  [ 1, "deca", "inherent"        ],
0x5a   :  [ 1, "decb", "inherent"        ],
0x0a   :  [ 2, "dec",  "direct"          ],
0x6a   :  [ 2, "dec",  "indexed"         ],
0x7a   :  [ 3, "dec",  "extended"        ],
0x88   :  [ 2, "eora", "imm8"            ],
0x98   :  [ 2, "eora", "direct"          ],
0xa8   :  [ 2, "eora", "direct"          ],
0xb8   :  [ 3, "eora", "extended"        ],
0xc8   :  [ 2, "eorb", "imm8"            ],
0xd8   :  [ 2, "eorb", "direct"          ],
0xe8   :  [ 2, "eorb", "direct"          ],
0xf8   :  [ 3, "eorb", "extended"        ],
0x1e   :  [ 2, "exg",  "r1,r2"           ],
0x4c   :  [ 1, "inca", "inherent"        ],
0x5c   :  [ 1, "incb", "inherent"        ],
0x0c   :  [ 2, "inc",  "indexed"         ],
0x6c   :  [ 2, "inc",  "direct"          ],
0x7c   :  [ 3, "inc",  "extended"        ],
0x0e   :  [ 2, "jmp",  "indexed"         ],
0x6e   :  [ 2, "jmp",  "direct"          ],
0x7e   :  [ 3, "jmp",  "extended"        ],
0x9d   :  [ 2, "jsr",  "indexed"         ],
0xad   :  [ 2, "jsr",  "direct"          ],
0xbd   :  [ 3, "jsr",  "extended"        ],


0x26   :  [ 2, "bne",  "rel8", pcr       ],
0x1026 :  [ 4, "lbne", "rel16", pcr      ],

0x00   :  [ 2, "neg",  "direct"          ],

0xff   :  [ 3, "stu", "extended"         ],

}

# End of processor specific code
##########################################################################