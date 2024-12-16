import random

bits = 10
crossP = 0.8
mutaP = 0.05
#x, y range
lower = 0
upper = 6
ran = pow(2, bits)

def f(var):
    #f(x,y) = (x**2 + y - 11)**2 +(x + y**2 - 7)**2
    x = var[0]
    y = var[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2
def chromo(chromos):
    C1 = int(random.randrange(len(chromos)))
    C2 = int(random.randrange(len(chromos)))
    while C1 == C2:
        C2 = int(random.randrange(len(chromos)))
    return C1,C2
    
def singleSiteCrossover(chromos,C1,C2,offsprings,site): 
    #chromos contains array of chormosomes
    #C1, C2 represent the index of choosen chromosomes for crossover
    #offsprings is an array that holds offsprings
    #site represents the the site of crossover, the bit
    off1,off2 = chromos[C1], chromos[C2]
    #crossover
    off1,off2 = off2[:bits-site] + off1[bits-site:], (chromos[C1])[:bits-site] + off2[bits-site:]
    offsprings.append(off1)
    offsprings.append(off2)
    return offsprings
    
def twoSiteCrossover(chromos,C1,C2,offsprings,site1,site2):
    bit = bits*2
    off1,off2 = chromos[C1], chromos[C2]
    off1 = off1[:bit-site2+1] + off2[bit-site2+1:bit-site1] + off1[bit-site1:]
    off2 = off2[:bit-site2+1] + (chromos[C1])[bit-site2+1:bit-site1] + off2[bit-site1:]
    offsprings.append(off1)
    offsprings.append(off2)
    return offsprings

def mutation(chromos, C, site, offsprings):
    offspring = chromos[C]
    site = bits*2 - site #index of site
    if  offspring[site] == "1":
        offspring = offspring[:site] + "0" + offspring[site+1:]
    else:
        offspring = offspring[:site] + "1" + offspring[site+1:]

    offsprings.append(offspring)
    return offsprings


def F(x):
    return round(1/(1 + x),4)

def scale(dec, l, u):
    return [[l + (u - l)/(pow(2,bits) - 1) * x for x in pair] for pair in dec]

def genetic_algorithm():
    dec = []
    chromos = []
    F_val = []
    P = []
    offsprings = []
    for i in range(5):
        l = [ random.randrange(ran),random.randrange(ran) ]
        dec.append(l[:])  # Create a copy of the list
        bin_l = [bin(x)[2:].zfill(10) for x in l]
        chromos.append(''.join(bin_l))
    scaled_dec = scale(dec, lower, upper)
    for i in range(len(scaled_dec)):
        F_val.append(f(scaled_dec[i]))
        F_val[i] = F(F_val[i])
    s = sum(F_val)
    print("\n\nCHROMOSOMES ARE:",chromos)
    for i in range(len(F_val)):
        P.append(round(F_val[i]/s, 3))
    print("f:",F_val)
    print("P:",P)
    
    rand = 1
    while rand > crossP:
        site = int(random.randrange(bits*2))
        rand = random.random()
    print("\nSINGLE POINT CROSSOVER. Chromosome selected are:\n")
    #choosing which 2 random Chromosomes to be crossed over
    C1,C2 = chromo(chromos)
    print("Before single Point crossover Chromosome 1: ", chromos[C1])
    print("Before single Point crossover Chromosome 2: ", chromos[C2])
    print("Crossover Site: ", site)
    offsprings = singleSiteCrossover(chromos,C1,C2,offsprings,site)  
    print("After single point crossover Offspring 1: ", offsprings[0])
    print("After single point crossover Offspring 2: ", offsprings[1])
    
    #2-point Crossover
    rand = 1
    site1,site2 = 0,0
    while rand > crossP and site1 == site2:
        site1,site2 = int(random.randrange(bits*2)),int(random.randrange(bits*2))
        rand = random.random()
    #selecting 2 random Chromosomes for crossover
    print("TWO POINT CROSSOVER. They selected Chromosomes are:\n")
    C1, C2 = chromo(chromos)
    print("Chromosome 1 before two point crossover:", chromos[C1])
    print("Chromosome 2 before two point crossover:", chromos[C2])
    if site2 < site1:  #if index of site1 greater than site2 swapping site1 and site2
        temp = site1
        site1= site2
        site2 = temp
    print("Site 1: ",site1)
    print("Site 2: ",site2)
    offsprings = twoSiteCrossover(chromos, C1, C2, offsprings, site1, site2)
    print("After two point crossover Offspring 3:",offsprings[2])
    print("After two point crossover Offspring 4:",offsprings[3])
    
    #Mutation
    C = random.randrange(len(chromos))
    rand = 1
    while rand > mutaP:
        site = int(random.randrange(bits*2))
        rand = random.random()
    print("MUTATION. Chromosome selected:\n")
    print("Before mutation Chromosome:",chromos[C])
    print("Mutation site: ",site)
    offsprings = mutation(chromos,C,site,offsprings)
    print("After mutation Offspring 5:",offsprings[4])
    print("\n\nALL OFFSPRINGS:\n")
    for offspring in offsprings:
        print(offspring)             

genetic_algorithm()