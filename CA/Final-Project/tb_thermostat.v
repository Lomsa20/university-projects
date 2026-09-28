module thermostat_top (
    input        CLK50M,    // 50 MHz clock
    input        KEY0,      // Reset       (active LOW)
    input        KEY1,      // Load temp   (active LOW)
    input  [7:0] SW,        // Current temperature input
    output [9:0] LEDR       // LEDs [0]=fan [1]=alarm [9:2]=temperature
);
 
    // ── Reset (active-low key → active-high internal signal) ─
    wire reset = ~KEY0;
 
    // ── BTN1 3-stage synchroniser + rising-edge detector ─────
    // KEY1 is active LOW: pressed = 0 → we invert to get
    // a logic-high "pressed" signal, then catch rising edge.
    reg [2:0] key1_sync;
    wire      load_pulse;
 
    always @(posedge CLK50M or posedge reset) begin
        if (reset)
            key1_sync <= 3'b0;
        else
            key1_sync <= {key1_sync[1:0], ~KEY1}; // invert: 1 when pressed
    end
 
    // Rising edge of the debounced ~KEY1 signal
    assign load_pulse = key1_sync[2] & ~key1_sync[1];
 
    // ── MIPS Core Instantiation 
    wire        fan, alarm;
    wire [31:0] cur_temp;
 
    mips_core PROC (
        .clk             (CLK50M),
        .reset           (reset),
        .ext_we          (load_pulse),
        .ext_addr        (8'd0),              // always write to word 0 (current temp)
        .ext_wdata       ({24'b0, SW}),       // zero-extend 8-bit SW to 32-bit
        .fan_out         (fan),
        .alarm_out       (alarm),
        .current_temp_out(cur_temp)
    );
 
    // ── LED Assignments 
    assign LEDR[0]   = fan;                  // LED0 = Fan  status
    assign LEDR[1]   = alarm;               // LED1 = Alarm status
    assign LEDR[9:2] = cur_temp[7:0];       // LED[9:2] = current temperature
 
endmodule