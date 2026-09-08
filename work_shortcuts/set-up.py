import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
data_dir = current_dir / "data"

current_csv=pd.read_csv(data_dir / "current.csv")
previous_csv=pd.read_csv(data_dir / "previous.csv")

current_csv=(current_csv[current_csv["source"]!="DSC" & 
                         (current_csv["sport"]!="Tennis") ]
)

for index, row in current_csv.iterrows():
    for index2, row2 in previous_csv.iterrows():
    if (current_csv.loc[index, row]["server"] == previous_csv.loc[index2, row2]["server"]) 
    and (current_csv.loc[index, row]["channel"] == previous_csv.loc[index2, row2]["channel"]):
        pass
    elif (current_csv.loc[index, row]["channel"] != previous_csv.loc[index2, row2]["channel"]) 
    and (current_csv.loc[index, row]["server"] == previous_csv.loc[index2, row2]["server"]):
        previous_csv.loc[index, "status"] ="switched server" 
    elif (current_csv.loc[index, row]["server"] not in previous_csv['server'].unique()):
        current_csv.loc[index, "status"] = "check channel"
        current_csv.loc[index, row]["status"] = "check decoder"
        
    return current_csv
        
        
