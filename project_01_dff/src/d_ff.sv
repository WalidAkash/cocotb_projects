module d_ff (
  input logic clk,
  input logic d,
  output logic q
);
  
always_ff @(posedge clk) begin : d_flip_flop
  q <= d;
end
endmodule
