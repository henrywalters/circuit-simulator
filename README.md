# circuit-simulator

This simulator allows you to investigate the inner workings of intergrated circuit chips using logical gates.  The added benefit from it existing as a python library is the ability to create complex circuits abstractly without the hinderence of gui's often found with circuit simulators.


Library Functions

These are the 6 basic logical operatiors

OR(a,b)     
AND(a,b)  
XOR(a,b)  
NOT(a)
NAND(a,b)
NOR(a,b)

combining the XOR and AND gates, half adders and subbers are created

half_adder(a,b)   
half_sub(a,b) 

combing two half_adders or subbers, you can create a full adder circuit

full_adder(a,b,cin)         
full_subtractor(a,b,cin)  

utilizing the combination and flow of data through full adders, addition and subtraction may be done 
at any bit size.

addByBit(bit,a,b)    
subByBit(bit,a,b)

combining addition and subtraction circuits, multiplcation and division is possible

multiplyByBit(bit,a,b) 
divideByBit(bit,a,b)   

House keeping functions
to smoothly handle interface the following functions exist

clean(bit_array)  
convertToBit(bit,n)  
convertToInt(n)   

*** you may wonder why these are even used instead of bin(), the purpose of this library is to explore the 
    manipulation of binary

reverse(array) 


