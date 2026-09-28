module rom (
    input  [2:0] address,
    output reg [7:0] data
);
    always @(*) begin
        case (address)
			3'd0: data = 8'b10000001;
			3'd1: data = 8'b11000011;
			3'd2: data = 8'b11100111;
			3'd3: data = 8'b11111111;
			3'd4: data = 8'b01111110;
			3'd5: data = 8'b00111100;
			3'd6: data = 8'b00011000;
			3'd7: data = 8'b00000000;
			default: data = 8'b00000000;
        endcase
    end
endmodule