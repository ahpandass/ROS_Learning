
x = [825,1220,1350,1465,1550,1625,1680,1725,1770,1800,1820,1865,1885,1900,1930]
y = [800,1200,1400,1600,1800,2000,2400,2600,2800,3000,3200,3400,3600,3800,4000]


inneral = 2920
external = 2895
width_wheel_half = 13
length_chop = 209
width_axis = 125

--> fact = 0.99144



z = 5
z = 4: 1280 1545
z = 3.5:1525 1750
z = 3: 1775 1940
z = 2.5: 1965 2115
z = 2: 2113 2210
z = 1.5: 2230 2410



def dist2pwm(dist_m):
    dist = dist_m*200
    if dist < 825
        y = 0
    if dist in range(825,1220):
        y = 1.013*x - 35.44
    elif dist in range(1220,1350):
        y = 1.538*x - 676.9
    elif dist in range(1350,1465):
        y = 1.739 *x -947.8
    elif dist in range(1465,1550):
        y = 2.353 *x -1847
    elif dist in range(1550,1625):
        y = 2.667 *x -2333
    elif dist in range(1625,1680):
        y = 7.273 *x - 9818
    elif dist in range(1680,1725):
        y = 4.444 *x -5067
    elif dist in range(1725,1770):
        y = 4.444 *x -5067
    elif dist in range(1770,1800):
        y = 6.667 *x -9000
    elif dist in range(1800,1820):
        y = 10    *x -15000
    elif dist in range(1820,1865):
        y = 4.444 *x -4889
    elif dist in range(1865,1885):
        y = 10    *x -15250
    elif dist in range(1885,1900):
        y = 13.33 *x -21530
    elif dist in range(1900,1930):
        y = 6.667 *x -8867  
    else y = 4096
    return y

def calc_fact(left_v):
    return left_v / 0.99144