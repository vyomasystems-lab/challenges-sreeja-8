# SYNCHRONOUS FIFO Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![](https://imgur.com/a/QzoOwtR)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (synchronous FIFO module here) which takes  16-bit input data has been written to FIFO  as write operation and 16-bit ouput has been read from FIFO as a part of read operation.

The values are assigned to the  FIFO using for loop based on the depth
```
 for i in range(0,depth) :
        await RisingEdge(dut.clk_i)
        dut.write_en_i.value=1;
        dut.wdata_i.value=random.randint(0,pow(2,16));
```

 
declared an array arr which will append the data to array in the same order that has been written to FIFO 


The assert statement is used for comparing the rdata_out  to the  arr data which means written data of FIFO.
 assert dut.rdata_out.value== arr[i], "Randomised test failed  for {i} data which is not reading:{rdata_out}!= {writedata_in}".format(rdata_out=dut.rdata_out.value,writedata_in=arr[i],i=i) 



## Introducing bugs into design
Initially the randomised tests have been passed correctly. 
After modification of some changes 

The following errors have seen:

## ERROR 1
``` 
  assert dut.rdata_out.value== arr[i], "Randomised test failed  for {i} data which is not reading:{rdata_out}!= {writedata_in}".format(rdata_out=dut.rdata_out.value,writedata_in=arr[i],i=i)
                     AssertionError: Randomised test failed  for 2 data which is not reading:00000000000000001111100011100110!= 0000000000000000011100000001110
```

The above  error has been occured due to the non-increment of read pointer
rd_ptr=rd_ptr;

## ERROR 2
```

 assert dut.rdata_out.value== arr[i], "Randomised test failed  for {i} data which is not reading:{rdata_out}!= {writedata_in}".format(rdata_out=dut.rdata_out.value,writedata_in=arr[i],i=i)
                     AssertionError: Randomised test failed  for 1 data which is not reading:00000000000000000000000000000000!= 00000000000000000010011000110001
```
The above error  has been occured due to the non-increment of write pointer
wr_ptr=wr_ptr;

## ERROR 3
```

assert dut.full_out.value== flag1, "Randomised test failed  for {i} data which is not indicating full:{full_out}!= {flag1}".format(full_out=dut.full_out.value,flag1=flag1,i=i)
                     AssertionError: Randomised test failed  for 15 data which is not indicating full:0!= 1
```
The above has been occured due to the assignment of full_out as 0 even after writing to the depth of FIFO.
 if(wr_toggle_f!=rd_toggle_f) full_out=0;

 
## Test Scenario **(Important)**
- Test Inputs: random inputs have written to FIFO sequentially  and an array  will store the inputs in indexed manner.
- Expected Output: While reading data from FIFO the data should be read in the same order with reference to array
- Observed Outputs: Due to the modifications in DUT assertions are failing  
Output mismatches are proving that there is a design bug in the DUT

## Design Bug
Based on the above test input and analysing the design, it has been observed that there are some  assignments that needs to be changed as per the requirement 

## For ERROR 1
```
rd_ptr=rd_ptr;

```
## For ERROR 2
```
wr_ptr=wr_ptr;

```
## For ERROR 3
```
if(wr_toggle_f!=rd_toggle_f) full_out=0;

```
From the above details  improper assignment  bugs has been identified


## Design Fix
Updating the design and re-running the test makes the test pass.

```
00000000000000000100100001111001
00000000000000001000011101110000
00000000000000001100111011101011
370050.00ns INFO     test_sync_fifo_bugfree passed
370050.00ns INFO     *******************************************************************************************************
                     ** TEST                                           STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     *******************************************************************************************************
                     ** test_sync_fifo_bugfree.test_sync_fifo_bugfree   PASS      370050.00           0.01   36020009.27  **
                     *******************************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                              370050.00           0.03   14458334.41  **
                     *******************************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-sreeja-8/level3_design/level3_design_bugfree'
```

The updated design has been created in another folder "level3_design_bugfree" within level3_design folder and the design has been verified and the bug has been fixed.




