# MULTIPLEXER Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![](https://ibb.co/cDYWg9C)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes  32 2-bit inputs *inp0*  to *inp30* and gives a one 2bit output *out* based on 5-bit select line *sel*

The values are assigned to the input ports using an array
Initially random  values are stored in an array by running a for loop for 32 times
```
 for i in range(31):
        A = random.randint(0, 30)
        dut.sel.value = A
        arr=[]
        for i in range(0,31):
            a=random.randint(0,3)
            arr.append(a)
           

        dut.inp0.value=arr[0]
        dut.inp1.value=arr[1]
        '
        '
        '
        '
        '
        dut.inp30.value=arr[30]
```

The assert statement is used for comparing the mux output to the selected input value.


The following errors have seen:
``` 
assert dut.out.value == arr[A], "Randomised test failed with: input{input} of select line {A} with  input_value {value1} != mux_out {out}".format(input=A,
                     AssertionError: Randomised test failed with: input12 of select line 01100 with  input_value 1 != mux_out 00
```
```
assert dut.out.value == arr[A], "Randomised test failed with: input{input} of select line {A} with  input_value {value1} != mux_out {out}".format(input=A,
                     AssertionError: Randomised test failed with: input13 of select line 01101 with  input_value 1 != mux_out 11
```
```
assert dut.out.value == arr[A], "Randomised test failed with: input{input} of select line {A} with  input_value {value1} != mux_out {out}".format(input=A,
                     AssertionError: Randomised test failed with: input30 of select line 11110 with  input_value 1 != mux_out 00

```

## Test Scenario **(Important)**
- Test Inputs: random inputs have given to mux inputs with an array and random select lines have been generated
- Expected Output: arr[selectline] value= out value
- Observed Outputs in the DUT are failing for inputs 12,13 and 30.

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, it has been observed that there is 

```
 5'b01101: out = inp12;
 5'b01101: out = inp13;
                                =====> BUG
 5'b11101: out = inp29;
      default: out = 0;
```
From the above details following bugs has been identified
For the mux design, there are two same case matching statements for 12,13 input ports which will result in 0 output for select value 12 and input12 value as ouput for select value 13 and there is no case matching statement for input port 30.

## Design Fix
Updating the design and re-running the test makes the test pass.

```
1 01
29
1 01
18
0 00
   100.00ns INFO     test_mux_bugfree passed
   100.00ns INFO     *******************************************************************************************
                     ** TEST                               STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     *******************************************************************************************
                     ** test_mux_bugfree.test_mux_bugfree   PASS         100.00           0.02       4548.89  **
                     *******************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                     100.00           0.03       3265.81  **
                     *******************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-sreeja-8/level1_design1/level1_design_bugfree'
```

The updated design has been created in another folder "level1_design_bugfree" within level1_design1 folder and the design has been verified and the bug has been fixed.

## Verification Strategy
Integer A has been assigned to sel value .
for every A value using for loop all 32 inputs of mux were first stored in an array and then assigned to inputs based on array index.
Then assertion has been made which compares DUT out value with array[A] which means array[sel].

