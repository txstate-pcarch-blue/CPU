#! /usr/local/Cellar/icarus-verilog/10.2/bin/vvp
:ivl_version "10.2 (stable)" "(v10_2)";
:ivl_delay_selection "TYPICAL";
:vpi_time_precision - 9;
:vpi_module "system";
:vpi_module "vhdl_sys";
:vpi_module "v2005_math";
:vpi_module "va_math";
S_0x7fd3b1c13680 .scope module, "alu_tb" "alu_tb" 2 3;
 .timescale -9 -9;
P_0x7fd3b1c13ae0 .param/l "tck" 0 2 5, +C4<00000000000000000000000000001010>;
v0x7fd3b1c27640_0 .var "a", 31 0;
v0x7fd3b1c276d0_0 .var "b", 31 0;
v0x7fd3b1c27760_0 .var "clk", 0 0;
v0x7fd3b1c277f0_0 .var "ctrl", 1 0;
v0x7fd3b1c27880_0 .var/i "num_iter", 31 0;
v0x7fd3b1c27950_0 .net "ovf", 0 0, L_0x7fd3b1c28a10;  1 drivers
v0x7fd3b1c279e0_0 .net "r", 31 0, L_0x7fd3b1c289a0;  1 drivers
v0x7fd3b1c27a90_0 .var "reset", 0 0;
v0x7fd3b1c27b40_0 .var/i "seed", 31 0;
v0x7fd3b1c27c50_0 .net "zero", 0 0, L_0x7fd3b1c28930;  1 drivers
E_0x7fd3b1c137e0 .event negedge, v0x7fd3b1c26e40_0;
S_0x7fd3b1c13320 .scope module, "dut" "alu" 2 15, 3 1 0, S_0x7fd3b1c13680;
 .timescale 0 0;
    .port_info 0 /INPUT 32 "A"
    .port_info 1 /INPUT 32 "B"
    .port_info 2 /INPUT 2 "CTRL"
    .port_info 3 /INPUT 1 "clk"
    .port_info 4 /INPUT 1 "reset"
    .port_info 5 /OUTPUT 32 "R"
    .port_info 6 /OUTPUT 1 "zero"
    .port_info 7 /OUTPUT 1 "ovf"
