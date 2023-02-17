Assignment 2
import numpy as np
L = 12 #length of the beam in meters
W = 10 #intensity of the load in kN/m
#Question A
#Bending moment(M) and shear force(V) at the first end, x=0
x=0
M = (W*(-6*x**2+6*L*x-L**2))/12
V = W*(L/2-x)
a= 'the bending moment at x=0 is'
b= 'the shear force at x=0 is'
print()
print('(A.1)'+a+str(M)+'and',b+str(V))
#bending moment(M) and shear force(V) at the last end, x=12
x=12
M = (W*(-6*x**2+6*L*x-L**2))/12
V = W*(L/2-x)
c= 'the bending moment at x=L is'
d= 'the shear force at x=L is'
print()
print('(A.2)'+a+str(M)+'and',b+str(V))
#Question B
#when the bending moment is zero, we get an expression x**2-L*x+L**2/6 = 0
#from the expression
a= 1
b= -L
c= L**2/6
#using the almighty formula, the roots are;
discriminant= b**2-4*a*c
root_1b= (-b + np.sqrt(discriminant))/2*a
root_2b= (-b - np.sqrt(discriminant))/2*a
print()
print('(B) the points of contra-flexure are {0} and {1}'. format(root_1b,root_2b))
#Question C
V=0
x=L/2
print()
print('(C) the point at which V=0 is {}'. format(x))
#Question D
L= 12
p= 0
r= 0.01
q= L+r
x= np.arange(p,q,r)
M= (W*(-6*x**2+6*L*x-L**2))/12
print()
print('(D) using the initialized variable, the bending moment at each step in the array is {0}'. format(M))
#Question E
V= W*(L/2 -x) 
print() 
print('(E) the shear force for each step along the span is {}'. format(V)) 
#Question F
#absolute M = AM
#minimum AM = m_AM
AM = abs(M)
m_AM = min(AM)
#when the bending moment is m_AM, we get an expression x**2-L*x+(L**2/6)+(2*m_AM)/W = 0
#from the expression above
a= 1
b= -L
c= (L**2/6)+(2*m_AM)/W
#using the almighty formula the roots are;
discriminant= b**2-4*a*c
root_1f= (-b + np.sqrt(discriminant))/2*a
root_2f= (-b - np.sqrt(discriminant))/2*a
print()
print('(F) the points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'. format(root_1f,root_2f))
#Question G
#let the relative erros be r_e
r_e1= ((root_1b - root_1f)/root_1b*100)
r_e2= ((root_2f - root_2b)/root_2f*100)
print()
print('(G) the relative errors between the estimated points of contra-flexure are {0}% and {1}%'. format(r_e1,r_e2))
#Question H
#maximum M = max_M
#minimum M = min_M
max_M = max(M)
#when the bending momnet is max_M, we get an expression x**2-L*x+(L**2/6)+(2*max_M)/W = 0
a= 1
b= -L
c= (L**2/6)+(2*max_M)/W
#using the almighty formula the roots are;
discriminant= b**2-4*a*c
root_1max= (-b + np.sqrt(discriminant))/2*a
root_2max= (-b - np.sqrt(discriminant))/2*a
print()
print('(H.1) the points at which the maximum bending moment occur are {0} and {1}'. format(root_1max,root_2max))
#for the minimum
min_M= min(M)
#when the bending moment is min_M, we get an expression x**2-L*x+(L**2/6)+(2*min_M)/W = 0
a= 1
b= -L
c= (L**2/6)+(2*min_M)/W
#using the almighty formula the roos are;
discriminant= b**2-4*a*c
root_1min= (-b + np.sqrt(discriminant))/2*a
root_2min= (-b - np.sqrt(discriminant))/2*a
print()
print('(H.2) the points at which the minimum bending moment occur are {0} and {1}'. format(root_1min,root_2min))

                                                            