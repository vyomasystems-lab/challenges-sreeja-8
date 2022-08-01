# SEQUENCE DETECTOR 1011 Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![gitpod_image](https://user-images.githubusercontent.com/81299825/182123886-34b15364-8acf-4615-870f-1a9673f2cf67.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (sequence detector module here) which takes  1-bit inputs *inp_bit*  certain times as a sequencce and gives a one 1-bit output *seq_seen* when a particular sequence 1011 has been detected in the sequence of input bits.

The values are assigned to the input ports 
```
dut.inp_bit.value=0 0r 1
```
 
declared a string str1 which will append the sequence of bits 
From 4th bit onwards a substring called b will be extracted from preceeding 4 bits to current bit position
if b is equal to 1011 then flag is assigned to 1

The assert statement is used for comparing the seq_seen  to the selected flag ouput.


The following errors have seen:
``` 
 assert dut.seq_seen.value == flag  , "Randomised test failed with:{seq_seen}!= {flag} for sequencce {b} at {i} th bit ".format(flag=flag,
                     AssertionError: Randomised test failed with:0!= 1 for sequencce 1011 at 20 th bit 
```

## Test Scenario **(Important)**
- Test Inputs: random inputs have given as inp_bit  and a string will store the sequence of bits
- Expected Output: As explained above if flag is 1 then seq_seen should be high
- Observed Outputs in the DUT are indicating that seq_seen is not high even when the flag is high(i.e., even after pattern  is found in the sequence)

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, it has been observed that there are some state assignments that needs to be changed as per the given sequence 1011 

```
 SEQ_10:
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;              ===> BUG here the next state should be SEQ_10;
      end
      SEQ_1011:
      begin
        next_state = IDLE;      ===>BUG The next_states should be SEQ_1 if input is 1 or else SEQ_10; 
      end



```
From the above details  improper state assignment  bugs has been identified


## Design Fix
Updating the design and re-running the test makes the test pass.

```
0010000110010000001100010000101110110101100111111
1 0
1110
00100001100100000011000100001011101101011001111110
0 0
515000.00ns INFO     test_seq_bug1 passed
515000.00ns INFO     *********************************************************************************************
                     ** TEST                                 STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     *********************************************************************************************
                     ** test_seq_1011_bugfree.test_seq_bug1   PASS      515000.00           0.02   32522306.67  **
                     *********************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                    515000.00           0.03   18203830.81  **
                     *********************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-sreeja-8/level1_design2/level1_design2_bugfree'
```

The updated design has been created in another folder "level1_design2_bugfree" within level1_design2 folder and the design has been verified and the bug has been fixed.

## Verification Strategy
 *random inputs have given as inp_bit one by one  and a string str1 will store the sequence of bits
 *From 4th bit onwards a substring called b will be extracted from preceeding 4 bits to current bit position
 *A variable called flag is assigned to initially  and if b is equal to 1011 then flag is assigned to 1
 *The assert statement is used for comparing the seq_seen  to the selected flag ouput. If it matches then the test would pass otherwise it will show an error.

