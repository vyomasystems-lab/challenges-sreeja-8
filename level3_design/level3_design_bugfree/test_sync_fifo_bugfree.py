
import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge,Timer



@cocotb.test()
async def test_sync_fifo_bugfree(dut):
    """Test for seq detection """

    clk_i = Clock(dut.clk_i, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clk_i.start())        # Start the clock
    depth=16;
    # reset
    dut.rst_i.value = 1
    dut.write_en_i.value=0;
    dut.read_en_i.value=0;
    dut.wdata_i.value=0;
    await FallingEdge(dut.clk_i)  
    dut.rst_i.value = 0;
    arr=[];

    await FallingEdge(dut.clk_i)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    flag1=0;
    flag2=0;
    for i in range(0,depth) :
        await RisingEdge(dut.clk_i)
        dut.write_en_i.value=1;
        dut.wdata_i.value=random.randint(0,pow(2,16));
        arr.append(dut.wdata_i.value);
        print(dut.wdata_i.value);
        print(dut.wr_ptr.value);
        print(dut.full_out.value)
    await RisingEdge(dut.clk_i)
    if(dut.wr_ptr.value==depth-1):
            flag1=1;
    print(flag1)
    await RisingEdge(dut.clk_i)
    assert dut.full_out.value== flag1, "Randomised test failed  for {i} data which is not indicating full:{full_out}!= {flag1}".format(full_out=dut.full_out.value,flag1=flag1,i=i) 
    dut.write_en_i.value=1;
    dut.wdata_i.value=0;
    print("data has been written")
    await Timer(50, units="ns")

    for i in range(0,depth) :
        await RisingEdge(dut.clk_i)
        if(i==1):
            await RisingEdge(dut.clk_i)
        dut.read_en_i.value=1;
        print(dut.rdata_out.value); 
        assert dut.rdata_out.value== arr[i], "Randomised test failed  for {i} data which is not reading:{rdata_out}!= {writedata_in}".format(rdata_out=dut.rdata_out.value,writedata_in=arr[i],i=i) 
    await RisingEdge(dut.clk_i)   
     
    dut.read_en_i.value=0;
    await Timer(50, units="ns")

    
    
       



    