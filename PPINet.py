import pandas as pd
import numpy as np
import networkx as nx
from tkinter import filedialog


with filedialog.askopenfile() as file:    
    df_prot = pd.read_csv(file)

P = nx.Graph()

P.add_nodes_from()