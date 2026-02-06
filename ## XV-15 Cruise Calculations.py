## XV-15 Cruise Calculations
import matplotlib as plt
import numpy as np

#Geometry Specs
S= 32.17 #ft
A=169 #ft^2

e=1/(1.05 + 0.007*np.pi*A)
K=1/(np.pi*e*A)
CD_0=0.012909
CL=0.3427
#print(e,K)

#Condition Specs
V_cruise_mph= 345
mph_to_fts= 1.46667
V_cruise= V_cruise_mph*mph_to_fts
#print(V_cruise)

rho=17.56E-4 #slugs/ft^3 @10000 ft
q=0.5*rho*(V_cruise**2)
#print(q)

#Battery Specs
E_sb= 2500 # W/kg
efficiency_b2s= 0.8


# power required for steady level flight 
def P_cruise(q,S,CD_0, K, CL, V_cruise):
    P=q*S*(CD_0 + K*(CL**2))*V_cruise
    print(P/550) #hp

P_cruise(224.8,32.17,0.012909,0.00897766,0.3427,506) #ideal HP

