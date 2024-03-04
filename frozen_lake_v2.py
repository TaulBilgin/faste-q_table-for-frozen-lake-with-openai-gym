import gym
import torch
import random

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

env = gym.make('FrozenLake-v1',  render_mode="human", is_slippery=False)

action_space_size = env.action_space.n
state_space_size =  env.observation_space.n

q_table = torch.zeros(state_space_size, action_space_size).to(device) # Q value table


for _ in range(10):
    print(1)
    for v0 in range(state_space_size):
        for v1 in range(action_space_size):
            if q_table[v0][v1] == 2:
                q_table[v0][v1] = 0
    stop = False
    done = False

    while not stop:
        now = env.reset()
        for i in range(4):
            if q_table[0][i] == 2:
                stop = True
                steps = 0
                
        while not done: 
            if stop == True:
                steps += 1
            item_of_0 = []
            item_of_2 = []
            item_of_1 = []
            now_state = now[0]
            
           # decide to what move
            for i in range(4):
                if q_table[now_state][i] == 0:
                    item_of_0.append(i)

                elif q_table[now_state][i] == 2:
                    item_of_2.append(i)

                elif q_table[now_state][i] == -1:
                    item_of_1.append(i)
                
            if len(item_of_1) == 4:
                break
                
            if len(item_of_2) != 0:
                action = random.choice(item_of_2)

            elif len(item_of_2) == 0:
                action = random.choice(item_of_0)

            # change to q_table by movement
            future = env.step(action)
            future_state = future[0]
            future_reward = future[1]
            future_done = future[2]

                
            env.render()
            now = future


            if future_reward == 1:
                q_table[now_state][action] = 2

            if future_state == now_state:
                q_table[now_state][action] = -1
                
            for i in range(4):
                if q_table[future_state][i] == 2:
                    q_table[now_state][action] = 2

            if future_done == True and future_reward == 0 : 
                q_table[now_state][action] = -1
                break
            if future_reward == 1:
                break
            
        if stop == True:
            print(q_table)
            print(steps)
            print("--------")




        
        






