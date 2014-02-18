# Week 1 (simple), 2 (annuity)
def fv(rate, nper, pmt, pv=0, type="annuity"):
    if type=="simple":
        return pv*((1+rate)**nper)
    elif type=="annuity":
        compound_sum = 0
        for x in xrange(0, nper):
            compound_sum += (1+rate)**x
        return pmt * compound_sum

# print fv(.07, 10, 0, 500, "simple")
# print fv(.08, 40, 10000, 0, "annuity")

def fv(rate, nper, pmt, fv=0, type="simple"):
    if type=="simple":
        return fv / ((1+rate)**nper)
        
