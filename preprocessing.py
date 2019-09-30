import pandas as pd


def remove_http(v):
    if v.startswith("http://"):
        return v.split("http://")[1]
    elif v.startswith("https://"):
        return v.split("https://")[1]
    else:
        return v


attacks = "table_attack_twbooter.csv"

attack_df = pd.read_csv(attacks, delimiter=";")
attack_df["victim"] = attack_df["victim"].apply(remove_http)



