
//MIPS CORE — single-cycle datapath + control

module mips_core (
    input         clk,
    input         reset,
    // External memory write (FPGA switches / testbench)
    input         ext_we,
    input  [7:0]  ext_addr,
    input  [31:0] ext_wdata,
    // Thermostat status outputs
    output        fan_out,
    output        alarm_out,
    output [31:0] current_temp_out
);

    // ── Program Counter ──────────────────────────────────────
    reg  [31:0] pc;
    wire [31:0] pc_plus4   = pc + 32'd4;
    wire [31:0] instr;

    // ── Instruction Fields ───────────────────────────────────
    wire [5:0]  opcode = instr[31:26];
    wire [4:0]  rs     = instr[25:21];
    wire [4:0]  rt     = instr[20:16];
    wire [4:0]  rd     = instr[15:11];
    wire [15:0] imm16  = instr[15:0];
    wire [25:0] jaddr  = instr[25:0];

    // ── Control Signals ──────────────────────────────────────
    wire        RegDst, ALUSrc, MemToReg, RegWrite;
    wire        MemRead, MemWrite, Branch, BNE, Jump;
    wire [1:0]  ALUOp;

    // ── Datapath Wires ───────────────────────────────────────
    wire [31:0] imm_ext;          // sign-extended immediate
    wire [4:0]  write_reg;        // destination register
    wire [31:0] rdata1, rdata2;   // register file read ports
    wire [31:0] alu_b;            // ALU second operand
    wire [3:0]  alu_ctrl;
    wire [31:0] alu_result;
    wire        zero;
    wire [31:0] mem_rdata;        // data memory read data
    wire [31:0] reg_wdata;        // data written back to register file

    // ── PC Next Logic ─────────────────────────────────────────
    wire        PCSrc;
    wire [31:0] pc_branch = pc_plus4 + (imm_ext << 2);
    wire [31:0] pc_jump   = {pc_plus4[31:28], jaddr, 2'b00};
    wire [31:0] pc_next   = Jump   ? pc_jump   :
                            PCSrc  ? pc_branch :
                                     pc_plus4;

    // PCSrc: BNE=0→branch when zero=1 (beq), BNE=1→branch when zero=0 (bne)
    assign PCSrc = Branch & (BNE ^ zero);

    always @(posedge clk or posedge reset) begin
        if (reset) pc <= 32'h0;
        else       pc <= pc_next;
    end

    // ── Muxes ────────────────────────────────────────────────
    assign write_reg  = RegDst  ? rd         : rt;
    assign alu_b      = ALUSrc  ? imm_ext    : rdata2;
    assign reg_wdata  = MemToReg ? mem_rdata : alu_result;

    // ── Module Instantiations ────────────────────────────────
    inst_mem IM (
        .addr  (pc),
        .instr (instr)
    );

    sign_extend SE (
        .in  (imm16),
        .out (imm_ext)
    );

    control_unit CU (
        .opcode   (opcode),
        .RegDst   (RegDst),
        .ALUSrc   (ALUSrc),
        .MemToReg (MemToReg),
        .RegWrite (RegWrite),
        .MemRead  (MemRead),
        .MemWrite (MemWrite),
        .Branch   (Branch),
        .BNE      (BNE),
        .Jump     (Jump),
        .ALUOp    (ALUOp)
    );

    alu_control AC (
        .alu_op   (ALUOp),
        .funct    (instr[5:0]),
        .alu_ctrl (alu_ctrl)
    );

    reg_file RF (
        .clk      (clk),
        .RegWrite (RegWrite),
        .rs       (rs),
        .rt       (rt),
        .rd       (write_reg),
        .wdata    (reg_wdata),
        .rdata1   (rdata1),
        .rdata2   (rdata2)
    );

    alu MAIN_ALU (
        .a      (rdata1),
        .b      (alu_b),
        .ctrl   (alu_ctrl),
        .result (alu_result),
        .zero   (zero)
    );

    data_mem DM (
        .clk            (clk),
        .MemRead        (MemRead),
        .MemWrite       (MemWrite),
        .addr           (alu_result),
        .wdata          (rdata2),
        .rdata          (mem_rdata),
        .ext_we         (ext_we),
        .ext_addr       (ext_addr),
        .ext_wdata      (ext_wdata),
        .fan_out        (fan_out),
        .alarm_out      (alarm_out),
        .current_temp_out (current_temp_out)
    );

endmodule