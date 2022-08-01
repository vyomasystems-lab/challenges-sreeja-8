// See LICENSE.vyoma for more details
// Verilog module for Sequence detection: 1011
module seq_1011_bugfree(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
   assign seq_seen = current_state == SEQ_1011 ? 1 : 0;  
  // state transition
  always @(posedge clk or posedge reset)
  begin
    if(reset)
    begin
      current_state <= IDLE;
       
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(current_state or inp_bit )
  begin
    case(current_state)
      IDLE:
      begin
             
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
          
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
           
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
            
        if(inp_bit == 1)begin
          next_state = SEQ_1011;
        end
        else
          next_state = SEQ_10;
      end
      SEQ_1011:
      begin
            
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
    endcase
  end
endmodule
