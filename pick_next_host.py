file_path = "meeting-hosts.md"

# Write back the updated DataFrame to the Markdown file
def write_md_file(file_path, df):
    try:
        with open(file_path, "w") as f:
            f.write("# Meeting Hosts\n\n")
            f.write("| Name       | Hosted Count | Randomized Sort |\n")
            f.write("|------------|--------------|-----------------|\n")
        print("File successfully updated.")
    except Exception as e:
        print(f"Error writing to the file: {e}")

write_md_file(file_path, "test")

if __name__ == "__main__":
    pick_next_host()
