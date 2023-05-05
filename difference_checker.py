def compare_text_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    differences = []
    extra_lines = None

    # Check for lines present in both files
    for i, line in enumerate(lines1):
        if i >= len(lines2):
            extra_lines = lines2[len(lines1):]
            break

        if line != lines2[i]:
            differences.append((i + 1, line.strip(), lines2[i].strip()))

    # Check for extra lines in file2
    if extra_lines is None and len(lines2) > len(lines1):
        extra_lines = lines2[len(lines1):]

    # Print differences and extra lines
    if differences:
        print(f"Differences between {file1} and {file2}:")
        for line_number, line1, line2 in differences:
            print(f"\tLine {line_number}:")
            print(f"\t\t{file1}: {line1}")
            print(f"\t\t{file2}: {line2}")

    if extra_lines is not None:
        print(f"Extra lines in {file2}:")
        for line in extra_lines:
            print(f"\t{line}")


compare_text_files("config.txt", "config1.txt")
