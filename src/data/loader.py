import pandas as pd 
from pathlib import Path 

def load_raw_options(data_dir: str) -> pd.DataFrame: 
    "Load all daily option CSVs from data_dir into a single DataFrame.""" 
    data_path = Path(data_dir) 
    csv_files = sorted(data_path.glob("*.csv")) 

    frames = [] 
    for f in csv_files: 
        df = pd.read_csv(f, parse_dates = ["quote_date", "expiration"])
        frames.append(df)

    return pd.concat(frames, ignore_index = True) 

def filter_spx(df: pd.DataFrame) -> pd.DataFrame: 
    """Keep only SPX and SPXW contracts. Verify all are European-style contracts.""" 
    df = df[df["underlying"].isin(["SPX", "SPXW"])].copy() 

    non_european = df[df["style"] != "E"] 
    if len(non_european) > 0: 
        raise ValueError( 
            f"{len(non_european)} rows are not European-style. Check data."
        )

    return df 