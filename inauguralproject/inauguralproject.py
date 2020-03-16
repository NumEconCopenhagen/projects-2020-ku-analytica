

## Question 1 ##

# Import packages

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# Define global parameters

m = 1
v = 10
#eps = 0.3 # We define epsilon wothin the functions later in order to being able to change it more easy.
tau0 = 0.4
tau1 = 0.1
kappa = 0.4
w = 1 # w is arbitrarily set to 1. Varies throughout problems

# Define the utility function

def u_function(c, l, v, eps):
    u = np.log(c) - v * (l**(1+1/eps))/(1+1/eps)
    return u

# Define constraint for x.

def cons(m, w, l, tau0, tau1, kappa):
    x = m + w*l - (tau0*w*l + tau1 * max(w*l - kappa, 0))
    return x

# Incorporate that c* = x. Set up objective function:

def obj_function(l, w, m, tau0, tau1, kappa, v, eps):
    c = cons(m, w, l, tau0, tau1, kappa)
    return -u_function(c, l, v, eps)

# Use optimizer function to maximize (minimize the -u_function):

def opt(w, m, tau0, tau1, kappa, v, eps):
    result = optimize.minimize_scalar(obj_function, method='bounded', bounds=(0,1), args=(w, m, tau0, tau1, kappa, v, eps))
    l_star = result.x
    c_star = cons(m, w, l_star, tau0, tau1, kappa)
    u_star = u_function(c_star, l_star, v, eps)
    return [l_star, c_star, u_star]

# Assign optimal values to variable names:

l_star = opt(w, m, tau0, tau1, kappa, v, eps=0.3)[0]
c_star = opt(w, m, tau0, tau1, kappa, v, eps=0.3)[1]
u_star = opt(w, m, tau0, tau1, kappa, v, eps=0.3)[2]

# Define function that prints results:

def print_result(w, m, tau0, tau1, kappa, v, eps=0.3):
    print(f'Opitmal labor supply is: {l_star:.3f}')
    print(f'Optimal consumption is: {c_star:.3f}')
    print(f'Corresponding utility is: {u_star:.3f}')

# Print result
#print_result(w, m, tau0, tau1, kappa, v, eps=0.3)



## Question 2 ##

# Create empty initial values of l, c and w

l_values = np.zeros(10000)
c_values = np.zeros(10000)
w_list = np.linspace(0.5,1.5, 10000)

# Create values for l and c for all 10.000 values of w between 0.5 and 1.5

for i in range(10000):
    l_values[i] = opt(w_list[i], m, tau0, tau1, kappa, v, eps=0.3)[0]
    c_values[i] = opt(w_list[i], m, tau0, tau1, kappa, v, eps=0.3)[1]

# Create plot for optimal values of l for w between 0.5 and 1.5

#plt.figure(figsize = (12,8))
#plt.scatter(w_list, l_values)
#plt.xlabel("w")
#plt.ylabel("Optimal l")
#plt.grid(True)
#plt.show()

# Create plot for optimal values of c for w between 0.5 and 1.5

#plt.figure(figsize = (12,8))
#plt.scatter(w_list, c_values)
#plt.xlabel("w")
#plt.ylabel("Optimal c")
#plt.grid(True)
#plt.show()

## Question 3 ##

# Define the tax revenue function

def tax_revenue():
    tax_total = 0
    for i in range(10000):
        tax_i = tau0 * w_list[i] * l_values[i] + tau1 * max(w_list[i]*l_values[i] - kappa, 0)
        tax_total += tax_i
    return tax_total

# Print total tax revenue

#print(tax_revenue())

## Question 4 ##

# Define new 'empty' values of l, and calculate 10.000 optimal l values for epsilon=0.1

l_values_new = np.zeros(10000)

for i in range(10000):
    l_values_new[i] = opt(w_list[i], m, tau0, tau1, kappa, v, eps=0.1)[0]

# Replicate the tax_revenue function, just substitute l_values with the new l_values_new for epsilon=0.1. Call new function tax_revenue_new    
    
def tax_revenue_new():
    tax_total_new = 0
    for i in range(10000):
        tax_i_new = tau0 * w_list[i] * l_values_new[i] + tau1 * max(w_list[i]*l_values_new[i] - kappa, 0)
        tax_total_new += tax_i_new
    return tax_total_new



# Print new total tax revenue

#print(tax_revenue_new())

## Question 5 ##

# Define a tax revenue function, where w gets drawn from a uniform distribution between 0.5 and 1.5.  
# Set random seed, and draw wage, w, for 10.000 individuals from a random, unirformly distributed mass
# Initiate an empty tax function
# Loop over all drawn wages, and repeat the optimizer function for optimal l, c and u. Allow for parameters tau0, tau1 and kappa to be 'solved'
# Define the tax function once again (called tax_z), and add for each tax calculated the value to the empty total tax function

def tax_revenue_objective(x):
    np.random.seed(12345)
    w_z = np.random.uniform(low=0.5, high=1.5,size=100)
    total_tax_z = 0
    for z, w_z in enumerate(w_z): 
        l_opt_z, c_opt_z, u_opt_z = opt(w = w_z, eps = 0.3,v = v, tau0 = x[0], tau1 = x[1], kappa = x[2], m = m)
        tax_z = tau0 * w_z * l_opt_z + tau1 * max(w_z * l_opt_z - kappa, 0)
        total_tax_z += tax_z
    return total_tax_z 

# Now define the bounds of the three parameters

bnds = ((0.0, 1.0), (0.0, 1.0), (0.0, None))

# Set initial guess equal to values from before

opt_parameters = optimize.minimize(tax_revenue_objective, method='TNC', x0=[0.4, 0.1, 0.4], bounds=bnds)

# Assign values to new paramter names

tau_0_opt=opt_parameters.x[0]
tau_1_opt=opt_parameters.x[1]
kappa_opt=opt_parameters.x[2]

#Print the function that calculates optimal paramters

print(opt_parameters)

# Print optimal paramter values

#print('Optimal tau_0 is', tau_0_opt)
#print('Optimal tau_1 is', tau_1_opt)
#print('Optimal kappa is', kappa_opt)