
// tb_thermostat.v — Simulation Testbench
// Tests all 3 required functional cases + 22 additional scenarios
// (25 total, exceeds the 20-scenario minimum requirement)
//
// How it works:
//   - Writes current/desired/critical temperatures to data memory
//     via the ext_we interface (simulates BTN1 + SW on FPGA)
//   - Waits 200 clock cycles for the MIPS program to complete
//     at least 4 full loop iterations and stabilise fan/alarm
//   - Checks fan_out and alarm_out against expected values
//   - Prints PASS / FAIL with all relevant values

module tb_thermostat;

    // DUT Signals 
    reg         clk;
    reg         reset;
    reg         ext_we;
    reg  [7:0]  ext_addr;
    reg  [31:0] ext_wdata;
    wire        fan;
    wire        alarm;
    wire [31:0] cur_temp;

    //DUT Instantiation 
    mips_core DUT (
        .clk              (clk),
        .reset            (reset),
        .ext_we           (ext_we),
        .ext_addr         (ext_addr),
        .ext_wdata        (ext_wdata),
        .fan_out          (fan),
        .alarm_out        (alarm),
        .current_temp_out (cur_temp)
    );

    //Clock: 10 ns period (100 MHz) 
    initial clk = 0;
    always  #5 clk = ~clk;

    //Waveform Dump 
    initial begin
        $dumpfile("thermostat_tb.vcd");
        $dumpvars(0, tb_thermostat);
    end

    //Counters 
    integer pass_count = 0;
    integer fail_count = 0;

    
    //TASK: write_mem
    //Write a 32-bit value to a specific data memory word
    //(word address: 0=cur, 1=des, 2=crit)
    
    task write_mem;
        input [7:0]  word_addr;
        input [31:0] value;
        begin
            @(negedge clk);
            ext_we    = 1;
            ext_addr  = word_addr;
            ext_wdata = value;
            @(posedge clk); #1;
            ext_we = 0;
        end
    endtask

    
    // TASK: set_temps
    //   Load current / desired / critical temperatures
    
    task set_temps;
        input [31:0] cur;
        input [31:0] des;
        input [31:0] crit;
        begin
            write_mem(8'd0, cur);
            write_mem(8'd1, des);
            write_mem(8'd2, crit);
            // Wait for MIPS to complete ≥4 full loop iterations
            // Worst-case loop = 22 instructions; 200 cycles >> 4×22 = 88
            repeat(200) @(posedge clk);
        end
    endtask

    
    // TASK: check
    
    task check;
        input [7:0]  test_num;
        input [31:0] cur, des, crit;
        input        exp_fan;
        input        exp_alarm;
        begin
            if (fan === exp_fan && alarm === exp_alarm) begin
                $display("[PASS] Test %02d | cur=%3d des=%3d crit=%3d | fan=%b alarm=%b",
                          test_num, cur, des, crit, fan, alarm);
                pass_count = pass_count + 1;
            end else begin
                $display("[FAIL] Test %02d | cur=%3d des=%3d crit=%3d | fan=%b(exp %b) alarm=%b(exp %b)",
                          test_num, cur, des, crit, fan, exp_fan, alarm, exp_alarm);
                fail_count = fail_count + 1;
            end
        end
    endtask

    
    // MAIN TEST SEQUENCE
    
    initial begin
        // ── Reset ────────────────────────────────────────────
        ext_we = 0; ext_addr = 0; ext_wdata = 0;
        reset  = 1;
        repeat(4) @(posedge clk);
        reset  = 0;
        repeat(10) @(posedge clk);   // let PC settle at 0

        $display("========================================");
        $display(" MIPS Thermostat Testbench — 25 Tests");
        $display("========================================");

        // REQUIRED CASES (from project spec)
        
        // Test 01 — Case 1: cur=22 < des=25 → fan=OFF alarm=OFF
        set_temps(32'd22, 32'd25, 32'd40);
        check(8'd1, 32'd22, 32'd25, 32'd40, 1'b0, 1'b0);

        // Test 02 — Case 2: cur=30 > des=25, crit=40 → fan=ON alarm=OFF
        set_temps(32'd30, 32'd25, 32'd40);
        check(8'd2, 32'd30, 32'd25, 32'd40, 1'b1, 1'b0);

        // Test 03 — Case 3: cur=45 > crit=40 → fan=ON alarm=ON
        set_temps(32'd45, 32'd25, 32'd40);
        check(8'd3, 32'd45, 32'd25, 32'd40, 1'b1, 1'b1);

        
        // BOUNDARY / EDGE CASES
        

        // Test 04 — cur == des exactly → fan=OFF (not exceeding)
        set_temps(32'd25, 32'd25, 32'd40);
        check(8'd4, 32'd25, 32'd25, 32'd40, 1'b0, 1'b0);

        // Test 05 — cur == crit exactly → alarm=OFF (not exceeding)
        set_temps(32'd40, 32'd25, 32'd40);
        check(8'd5, 32'd40, 32'd25, 32'd40, 1'b1, 1'b0);

        // Test 06 — cur one below des → fan=OFF
        set_temps(32'd24, 32'd25, 32'd40);
        check(8'd6, 32'd24, 32'd25, 32'd40, 1'b0, 1'b0);

        // Test 07 — cur one above des → fan=ON
        set_temps(32'd26, 32'd25, 32'd40);
        check(8'd7, 32'd26, 32'd25, 32'd40, 1'b1, 1'b0);

        // Test 08 — cur one below crit → alarm=OFF
        set_temps(32'd39, 32'd25, 32'd40);
        check(8'd8, 32'd39, 32'd25, 32'd40, 1'b1, 1'b0);

        // Test 09 — cur one above crit → alarm=ON
        set_temps(32'd41, 32'd25, 32'd40);
        check(8'd9, 32'd41, 32'd25, 32'd40, 1'b1, 1'b1);

        
        // MIN / MAX TEMPERATURE
        
        // Test 10 — cur=0 (minimum) → fan=OFF alarm=OFF
        set_temps(32'd0,   32'd25, 32'd40);
        check(8'd10, 32'd0, 32'd25, 32'd40, 1'b0, 1'b0);

        // Test 11 — cur=255 (max 8-bit) → fan=ON alarm=ON
        set_temps(32'd255, 32'd25, 32'd40);
        check(8'd11, 32'd255, 32'd25, 32'd40, 1'b1, 1'b1);

        // Test 12 — cur=100, des=25, crit=40 → fan=ON alarm=ON
        set_temps(32'd100, 32'd25, 32'd40);
        check(8'd12, 32'd100, 32'd25, 32'd40, 1'b1, 1'b1);

        
        // DIFFERENT THRESHOLD SETS
        

        // Test 13 — des=30, crit=45: cur=28 → fan=OFF alarm=OFF
        set_temps(32'd28, 32'd30, 32'd45);
        check(8'd13, 32'd28, 32'd30, 32'd45, 1'b0, 1'b0);

        // Test 14 — des=30, crit=45: cur=35 → fan=ON alarm=OFF
        set_temps(32'd35, 32'd30, 32'd45);
        check(8'd14, 32'd35, 32'd30, 32'd45, 1'b1, 1'b0);

        // Test 15 — des=30, crit=45: cur=50 → fan=ON alarm=ON
        set_temps(32'd50, 32'd30, 32'd45);
        check(8'd15, 32'd50, 32'd30, 32'd45, 1'b1, 1'b1);

        // Test 16 — des=20, crit=30: cur=10 → fan=OFF alarm=OFF (cool)
        set_temps(32'd10, 32'd20, 32'd30);
        check(8'd16, 32'd10, 32'd20, 32'd30, 1'b0, 1'b0);

        // Test 17 — des=20, crit=30: cur=20 (equal des) → fan=OFF alarm=OFF
        set_temps(32'd20, 32'd20, 32'd30);
        check(8'd17, 32'd20, 32'd20, 32'd30, 1'b0, 1'b0);

        // Test 18 — des=20, crit=30: cur=21 (just above des) → fan=ON alarm=OFF
        set_temps(32'd21, 32'd20, 32'd30);
        check(8'd18, 32'd21, 32'd20, 32'd30, 1'b1, 1'b0);

        // Test 19 — des=20, crit=30: cur=30 (equal crit) → fan=ON alarm=OFF
        set_temps(32'd30, 32'd20, 32'd30);
        check(8'd19, 32'd30, 32'd20, 32'd30, 1'b1, 1'b0);

        // Test 20 — des=20, crit=30: cur=31 (just above crit) → fan=ON alarm=ON
        set_temps(32'd31, 32'd20, 32'd30);
        check(8'd20, 32'd31, 32'd20, 32'd30, 1'b1, 1'b1);

        // ══════════════════════════════════════════════════════
        // STRESS / REGRESSION
        // ══════════════════════════════════════════════════════

        // Test 21 — all zeros → fan=OFF alarm=OFF
        set_temps(32'd0, 32'd0, 32'd0);
        check(8'd21, 32'd0, 32'd0, 32'd0, 1'b0, 1'b0);

        // Test 22 — des=15, crit=20: cur=15 (equal des) → fan=OFF alarm=OFF
        set_temps(32'd15, 32'd15, 32'd20);
        check(8'd22, 32'd15, 32'd15, 32'd20, 1'b0, 1'b0);

        // Test 23 — des=25, crit=35: cur=35 (equal crit) → fan=ON alarm=OFF
        set_temps(32'd35, 32'd25, 32'd35);
        check(8'd23, 32'd35, 32'd25, 32'd35, 1'b1, 1'b0);

        // Test 24 — des=25, crit=35: cur=36 (just above crit) → fan=ON alarm=ON
        set_temps(32'd36, 32'd25, 32'd35);
        check(8'd24, 32'd36, 32'd25, 32'd35, 1'b1, 1'b1);

        // Test 25 — des=5, crit=10: cur=5 (cold env, equal des) → fan=OFF alarm=OFF
        set_temps(32'd5, 32'd5, 32'd10);
        check(8'd25, 32'd5, 32'd5, 32'd10, 1'b0, 1'b0);

        // ── Summary ──────────────────────────────────────────
        $display("========================================");
        $display(" Results: %0d PASSED / %0d FAILED", pass_count, fail_count);
        $display("========================================");

        if (fail_count == 0)
            $display(" ALL TESTS PASSED");
        else
            $display(" SOME TESTS FAILED — check waveforms");

        $finish;
    end

    // ── Timeout Guard (prevents infinite loop in sim) 
    initial begin
        #1_000_000;
        $display("[TIMEOUT] Simulation exceeded 1 ms — check for stalls");
        $finish;
    end

endmodule 