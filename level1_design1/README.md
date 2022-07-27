# Adder Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![](https://i.imgur.com/miWGA1o.png)

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

![](https://i.imgur.com/5XbL1ZH.png)

The updated design has been created in another folder "level1_design_bugfree" within level1_design1 folder and the design has been verified and the bug has been fixed.

## Verification Strategy


