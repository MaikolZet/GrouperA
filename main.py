import DataStructure as dt
import BruteForce as bt
import timeit

struct = dt.Structure(3,"Proof/Proof.txt","Proof/ProofNames.txt")
struct.randomInitialization()
struct.print()
struct.updateX(bt.BruteForce(struct.x,struct.y,struct.n,struct.k))
struct.print()
t1 = timeit.default_timer()
struct.print()
t2 = timeit.default_timer()
print("Denbora: ", t2-t1)