
//REGISTER FILE — 32 × 32-bit, $zero always reads 0

module reg_file (
    input         clk,
    input         RegWrite,
    input  [4:0]  rs,
    input  [4:0]  rt,
    input  [4:0]  rd,
    input  [31:0] wdata,
    output [31:0] rdata1,
    output [31:0] rdata2
);
    reg [31:0] regs [0:31];
    integer i;
    initial begin
        for (i = 0; i < 32; i = i + 1)
            regs[i] = 32'b0;
    end

    // Asynchronous read; $zero always 0
    assign rdata1 = (rs == 5'b0) ? 32'b0 : regs[rs];
    assign rdata2 = (rt == 5'b0) ? 32'b0 : regs[rt];

    // Synchronous write; never write to $zero
    always @(posedge clk) begin
        if (RegWrite && rd != 5'b0)
            regs[rd] <= wdata;
    end
endmodule