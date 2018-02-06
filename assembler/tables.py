op_table = {
	"LOAD"	:	"0",
	"MOV"	:	"10",
	"JMP"	:	"1110",
	"JNZ"	:	"1111"
}

alu_func_table = {
	"NEG"	:	"000",
	"ADD"	:	"010",
	"SUB"	:	"001",
	"MULHI"	:	"011",
	"MULLO"	:	"100",
	"AND"	:	"110",
	"XOR"	:	"101",
	"COM"	:	"111"
}

reg_table = {
	"X0"	:	"000",
	"X1"	:	"001",
	"Y0"	:	"010",
	"Y1"	:	"011",
	"M"		:	"101",
	"I"		:	"110",
	"DM"	:	"111"
}

src_only_reg_table = {
	"R"		:	"100",
	"I_REG"	:	"110",
	"IREG"	:	"110",
	"I_PINS":	"110",
	"IPINS"	:	"110",
}

dest_only_reg_table = {
	"O_REG"	:	"100",
	"OREG"	:	"100",
}