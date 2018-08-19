from scipy.stats import binom

n = 50
k = 5
#probability of getting D is 
p = 1/5

print(binom.pmf(k,n,p))
