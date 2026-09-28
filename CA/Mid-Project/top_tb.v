module top_tb;
    reg clk, rst, en;
    wire [7:0] data_out;
    wire [7:0] rom_data;

    top uut (
        .clk(clk),
        .rst(rst),
        .en(en),
        .data_out(data_out),
        .rom_data(rom_data)
    );

    // 10ns clock period
    initial clk = 0;
    always #5 clk = ~clk;

    initial begin
        rst = 1; en = 0;
        @(posedge clk); #1;   // hold reset for 2 cycles
        @(posedge clk); #1;
        rst = 0; en = 1;      // run: step through all 8 ROM addresses
        repeat(8) @(posedge clk); #1;
        en = 0;               // hold: counter and output freeze
        repeat(3) @(posedge clk); #1;
        en = 1;               // resume
        repeat(8) @(posedge clk); #1;
        rst = 1;              // reset mid-run
        @(posedge clk); #1;
        rst = 0;
        repeat(8) @(posedge clk); #1;
        $stop;
    end
    initial begin
        $monitor("t=%0t rst=%b en=%b addr=%0d rom=%h dout=%h",
                  $time, rst, en, uut.u_counter.addr, rom_data, data_out);
    end
endmodule