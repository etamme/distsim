import random
import statistics

# gloal "shared" state for consistent use
hosts=[0]*50

# eventually consistent local state per proxy
proxy_states=[ [0]*50 , [0]*50 , [0]*50 ]
proxy_call_attempts=[0,0,0]

proxy_distribution=[list(range(1,35)),list(range(36,50)),list(range(51,100))]

# total call attempts
total_call_attempts=100000

# crash percent is defined as 1 out of X, so if you set it as 10 it will be 1 out of 10 times
# 1 out of 100 would be 1%
crash_chance=100000
crashes=0

# loop through total call attempts
for x in range(total_call_attempts):
    
    # select a proxy
    dist=random.randint(1,100)
    p_index=0
    for i in range(3):
        if dist in proxy_distribution[i]:
            p_index=i
            # we found a matching proxy distribution, exit this inner for loop
            # increment the number of calls this proxy has been sent
            proxy_call_attempts[p_index]=proxy_call_attempts[p_index]+1
            continue

    # determine if proxy has crashed and lost state
    if random.randint(1,crash_chance) == 1:
        # reset this proxy state
        proxy_states[p_index]=[0]*50
        crashes+=1
    
    # if this proxy has no state 
    if max(proxy_states[p_index]) == 0:

            low=random.randint(0,len(proxy_states[p_index])-1)
            proxy_states[p_index][low]=proxy_states[p_index][low]+1
            hosts[low]=hosts[low]+1
    else:
        # if this proxy has any state, select the lowest call volume host
        low=proxy_states[p_index].index(min(proxy_states[p_index]))
        # increment the local proxy state for the host
        proxy_states[p_index][low]=proxy_states[p_index][low]+1

        # increment the state for the host
        hosts[low]=hosts[low]+1
        # set our local state for the host equal to what the host told us
        # this simulates receiving a actual call count from the host in the response
        proxy_states[p_index][low]=hosts[low]
#hosts.sort()
print("proxies crashed "+str(crashes)+" times")
print("standard deviation of calls per host "+str(statistics.stdev(hosts)))
with open("hosts.csv", "w") as f:
    for i in range(len(hosts)):
        text=str(i)+","+str(hosts[i])+"\n"
        f.write(text)
with open("proxy.csv", "w") as f:
    for i in range(len(proxy_call_attempts)):
        text=str(i)+","+str(proxy_call_attempts[i])+"\n"
        f.write(text)


print(*hosts, sep=',')
