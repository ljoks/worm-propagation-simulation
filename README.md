# worm-propagation-simulation
Modeling the spread of an internet worm like Code Red with two different spread methods
- Random Scanning
- Sequential Scanning
  - 80% chance of scanning the next 5 sequential nodes
  - 20% chance of randomly scanning 5 nodes

Set in a n=100,000 IP address space, with 1,000 vulnerable nodes.

See Report pdf for more details about problem and implementation

## Steps to Run
Install libraries necessary:
```
pip install matplotlib
```

Run random: 
```
python3 scan_random.py
```

Run Sequential:
```
python3 scan_sequential.py
```
