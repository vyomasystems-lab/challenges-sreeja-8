module sync_fifo(
  //write interface
  rst_i,clk_i,write_en_i,wdata_i,full_out,
  //read interface
  read_en_i,rdata_out,empty_out);
    input rst_i,clk_i,write_en_i,read_en_i;
  	
//     output reg wr_err_out,rd_error_out;
    parameter DEPTH=16,WIDTH=32,PTR_WIDTH=4;
  	 input [WIDTH-1:0] wdata_i;
   // parameter WIDTH=8;
    //parameter PTR_WIDTH=4;
   
    output reg [WIDTH-1:0] rdata_out;
    output reg empty_out,full_out;
    //write  and read pointer 
    reg [PTR_WIDTH-1:0] wr_ptr,rd_ptr;
    reg [WIDTH-1:0] mem[DEPTH-1:0];
    //write and read toggle flags
    reg wr_toggle_f,rd_toggle_f;  
  
  	integer i;
  	
    
  always @(posedge clk_i) begin
    if(rst_i==1) begin
      resetting();
      for(i=0;i<DEPTH;i=i+1) mem[i]=0;
    end
    else begin
      //rst is not applied
      //wrt can happen
      if(write_en_i==1) begin
        if(full_out==1) begin
        
        end
        else begin
          //store data into memory
          mem[wr_ptr]=wdata_i;
          
          //increment the pointer
          if(wr_ptr==DEPTH-1) wr_toggle_f=~wr_toggle_f;
          wr_ptr=wr_ptr+1;
        end
      end
      //read can happen
      if(read_en_i==1) begin
        if(empty_out==1) begin
          
        end
        else begin
          //get data from memory
          rdata_out=mem[rd_ptr];
         
          //increment the read pointer
          if(rd_ptr==DEPTH-1) rd_toggle_f=~rd_toggle_f;
          rd_ptr=rd_ptr;
        end
      end   
    end 
  end
  //logic for full and empty generation
  always @(*) begin
    empty_out=0;
    full_out=0;
    if(wr_ptr==rd_ptr)begin
      if(wr_toggle_f==rd_toggle_f) empty_out=1;
      if(wr_toggle_f!=rd_toggle_f) full_out=1;
    end    
  end
  task resetting();
    begin
      rdata_out=0;
      full_out=0;
      empty_out=1;
      wr_ptr=0;
      rd_ptr=0;
      wr_toggle_f=0;
      rd_toggle_f=0;
    end
  endtask
  endmodule
