import numpy as np 
from scipy.spatial import distance_matrix
 



class Scenario_Manager():
       
    def Scenario_Reduction(self,scdata,input_weights,n,use_sciPy=True):
#scdata: two-dimensional numpy array containing input scenario data, scenarios are placed in different rows and scenario parameters are arranged in columns.
#input_weights: a list representing weights for input scenarios (in most cases, all equal together with a summation of one)
#n: the number of the final representative scenarios
#use_sciPy: a boolean variable for selection of the method for calculation of the distance matrix, True->sciPy.dist_matrix is used

        print("#Scenario Reduction ...")      
        weights=input_weights.copy()
        Selected_SC =[]

        n_sc = scdata.shape[0]
        d = np.zeros(n_sc)
        Remained_SC =[i for i in range(n_sc)]
 
 
        if (use_sciPy):
              v =distance_matrix(scdata,scdata) 
        else: 
              v = np.zeros((n_sc,n_sc))            
              for i in range(n_sc-1):             
                 for j in range(i+1,n_sc):
                    v[i,j] = np.linalg.norm(scdata[i,:] - scdata[j,:])
                    v[j,i] = v[i,j]
 
 
        print("Euclidean Norms were calculated.")
        last_selected = -1
        vx = v.copy()
        for nx in range(n):
            if (last_selected !=-1):
              for i in Remained_SC: 
                      v[i,:] = np.minimum(v[i,:],v[i,last_selected])
  
            for i in Remained_SC:
               d[i] = np.dot(weights,v[:,i] )

            minind = np.argmin(d)
            Selected_SC.append(minind)
            Remained_SC.remove(minind)
            weights[minind] = 0
  
            last_selected=minind
            print("Scenario No. "+str(last_selected)+" was added. Total So far:"+str(len(Selected_SC)))

        output_weights={i:input_weights[i] for i in Selected_SC}
        mins = {dsc:min([vx[dsc,ssc]  for ssc in Selected_SC]) for dsc in Remained_SC} 
        ls = {dsc:[ssc  for ssc in Selected_SC if vx[dsc,ssc]==mins[dsc]][0] for dsc in Remained_SC}             
        output_weights ={ssc:input_weights[ssc]+sum([input_weights[dsc] for dsc in ls if ls[dsc]==ssc])for ssc in Selected_SC}
        print("#Scenario Reduction ... Finished.")

#The output is a dictionary indexed by selected scenario number and the relevant weight
        return output_weights


 