#!/usr/bin/env python

import fileinput
import subprocess
import time

def process_duplicates(filenames):
    if len(filenames) < 2:
        return

    command = ["bedup", "dedup-files"]
    command.extend(filenames)
    subprocess.call(command)

def main():
    cur_sha = ""
    cur_files = []
    for line in fileinput.input():
        sha, filename = line.split(None, 1)
        sha = sha.strip()
        filename = filename.strip()
        if sha == cur_sha:
            cur_files.append(filename)
        else:
            process_duplicates(cur_files)
            time.sleep(10)
            cur_sha = sha
            cur_files = []

if __name__ == "__main__":
    main()