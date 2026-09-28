module alu_control (
    input  [1:0] alu_op,
    input  [5:0] funct,
    output reg [3:0] alu_ctrl
);
    always @(*) begin
        case (alu_op)
            2'b00: alu_ctrl = 4'b0010;        // ADD  (lw / sw / addi)
            2'b01: alu_ctrl = 4'b0110;        // SUB  (beq / bne comparison)
            2'b10: begin                       // R-type: decode funct
                case (funct)
                    6'h20: alu_ctrl = 4'b0010; // ADD
                    6'h22: alu_ctrl = 4'b0110; // SUB
                    6'h24: alu_ctrl = 4'b0000; // AND
                    6'h25: alu_ctrl = 4'b0001; // OR
                    default: alu_ctrl = 4'b0010;
                endcase
            end
            default: alu_ctrl = 4'b0010;
        endcase
    end
endmodule