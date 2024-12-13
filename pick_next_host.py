import random
import pandas as pd

# File path to the markdown file
file_path = "meeting-hosts.md"

# Read and parse the Markdown file
def read_md_file(file_path):
    try:
        # Read the Markdown file while skipping the header
        df = pd.read_csv(
            file_path,
            delimiter="|",
            skiprows=2,  # Skip the first two header rows
            names=["Name", "Hosted Count", "Randomized Sort"],
            skipinitialspace=True,
            engine="python"
        )
        # Drop NaN rows and reset index
        df = df.dropna().reset_index(drop=True)
        df["Hosted Count"] = df["Hosted Count"].astype(int)
        print("DataFrame loaded successfully:")
        print(df)
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Write back the updated DataFrame to the Markdown file
def write_md_file(file_path, df):
    try:
        with open(file_path, "w") as f:
            f.write("# Meeting Hosts\n\n")
            f.write("| Name       | Hosted Count | Randomized Sort |\n")
            f.write("|------------|--------------|-----------------|\n")
            for _, row in df.iterrows():
                f.write(f"| {row['Name']} | {row['Hosted Count']} | {row['Randomized Sort']} |\n")
        print("File successfully updated.")
    except Exception as e:
        print(f"Error writing to the file: {e}")

# Main logic for selecting the next host
def pick_next_host():
    df = read_md_file(file_path)

    if df.empty:
        print("Error: The DataFrame is empty. Please check the Markdown file content.")
        return

    # Assign random numbers and sort
    df["Randomized Sort"] = df["Hosted Count"] * 100 + [random.randint(0, 99) for _ in range(len(df))]
    df = df.sort_values(by=["Randomized Sort"]).reset_index(drop=True)

    # Select the next host
    next_host = df.iloc[0]["Name"]
    print(f"The next host is: {next_host}")
    df.loc[0, "Hosted Count"] += 1  # Increment the hosted count for the selected host

    # Write the updated DataFrame back to the file
    write_md_file(file_path, df)

if __name__ == "__main__":
    pick_next_host()
