module control_unit (
    input  [5:0] opcode,
    output reg   RegDst,
    output reg   ALUSrc,
    output reg   MemToReg,
    output reg   RegWrite,
    output reg   MemRead,
    output reg   MemWrite,
    output reg   Branch,
    output reg   BNE,
    output reg   Jump,
    output reg [1:0] ALUOp
);
    always @(*) begin
        // safe defaults
        {RegDst, ALUSrc, MemToReg, RegWrite,
         MemRead, MemWrite, Branch, BNE, Jump} = 9'b0;
        ALUOp = 2'b00;

        case (opcode)
            6'h00: begin   // R-type (add, sub, and, or)
                RegDst  = 1;
                RegWrite = 1;
                ALUOp   = 2'b10;
            end
            6'h23: begin   // lw
                ALUSrc   = 1;
                MemToReg = 1;
                RegWrite = 1;
                MemRead  = 1;
            end
            6'h2B: begin   // sw
                ALUSrc   = 1;
                MemWrite = 1;
            end
            6'h04: begin   // beq
                Branch = 1;
                ALUOp  = 2'b01;
            end
            6'h05: begin   // bne
                Branch = 1;
                BNE    = 1;
                ALUOp  = 2'b01;
            end
            6'h08: begin   // addi
                ALUSrc   = 1;
                RegWrite = 1;
                ALUOp    = 2'b00;
            end
            6'h02: begin   // j
                Jump = 1;
            end
        endcase
    end
endmodule

