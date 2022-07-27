# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux_bugfree(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    for i in range(50):
        A = random.randint(0, 30)
        dut.sel.value = A
        arr=[]
        for j in range(0,31):
            a=random.randint(0,3)
            arr.append(a)
           

        dut.inp0.value=arr[0]
        dut.inp1.value=arr[1]
        dut.inp2.value=arr[2]
        dut.inp3.value=arr[3]
        dut.inp4.value=arr[4]
        dut.inp5.value=arr[5]
        dut.inp6.value=arr[6]
        dut.inp7.value=arr[7]
        dut.inp8.value=arr[8]
        dut.inp9.value=arr[9]
        dut.inp10.value=arr[10]
        dut.inp11.value=arr[11]
        dut.inp12.value=arr[12]
        dut.inp13.value=arr[13]
        dut.inp14.value=arr[14]
        dut.inp15.value=arr[15]
        dut.inp16.value=arr[16]
        dut.inp17.value=arr[17]
        dut.inp18.value=arr[18]
        dut.inp19.value=arr[19]
        dut.inp20.value=arr[20]
        dut.inp21.value=arr[21]
        dut.inp22.value=arr[22]
        dut.inp23.value=arr[23]
        dut.inp24.value=arr[24]
        dut.inp25.value=arr[25]
        dut.inp26.value=arr[26]
        dut.inp27.value=arr[27]
        dut.inp28.value=arr[28]
        dut.inp29.value=arr[29]
        dut.inp30.value=arr[30]
        print(A)
        await Timer(2, units='ns')
        print(arr[A],dut.out.value)
        assert dut.out.value == arr[A], "Randomised test failed with: input{input} of select line {A} with  input_value {value1} != mux_out {out}".format(input=A,
            A=dut.sel.value,value1=arr[A], out=dut.out.value )
        
       