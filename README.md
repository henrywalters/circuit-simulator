# circuit-simulator

This simulator allows you to investigate the inner workings of intergrated circuit chips using logical gates.  The added benefit from it existing as a python library is the ability to create complex circuits abstractly without the hinderence of gui's often found with circuit simulators.


Library Functions


OR(a,b)     *These are the 6 logic gates that can be used to create most any icc
AND(a,b)    *Google search 'logic gates' will provide much more succinct information than 
XOR(a,b)    *I will, and also pictures :)
NOT(a)
NAND(a,b)
NOR(a,b)

half_adder(a,b)   *These circuits are the most basic of arithematic operators
half_sub(a,b)     *a and b are either single digit binary numbers which return a sum and carry

full_adder(a,b,cin)       *These circuits utilize the half circuits to create a circuit which
full_subtractor(a,b,cin)  *takes in a carry over digit

addByBit(bit,a,b) *To leave dynamics you may choose to add a 2 bit number or a 1000 bit number
subByBit(bit,a,b) *These circuits are created by the combination and flow of full adder and subtractors

multiplyByBit(bit,a,b)  *These circuits take advantage of the above simpler circuits.  I hope the trend
divideByBit(bit,a,b)    *is becoming obvious.

House keeping functions
to smoothly handle interface the following functions exist

clean(bit_array)  *This function converts the produced binary array and returns a neat integer
convertToBit(bit,n)  *turns n into a binary number of any bit
convertToInt(n)   *turns bin num into an int

*** you may wonder why these are even used instead of bin(), the purpose of this library is to explore the 
    manipulation of binary

reverse(array) *when a circuit handles binary, it may start from the left side or the right, it is nice to be able
               glide between directions.

