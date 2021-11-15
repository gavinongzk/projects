import numpy as np
import pandas as pd

states = [1, 0, -1]


prob_dict = {
    
    0: [1, 0, 0],
    1: [0.5, 0.5, 0],
    2: [0.33, 0.67, 0],
    3: [0.25, 0.75, 0],
    4: [0.25, 0.5, 0.25],
    5: [0.25, 0.5, 0.25],
    6: [0.2, 0.55, 0.25],
    7: [0.2, 0.55, 0.25],
    8: [0.2, 0.50, 0.3],
    9: [0.2, 0.50, 0.3]

    
    }


NUM_TRIALS = 100000
    
def i_list(NUM_TRIALS=NUM_TRIALS, initial_level=0, level_to_reach=6):

    i_list = []
    
    
    def prob():
        
        i = 0
        
        level = initial_level
    
        while level < level_to_reach:
                
            state = np.random.choice(states, p=prob_dict[level])
            
            level += state
            
            i += 1
    
        return i

    for n in range(NUM_TRIALS):

        i_list.append(prob())
    
    i_list_df = pd.Series(i_list)
    
        
    return i_list_df
    

i_list_df = i_list(initial_level=4)

i_list_df.describe()


plot = i_list_df.plot(kind='density').set_xlim(-25,100)


plot.set_xlim(0, 100)

plot.show()

