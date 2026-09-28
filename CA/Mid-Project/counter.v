module counter (
    input  clk,
    input  rst,
    input  en,
    output reg [2:0] addr
);
    always @(posedge clk) begin
        if (rst)
            addr <= 3'd0;
        else if (en)
            addr <= addr + 1;
    end
endmodule