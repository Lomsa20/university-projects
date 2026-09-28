
//INSTRUCTION MEMORY — ROM, 64 words, word-addressed via PC

module inst_mem (
    input  [31:0] addr,
    output [31:0] instr
);
    reg [31:0] mem [0:63];

    initial begin
        // ── Thermostat MIPS Program ──────────────────────────
        mem[0]  = 32'h20080000; // addi $t0, $zero, 0
        mem[1]  = 32'h8D090000; // lw   $t1, 0($t0)
        mem[2]  = 32'h8D0A0004; // lw   $t2, 4($t0)
        mem[3]  = 32'h8D0B0008; // lw   $t3, 8($t0)
        mem[4]  = 32'h8D100014; // lw   $s0, 20($t0)
        mem[5]  = 32'h200E0001; // addi $t6, $zero, 1
        mem[6]  = 32'h012AC020; // add  $t8, $t1, $t2
        mem[7]  = 32'h012A6022; // sub  $t4, $t1, $t2
        mem[8]  = 32'h11800004; // beq  $t4, $zero, 4   → instr 13
        mem[9]  = 32'h01906824; // and  $t5, $t4, $s0
        mem[10] = 32'h15A00002; // bne  $t5, $zero, 2   → instr 13
        mem[11] = 32'hAD0E000C; // sw   $t6, 12($t0)    FAN=ON
        mem[12] = 32'h0800000E; // j    14
        mem[13] = 32'hAD00000C; // sw   $zero, 12($t0)  FAN=OFF
        mem[14] = 32'h012B6022; // sub  $t4, $t1, $t3
        mem[15] = 32'h11800004; // beq  $t4, $zero, 4   → instr 20
        mem[16] = 32'h01906824; // and  $t5, $t4, $s0
        mem[17] = 32'h15A00002; // bne  $t5, $zero, 2   → instr 20
        mem[18] = 32'hAD0E0010; // sw   $t6, 16($t0)    ALARM=ON
        mem[19] = 32'h08000015; // j    21
        mem[20] = 32'hAD000010; // sw   $zero, 16($t0)  ALARM=OFF
        mem[21] = 32'h8D0F000C; // lw   $t7, 12($t0)
        mem[22] = 32'h8D110010; // lw   $s1, 16($t0)
        mem[23] = 32'h01F19025; // or   $s2, $t7, $s1
        mem[24] = 32'hAD120018; // sw   $s2, 24($t0)
        mem[25] = 32'h08000000; // j    0               restart
        // ─── remaining slots default to NOP (add $zero,$zero,$zero = 0x00000020) ─
        // Quartus will infer ROM; unused entries = 0
    end

    assign instr = mem[addr[31:2]]; // PC is byte-addressed; index by word
endmodule