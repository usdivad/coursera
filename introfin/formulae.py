# Implementing Excel functions

# Week 1 (simple), 2 (annuity)
def fv(rate, nper, pmt, pv=0, type="annuity"):
    if type=="simple":
        return pv*((1+rate)**nper)
    elif type=="annuity":
        compound_sum = 0
        for x in xrange(0, nper):
            compound_sum += (1+rate)**x
        return pmt * compound_sum

# print fv(.07, 10, 0, 500, "simple") # 983.58
# print fv(.08, 40, 10000, 0, "annuity") # 2.59 million

def pv(rate, nper, pmt, fv=0, type="simple"):
    if type=="simple":
        return fv / ((1+rate)**nper)
        
# print pv(0.1, 2, 0, 121000) # 100,000


def pmt(rate, nper, pv, fv=0, type="fv"):
    if type=="fv":
        return fv /((((1+rate)**nper)-1)/rate)
        
print pmt(.08, 25, 0, 500000) # 6839