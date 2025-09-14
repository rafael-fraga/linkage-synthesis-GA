from math import *

L1 = 152.4
L2 = 50.8
L3 = 177.8
L4 = 228.6
R_pa = 152.4
delta_3 = radians(30)
theta_2 = radians(30)
omega_2 = 10
alpha_2 = 0
config = "aberto"

a, b, c, d = L2, L3, L4, L1

# constantes
K1 = d/a
K2 = d/c
K3 = (a**2-b**2+c**2+d**2)/(2*a*c)
K4 = d/b
K5 = (c**2-d**2-a**2-b**2)/(2*a*b)

" A B C D E F "
A = cos(theta_2) - K1 - K2*cos(theta_2)+ K3
B = -2*sin(theta_2)
C = K1 - (K2+1)*cos(theta_2) + K3
D = cos(theta_2) - K1 + K4*cos(theta_2) + K5
E = -2*sin(theta_2)
F = K1 + (K4-1)*cos(theta_2) + K5

# theta
m = -1 if config=="aberto" else 1
theta_3 = 2*atan((-E+m*sqrt(E**2-4*D*F))/(2*D))
theta_4 = 2*atan((-B+m*sqrt(B**2-4*A*C))/(2*A))

# omega
omega_3 = L2*omega_2/L3 * sin(theta_4-theta_2)/sin(theta_3-theta_4)
omega_4 = L2*omega_2/L4 * sin(theta_2-theta_3)/sin(theta_4-theta_3)

# velocidade (A)
v_Ax = L2*omega_2*(-sin(theta_2))
v_Ay = L2*omega_2*cos(theta_2)
v_A = sqrt(v_Ax**2 + v_Ay**2)
arg_v_A = atan(v_Ay/v_Ax)+pi if atan(v_Ay/v_Ax)<0 else atan(v_Ay/v_Ax)

# aceleração (A)
a_Ax = (-L2)*alpha_2*sin(theta_2)-L2*omega_2**2*cos(theta_2)
a_Ay = L2*alpha_2*cos(theta_2)-L2*omega_2**2*sin(theta_2)
a_A = sqrt(a_Ax**2+a_Ay**2)
arg_a_A = atan(a_Ay/a_Ax)

" A B C D E F "
A = c*sin(theta_4)
B = b*sin(theta_3)
D = c*cos(theta_4)
E = b*cos(theta_3)
C = (
    a*alpha_2*sin(theta_2)
    + a*omega_2**2*cos(theta_2)
    + b*omega_3**2*cos(theta_3)
    - c*omega_4**2*cos(theta_4)
    )
F = (
    a*alpha_2*cos(theta_2)
    - a*omega_2**2*sin(theta_2)
    - b*omega_3**2*sin(theta_3)
    + c*omega_4**2*sin(theta_4)
    )

# alpha
alpha_3 = (C*D-A*F)/(A*E-B*D)
alpha_4 = (C*E-B*F)/(A*E-B*D)

# velocidade (B)
v_Bx = L4*omega_4*(-sin(theta_4))
v_By = L4*omega_4*cos(theta_4)
v_B = sqrt(v_Bx**2 + v_By**2)
arg_v_B = atan(v_By/v_Bx)+pi if atan(v_By/v_Bx)<0 else atan(v_By/v_Bx)

# aceleração (B)
a_Bx = -L4*alpha_4*sin(theta_4) - L4*omega_4**2*cos(theta_4)
a_By = L4*alpha_4*cos(theta_4) - L4*omega_4**2*sin(theta_4)
a_B = sqrt(a_Bx**2 + a_By**2)
arg_a_B = atan((a_By/a_Bx))

# velocidade (P)
v_Px = R_pa*omega_3*(-sin(theta_3+delta_3))
v_Py = R_pa*omega_3*(cos(theta_3+delta_3))
v_P = sqrt((v_Px+v_Ax)**2+(v_Py+v_Ay)**2)
arg_v_P = atan((v_Py+v_Ay)/(v_Px+v_Ax))

# aceleração (P)
a_Px = -R_pa*alpha_3*sin(theta_3+delta_3) - R_pa*omega_3**2*cos(theta_3+delta_3)
a_Py = R_pa*alpha_3*cos(theta_3+delta_3) - R_pa*omega_3**2*sin(theta_3+delta_3)
a_P = sqrt((a_Px+a_Ax)**2+(a_Py+a_Ay)**2)
arg_a_P = atan((a_Py/a_Px))