L_0x7fd3b1c287c0 .functor XOR 32, v0x7fd3b1c27640_0, v0x7fd3b1c276d0_0, C4<00000000000000000000000000000000>, C4<00000000000000000000000000000000>;
L_0x7fd3b1c28930 .functor BUFZ 1, v0x7fd3b1c272f0_0, C4<0>, C4<0>, C4<0>;
L_0x7fd3b1c289a0 .functor BUFZ 32, v0x7fd3b1c27120_0, C4<00000000000000000000000000000000>, C4<00000000000000000000000000000000>, C4<00000000000000000000000000000000>;
RS_0x10ffe9368 .resolv tri, L_0x7fd3b1c27d00, L_0x7fd3b1c282b0;
L_0x7fd3b1c28a10 .functor BUFZ 1, RS_0x10ffe9368, C4<0>, C4<0>, C4<0>;
v0x7fd3b1c09ab0_0 .net "A", 31 0, v0x7fd3b1c27640_0;  1 drivers
v0x7fd3b1c264c0_0 .net "B", 31 0, v0x7fd3b1c276d0_0;  1 drivers
v0x7fd3b1c26560_0 .net "CTRL", 1 0, v0x7fd3b1c277f0_0;  1 drivers
v0x7fd3b1c26610_0 .net "R", 31 0, L_0x7fd3b1c289a0;  alias, 1 drivers
L_0x11001b050 .functor BUFT 1, C4<0>, C4<0>, C4<0>, C4<0>;
v0x7fd3b1c266c0_0 .net *"_s10", 0 0, L_0x11001b050;  1 drivers
v0x7fd3b1c267b0_0 .net *"_s11", 32 0, L_0x7fd3b1c28140;  1 drivers
v0x7fd3b1c26860_0 .net *"_s16", 32 0, L_0x7fd3b1c284b0;  1 drivers
L_0x11001b098 .functor BUFT 1, C4<0>, C4<0>, C4<0>, C4<0>;
v0x7fd3b1c26910_0 .net *"_s19", 0 0, L_0x11001b098;  1 drivers
v0x7fd3b1c269c0_0 .net *"_s20", 32 0, L_0x7fd3b1c28590;  1 drivers
L_0x11001b0e0 .functor BUFT 1, C4<0>, C4<0>, C4<0>, C4<0>;
v0x7fd3b1c26ad0_0 .net *"_s23", 0 0, L_0x11001b0e0;  1 drivers
v0x7fd3b1c26b80_0 .net *"_s24", 32 0, L_0x7fd3b1c28680;  1 drivers
v0x7fd3b1c26c30_0 .net *"_s3", 32 0, L_0x7fd3b1c27ea0;  1 drivers
L_0x11001b008 .functor BUFT 1, C4<0>, C4<0>, C4<0>, C4<0>;
v0x7fd3b1c26ce0_0 .net *"_s6", 0 0, L_0x11001b008;  1 drivers
v0x7fd3b1c26d90_0 .net *"_s7", 32 0, L_0x7fd3b1c28000;  1 drivers
v0x7fd3b1c26e40_0 .net "clk", 0 0, v0x7fd3b1c27760_0;  1 drivers
v0x7fd3b1c26ee0_0 .net "diff", 31 0, L_0x7fd3b1c28390;  1 drivers
v0x7fd3b1c26f90_0 .net "ovf", 0 0, L_0x7fd3b1c28a10;  alias, 1 drivers
v0x7fd3b1c27120_0 .var "r_out", 31 0;
v0x7fd3b1c271b0_0 .net8 "regOvf", 0 0, RS_0x10ffe9368;  2 drivers
v0x7fd3b1c27240_0 .net "regXor", 31 0, L_0x7fd3b1c287c0;  1 drivers
v0x7fd3b1c272f0_0 .var "regZero", 0 0;
v0x7fd3b1c27390_0 .net "reset", 0 0, v0x7fd3b1c27a90_0;  1 drivers
v0x7fd3b1c27430_0 .net "sum", 31 0, L_0x7fd3b1c27da0;  1 drivers
v0x7fd3b1c274e0_0 .net "zero", 0 0, L_0x7fd3b1c28930;  alias, 1 drivers
E_0x7fd3b1c09d10 .event posedge, v0x7fd3b1c26e40_0;
L_0x7fd3b1c27d00 .part L_0x7fd3b1c28140, 32, 1;
L_0x7fd3b1c27da0 .part L_0x7fd3b1c28140, 0, 32;
L_0x7fd3b1c27ea0 .concat [ 32 1 0 0], v0x7fd3b1c27640_0, L_0x11001b008;
L_0x7fd3b1c28000 .concat [ 32 1 0 0], v0x7fd3b1c276d0_0, L_0x11001b050;
L_0x7fd3b1c28140 .arith/sum 33, L_0x7fd3b1c27ea0, L_0x7fd3b1c28000;
L_0x7fd3b1c282b0 .part L_0x7fd3b1c28680, 32, 1;
L_0x7fd3b1c28390 .part L_0x7fd3b1c28680, 0, 32;
L_0x7fd3b1c284b0 .concat [ 32 1 0 0], v0x7fd3b1c27640_0, L_0x11001b098;
L_0x7fd3b1c28590 .concat [ 32 1 0 0], v0x7fd3b1c276d0_0, L_0x11001b0e0;
L_0x7fd3b1c28680 .arith/sub 33, L_0x7fd3b1c284b0, L_0x7fd3b1c28590;
    .scope S_0x7fd3b1c13320;
T_0 ;
    %wait E_0x7fd3b1c09d10;
    %load/vec4 v0x7fd3b1c27390_0;
    %pad/u 32;
    %cmpi/e 1, 0, 32;
    %jmp/0xz  T_0.0, 4;
    %pushi/vec4 0, 0, 32;
    %assign/vec4 v0x7fd3b1c27120_0, 0;
    %jmp T_0.1;
T_0.0 ;
    %load/vec4 v0x7fd3b1c27390_0;
    %pad/u 32;
    %cmpi/e 0, 0, 32;
    %jmp/0xz  T_0.2, 4;
    %load/vec4 v0x7fd3b1c26560_0;
    %dup/vec4;
    %pushi/vec4 0, 0, 2;
    %cmp/u;
    %jmp/1 T_0.4, 6;
    %dup/vec4;
    %pushi/vec4 1, 0, 2;
    %cmp/u;
    %jmp/1 T_0.5, 6;
    %dup/vec4;
    %pushi/vec4 2, 0, 2;
    %cmp/u;
    %jmp/1 T_0.6, 6;
    %pushi/vec4 0, 0, 32;
    %assign/vec4 v0x7fd3b1c27120_0, 0;
    %jmp T_0.8;
