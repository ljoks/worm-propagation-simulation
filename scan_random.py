import random
import matplotlib.pyplot as plt

A = 100000 # size of ip address space
N = 1000 # num of vulnerable computers
B = 5 # scan rate

for r in range(3):
    print("\nRun {}".format(r))
    # initialize IP Address space
    # value at index: 
    #   -1: immune computer
    #    0: vulnerable but not yet infected
    #   >0: infected for {value} ticks
    #   10: ready to scan other computers
    ip_address_space = [-1 for i in range(A + 1)]
    for i in range(1, A, 10000): 
        for j in range(100):
            ip_address_space[i+j] = 0

    # single computer is initially infected,
    # set to 10 as it should start scanning immediately
    ip_address_space[10050] = 10
    num_infected = 1

    tick = 0 # record ticks
    num_infected_discrete = [1] # record num infected over time

    # propogate worm until all vulnerable machines are infected
    while num_infected < N:
        tick += 1

        # scan ip addresses
        scanned_ips = random.sample(range(1, A + 1), ip_address_space.count(10) * B)
        
        # increment ticks for already infected computers first, so new ones are not incremented
        ip_address_space = [t+1 if (t > 0 and t < 10) else t for t in ip_address_space]

        for ip in scanned_ips:
            if ip_address_space[ip] == 0:
                ip_address_space[ip] = 1
                num_infected += 1
                if num_infected >= N:
                    break

        num_infected_discrete.append(num_infected)

        if tick % 100 == 0:
            print("Time step: {}. number of computers infected: {}".format(tick, num_infected))
        if num_infected >= N: 
            print("Total time steps: {}, Number of computers infected: {}".format(tick, num_infected))

    plt.plot(num_infected_discrete, "-", label="Run #{}".format(r))


plt.ylabel("number of infected computers")
plt.xlabel("time tick t")
plt.title("I(t) for 3 Simulations of Random Scanning Worm Propogation")
plt.legend()
plt.show()