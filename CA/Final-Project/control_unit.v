
//DATA MEMORY — 128 words, async read / sync write
//    + external write port for FPGA switch loading11

module data_mem (
    input         clk,
    input         MemRead,
    input         MemWrite,
    input  [31:0] addr,
    input  [31:0] wdata,
    output [31:0] rdata,
    // External interface (BTN1 + SW on FPGA / testbench)
    input         ext_we,
    input  [7:0]  ext_addr,   // word index (0=cur, 1=des, 2=crit …)
    input  [31:0] ext_wdata,
    // Direct status outputs
    output        fan_out,
    output        alarm_out,
    output [31:0] current_temp_out
);
    reg [31:0] mem [0:127];

    initial begin : MEM_INIT
        integer k;
        for (k = 0; k < 128; k = k + 1)
            mem[k] = 32'b0;
        mem[0] = 32'd22;          // current temp  (default: Case 1)
        mem[1] = 32'd25;          // desired temp
        mem[2] = 32'd40;          // critical temp
        mem[3] = 32'h00000000;    // fan  = OFF
        mem[4] = 32'h00000000;    // alarm = OFF
        mem[5] = 32'h80000000;    // sign mask — DO NOT MODIFY AT RUNTIME
        mem[6] = 32'h00000000;    // LED combined
    end

    // Asynchronous read
    assign rdata = mem[addr[31:2]];

    // Synchronous write — ext_we has priority over MIPS MemWrite
    always @(posedge clk) begin
        if (ext_we)
            mem[ext_addr] <= ext_wdata;
        else if (MemWrite)
            mem[addr[31:2]] <= wdata;
    end

    assign fan_out          = mem[3][0];
    assign alarm_out        = mem[4][0];
    assign current_temp_out = mem[0];
endmodule