T_0.4 ;
    %load/vec4 v0x7fd3b1c27430_0;
    %assign/vec4 v0x7fd3b1c27120_0, 0;
    %jmp T_0.8;
T_0.5 ;
    %load/vec4 v0x7fd3b1c26ee0_0;
    %assign/vec4 v0x7fd3b1c27120_0, 0;
    %jmp T_0.8;
T_0.6 ;
    %load/vec4 v0x7fd3b1c27240_0;
    %assign/vec4 v0x7fd3b1c27120_0, 0;
    %jmp T_0.8;
T_0.8 ;
    %pop/vec4 1;
    %load/vec4 v0x7fd3b1c26610_0;
    %pushi/vec4 0, 0, 32;
    %cmp/e;
    %flag_get/vec4 4;
    %assign/vec4 v0x7fd3b1c272f0_0, 0;
T_0.2 ;
T_0.1 ;
    %jmp T_0;
    .thread T_0;
    .scope S_0x7fd3b1c13680;
T_1 ;
    %pushi/vec4 0, 0, 32;
    %store/vec4 v0x7fd3b1c27880_0, 0, 32;
    %pushi/vec4 1, 0, 32;
    %store/vec4 v0x7fd3b1c27b40_0, 0, 32;
    %end;
    .thread T_1;
    .scope S_0x7fd3b1c13680;
T_2 ;
    %delay 5, 0;
    %load/vec4 v0x7fd3b1c27760_0;
    %inv;
    %assign/vec4 v0x7fd3b1c27760_0, 0;
    %jmp T_2;
    .thread T_2;
    .scope S_0x7fd3b1c13680;
T_3 ;
    %vpi_call 2 30 "$dumpfile", "alu_ah.vcd" {0 0 0};
    %vpi_call 2 31 "$dumpvars", 32'sb11111111111111111111111111111111, S_0x7fd3b1c13320 {0 0 0};
    %vpi_call 2 32 "$monitor", "%b", v0x7fd3b1c279e0_0 {0 0 0};
    %end;
    .thread T_3;
    .scope S_0x7fd3b1c13680;
T_4 ;
    %pushi/vec4 0, 0, 1;
    %store/vec4 v0x7fd3b1c27760_0, 0, 1;
    %pushi/vec4 0, 0, 1;
    %store/vec4 v0x7fd3b1c27a90_0, 0, 1;
    %pushi/vec4 0, 0, 32;
    %store/vec4 v0x7fd3b1c27640_0, 0, 32;
    %pushi/vec4 0, 0, 32;
    %store/vec4 v0x7fd3b1c276d0_0, 0, 32;
    %end;
    .thread T_4;
    .scope S_0x7fd3b1c13680;
T_5 ;
    %wait E_0x7fd3b1c09d10;
    %vpi_func 2 44 "$random" 32, v0x7fd3b1c27b40_0 {0 0 0};
    %store/vec4 v0x7fd3b1c27640_0, 0, 32;
    %vpi_func 2 45 "$random" 32, v0x7fd3b1c27b40_0 {0 0 0};
    %store/vec4 v0x7fd3b1c276d0_0, 0, 32;
    %vpi_func 2 46 "$random" 32, v0x7fd3b1c27b40_0 {0 0 0};
    %pad/s 2;
    %store/vec4 v0x7fd3b1c277f0_0, 0, 2;
    %load/vec4 v0x7fd3b1c27880_0;
    %pushi/vec4 1, 0, 32;
    %add;
    %store/vec4 v0x7fd3b1c27880_0, 0, 32;
    %jmp T_5;
    .thread T_5;
    .scope S_0x7fd3b1c13680;
T_6 ;
    %wait E_0x7fd3b1c137e0;
    %pushi/vec4 99999, 0, 32;
    %load/vec4 v0x7fd3b1c27880_0;
    %cmp/s;
    %jmp/0xz  T_6.0, 5;
    %vpi_call 2 53 "$finish" {0 0 0};
T_6.0 ;
    %jmp T_6;
    .thread T_6;
# The file index is used to find the file name in the following table.
:file_names 4;
    "N/A";
    "<interactive>";
    "ALU_tb.v";
    "ALU.v";
