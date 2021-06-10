#!/bin/sh

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at:
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING, SOFTWARE
# DISTRIBUTED UNDER THE LICENSE IS DISTRIBUTED ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
# SEE THE LICENSE FOR THE SPECIFIC LANGUAGE GOVERNING PERMISSIONS AND
# LIMITATIONS UNDER THE LICENSE.

# -----------------------------------------------------------------------------

PWD=$(pwd)

# Due to the possibility that !!python references are contained in mkdocs.yml,
# and we'd have to properly load all necessary stuff, but we're only interested
# in the order of entries in the nav section, we're just using grep to extract
# the relevant data. First, we remove all commented out lines, to make sure that
# we don't include commented out navigation entries. Then, we use grep to
# extract all filenames
files=$( \
  grep -Ev "^ *#" mkdocs.yml | \
  grep -oE "[^ ]+\.md" | \
  tr -d '"' | \
  tr -d "'" \
)

# Preprocess each file with Pandoc and output the result to standard out
for f in $files; do
  pandoc \
    --filter $PWD/scripts/combine/preprocess.py \
    --metadata file:$f \
    --to gfm \
    docs/$f

  # Add a new line at the end for readability
  echo ""
done
