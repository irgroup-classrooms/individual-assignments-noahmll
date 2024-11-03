#!/bin/bash
wc -l ./shell-lesson/*.tsv | sort -nr | head -n 2 | tail -n 1