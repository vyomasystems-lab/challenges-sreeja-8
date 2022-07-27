
import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge,Timer



@cocotb.test()
async def test_sync_fifo(dut):
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
    arr2=[];
    await FallingEdge(dut.clk_i)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    for i in range(0,depth) :
        await RisingEdge(dut.clk_i)
        dut.write_en_i.value=1;
        dut.wdata_i.value=random.randint(0,pow(2,16));
        arr.append(dut.wdata_i.value);
        print(dut.wdata_i.value);
    await RisingEdge(dut.clk_i)
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

    #for i in range(0,depth):
        #assert arr2[i]==arr[i],"Randomised test failed with:{readout}!= {writedata_in}".format(readout=arr2[i],writedata_in=arr[i])


    
       



    