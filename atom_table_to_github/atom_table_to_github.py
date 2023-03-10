#!/usr/bin/python3

print("Enter table rows (separated by newlines):")
input_rows = []
while True:
    row = input()
    if not row:
        break
    input_rows.append(row)

# Replace + characters with | characters
table = []
for row in input_rows[1:]:
    row = row.replace('+', '|')
    cols = [col.strip() for col in row.split('|')[1:-1]]
    table.append(cols)

# Format and print output
output = ""
for i, row in enumerate(table[:-1]):
    row_str = " | ".join(row)
    output += f"| {row_str} |\n"


print(output)
