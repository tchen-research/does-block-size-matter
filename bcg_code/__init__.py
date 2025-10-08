import numpy as np
import scipy as sp

from .lanczos import *

import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['text.latex.preamble'] = r'\usepackage{charter}'
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

from cycler import cycler

default_cycler = (cycler(color=['#ffb000','#fe6100','#dc267f','#785ef0','#648fff']) +
                  cycler(marker=['^','s','h','p','8']))