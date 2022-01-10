import os
import re
from pandas import DataFrame
import time

start_time = time.time()

# Replace with your file names
# read_file = 'debug.log'
read_file = 'files/debug.log'

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

# Populate tally of log entries
with open(read_file) as f1:
    d = {}  # Dictionary for tally
    lines = f1.readlines()
    for line in lines:
        total += 1
        # Remove date from start of line
        line = re.sub(r"\[[^\]]+\]\s?(.*)", r"\1", line)
        line = re.sub(r"^=", "'=", line)
        # Remove trailing \n
        line = line.rstrip("\n")
        if line in d:
            d[line] += 1
        else:
            d[line] = 1

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

print(f'finished in {time.time() - start_time} seconds')
