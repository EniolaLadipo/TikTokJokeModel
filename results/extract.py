with open("results.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

block = []
num = ""

for line in lines:

    parsed_line = line.strip()
    block.append(parsed_line)

    if parsed_line == "-" * 40: # end of entry
        if any(f"Rating: {num}" in l for l in block):
            with open(f"results_rating_{num}.txt", "a", encoding="utf=8") as write_file:
                for x in block:
                    write_file.write(f"{x}\n")
        block = []
