import os

# Set the directory containing the text files to be merged
directory = r"C:\Users\MD00875297\Desktop\backup"


# Set the name for the merged file
merged_file = "merged.txt"

# Open the merged file in write mode
with open(merged_file, "w") as outfile:
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a text file
        if filename.endswith(".txt"):
            # Open the file in read mode and read its contents
            with open(os.path.join(directory, filename), "r") as infile:
                contents = infile.read()
            # Write the contents of the file to the merged file
            outfile.write(contents)
            print("success")

