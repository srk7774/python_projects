import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

dat = sm.datasets.get_rdataset("Guerry", "HistData").data
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

print(results.summary())

