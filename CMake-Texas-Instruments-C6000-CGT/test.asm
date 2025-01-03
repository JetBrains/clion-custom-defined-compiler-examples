        .include nonexisting.i

	.global __dummy
	.sect	".text:__dummy"
	.clink
__dummy: .asmfunc

	 NEGA	.S2	B4,	B5		; -den         .endasmfunc
