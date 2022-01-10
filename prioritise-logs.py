import os
import re
from pandas import DataFrame
import time

start_time = time.time()

# Replace with your file names
# read_file = 'debug.log'
read_file = 'files/debug.old-01.log'

# Auto-increment output file name
output_version = 0
while os.path.exists(f"files/output{output_version}.csv"):
    output_version += 1
write_file = f'files/output{output_version}.csv'

# Utility vars
count = []
message = []
percent = []
total = 0

num_results = 100

regex1 = re.compile(r"\[[^\]]+\]\s?(.*)")
regex2 = re.compile(r"^=")
# Populate tally of log entries
with open(read_file) as f1:
    d = {}  # Dictionary for tally
    lines = f1.readlines()
    for line in lines:
        total += 1

        # Remove date from start of line
        line = regex1.sub(r"\1", line)
        # line = regex2.sub("'=", line) # Escape the equals sign for google sheets

        # Remove trailing \n
        line = line.rstrip("\n")
        if line in d:
            d[line] += 1
        else:
            d[line] = 1

print(f'Done populating: {time.time() - start_time} seconds')

# Populate lists for DataFrame columns
for key in d:
    message.append(key)
    count.append(d[key])
    percent.append(round(d[key]/total, 5))

# Create DataFrame with headings and data
df = DataFrame({'count': count, 'percent': percent, 'message': message})
df.sort_values(['count'], inplace=True, ascending=False)
top_rows = df.head(num_results)
top_rows.to_csv(write_file, index=False)

print(f'Finished: {time.time() - start_time} seconds')
