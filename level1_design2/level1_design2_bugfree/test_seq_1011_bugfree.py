# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge,Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    str1=""
    
    for i in range(50):
        A=random.randint(0,1)
        dut.inp_bit.value=A
        await FallingEdge(dut.clk)
        out1=dut.seq_seen.value
        str1=str1+str(A)
        b=""
        flag=0
        if(i>=3):
            b=str1[i-3:i+1]
            print(b)
            if(b=="1011"):
                print("entering into if ")
                flag=1       
        print(str1)
        print(A,out1)
        "print(dut.current_state,dut.next_state)"
        
        assert dut.seq_seen.value == flag  , "Randomised test failed with:{seq_seen}= {flag} for sequencce {b} at {i} th bit ".format(flag=flag,
         seq_seen=dut.seq_seen.value ,b=b,i=i)



      
    