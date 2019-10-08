import pandas as pd

tcp_flags = {
    '0x002': 'SYN',
    '0x018': '(PSH, ACK)',
    '0x010': 'ACK',
    '0x012': '(SYN, ACK)',
    '0x014': '(RST, ACK)',
    '0x004': 'RST',
    '0x011': '(FIN, ACK)',
    '0x019': '(FIN, PSH, ACK)'
}

df_file = "for_the_afternoon.csv"

df = pd.read_csv(df_file)


def get_vendor(string: str):
    return string.split("_")[0]


def convert_to_int(to_convert):
    try:
        return int(to_convert)
    except ValueError:
        return to_convert


df['TCP Flags'] = df['TCP Flags'].apply(tcp_flags.get)
df['Vendor'] = df['Vendor'].apply(get_vendor)
df['Source Port'] = df['Source Port'].apply(convert_to_int)
df['Destination Port'] = df['Destination Port'].apply(convert_to_int)

