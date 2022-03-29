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

    # initialize scan types for each ip address
    # value at index:
    #   -1: immune or not yet chosen
    #    0: sequential
    #    1: random
    scanType = [-1 for i in range(A + 1)]

    for i in range(1, A, 10000): 
        for j in range(100):
            ip_address_space[i+j] = 0

    # single computer is initially infected,
    # set to 10 as it should start scanning immediately
    ip_address_space[10050] = 10
    # choose whether the initially infected computer
    # is random or sequential
    scanType[10050] = random.choices([0,1], [80, 20], k=1)[0]
    print("scan type for 10050: {}".format(scanType[10050]))
    num_infected = 1

    tick = 0 # record ticks
    num_infected_discrete = [1] # record num infected over time

    # propogate worm until all vulnerable machines are infected
    while num_infected < N:
        tick += 1

        scanned_ips = []

        # loop through possibly vulnerable subnets of ip addresses
        for i in range(1, A, 10000): 
            for j in range(100):
                ip = i+j
                # create a running list of IPs to infect
                # after incrementing ticks below
                if ip_address_space[ip] == 10:
                    for k in range(B):
                        # sequential
                        if scanType[ip] == 0:
                            scanned_ips.append( (ip + k + 1) % A)
                        # random
                        else: 
                            scanned_ips.append(random.randint(1,A))

                # if value between 1-9, increment
                elif ip_address_space[ip] > 0 and ip_address_space[ip] < 10:
                    ip_address_space[ip] += 1
                

        for ip in scanned_ips:
            if ip_address_space[ip] == 0:
                ip_address_space[ip] = 1
                num_infected += 1
                scanType[ip] = random.choices([0,1], [80, 20], k=1)[0]
                if num_infected >= N:
                    break


        num_infected_discrete.append(num_infected)

        if tick % 100 == 0:
            print("Time step: {}. number of computers infected: {}".format(tick, num_infected))
        if num_infected >= N: 
            print("Total time steps: {}, Number of computers infected: {}".format(tick, num_infected))

    plt.plot(num_infected_discrete, "-", label="Run #{}".format(r))
    print("number of sequential nodes: {}".format(scanType.count(0)))
    print("number of random nodes: {}".format(scanType.count(1)))


plt.ylabel("number of infected computers")
plt.xlabel("time tick t")
plt.title("I(t) for 3 Simulations of Sequential Scanning Worm Propogation")
plt.legend()
plt.show()