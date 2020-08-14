# This code is a demo for scenario reduction for randomly generated scenarios
import FCP_mdlAux
import numpy as np
import matplotlib.pyplot as plt

#initial number of scenarios.
n_sc = 50

#final number of scenarios.
n_rd = 5

#number of parameters per scenario.
n_param = 20
  
scdata = np.random.rand(n_sc,n_param)
input_weights = [(1/n_sc) for i in range(n_sc)]

sc_m = FCP_mdlAux.Scenario_Manager()
final_weights = sc_m.Scenario_Reduction(scdata, input_weights, n_rd)

print(final_weights)
fig,ax = plt.subplots()
for i in range(scdata.shape[0]):
    ax.plot(scdata[i,:], linewidth=1 if not(i in final_weights) else 5)

plt.show()



 
