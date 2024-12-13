import random
import pandas as pd

# File path to the markdown file
file_path = "README.md"

# Read and parse the Markdown file
def read_md_file(file_path):
    df = pd.read_csv(file_path, delimiter="|", skiprows=2, names=["Name", "Hosted Count", "Randomized Sort"], skipinitialspace=True)
    df = df.dropna().reset_index(drop=True)  # Clean up NaNs and reset index
    df["Hosted Count"] = df["Hosted Count"].astype(int)
    return df

# Update the file after selecting the next host
def write_md_file(file_path, df):
    with open(file_path, "w") as f:
        f.write("# Meeting Hosts\n\n")
        f.write("| Name       | Hosted Count | Randomized Sort |\n")
        f.write("|------------|--------------|-----------------|\n")
        for _, row in df.iterrows():
            f.write(f"| {row['Name']} | {row['Hosted Count']} | {row['Randomized Sort']} |\n")

# Main logic for selecting the next host
def pick_next_host():
    df = read_md_file(file_path)
    df["Randomized Sort"] = df["Hosted Count"] * 100 + [random.randint(0, 99) for _ in range(len(df))]
    df = df.sort_values(by=["Randomized Sort"]).reset_index(drop=True)
    next_host = df.iloc[0]["Name"]
    df.loc[0, "Hosted Count"] += 1
    write_md_file(file_path, df)
    print(f"The next host is: {next_host}")

if __name__ == "__main__":
    pick_next_host()
