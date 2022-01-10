# wordpress-log-sorter

## Description
Sort Wordpress error & notification messages in debug.log by most frequent first.

## Quick start
1. Create a folder called `files` in the root folder. This holds the read/write files.
2. Download your `debug.log` from the server and move it to the `files` folder.
3. Run from root directory with `python prioritise-logs.py`

## Notes
* The output file is created automatically: `output<x>.csv`, where `<x>` is an incremented integer.
* You can import the CSV to Google sheets or whatever.
