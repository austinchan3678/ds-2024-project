import numpy as np
import pandas as pd
r_dtypes = {"stars": np.float16, 
            "useful": np.int32, 
            "funny": np.int32,
            "cool": np.int32,
           }

with open("/Users/yensydney/Desktop/DSProject/yelp_dataset/copyyelp_academic_dataset_tip.json", "r") as f:
    df = pd.read_json(f, orient="records", lines=True, dtype=r_dtypes)
    for i in df['text']:
        print(i)