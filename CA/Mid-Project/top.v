module top (
    input  clk,
    input  rst,
    input  en,
    output [7:0] data_out,
    output [7:0] rom_data   // exposed for testbench visibility
);
    wire [2:0] addr;

    counter u_counter (
        .clk(clk), .rst(rst), .en(en),
        .addr(addr)
    );

    rom u_rom (
        .address(addr),
        .data(rom_data)
    );

    output_reg u_reg (
        .clk(clk), .rst(rst), .en(en),
        .d(rom_data), .q(data_out)
    );
endmodule