import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

czestotliwosc1 = 5
czestotliwosc2 = 15
czestotliwosc3 = 30
czestProbkowania = 250
czas = 1


sygnal=np.concatenate([np.concatenate([1*np.sin(2*np.pi*czestotliwosc1*t), 3*np.sin(2*np.pi*czestotliwosc2*t)]), 5*np.sin(2*np.pi*czestotliwosc3*t)])
