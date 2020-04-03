# Data analysis project

Our project is titled "Financial analysis - abnormal sales" and is about an econometric analysis of hundreds of companies with focus on sales.

The results of the project can be seen from running [dataproject.ipynb](dataproject.ipynb).

This loades one dataset (from a finance course at UCSD):

1. "financials.csv" downloaded from https://wrds-www.wharton.upenn.edu/?_ga=2.173040611.1389363270.1585921655-712757406.1585388435

Apart from a standard Anaconda Python 3 installation, the project requires the following installations:
import pandas as pd
import statsmodels.formula.api as sm
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.stats.outliers_influence as sm_influence
from patsy import dmatrices
import statsmodels.api as sm_non_formula
