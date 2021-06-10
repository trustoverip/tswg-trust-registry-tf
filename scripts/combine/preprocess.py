#!/usr/bin/env python

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

from pandocfilters import toJSONFilter, Header, Link, RawInline

import os
import re

"""
A pandoc filter to preprocess cross-references (i.e. internal links) in multi-
file documents, in order to create a combined Markdown document.

  pandoc \
    --filter scripts/preprocess.py <full/path/basename.md> \
    --metadata file:<basename.md> \
    --to gfm \
    > tmp/<basename>.md

This script is heavily inspired by:
https://gist.github.com/ba-tno/b00e07abe25ebc2702629ec91074b1c0
"""
def preprocess(key, value, format, meta):
    prefix = normalize(meta["file"]["c"])

    # Header - set anchor name explicitly
    if key == "Header":
        [level, [anchor, t1, t2], header] = value
        anchor = prefix + "-" + anchor

        # Append attribute list with prefixed anchor
        header.append(RawInline("html", " {{ #{} }}".format(anchor)))
        return Header(level, [anchor, t1, t2], header)

    # Link - correct links
    if key == "Link":
        [t1, text, [link, t4]] = value

        # This document
        if link[0] == "#":
            ref = prefix + "-" + link[1:]
            return Link(t1, text, [ref, t4])

        # That document
        elif "#" in link:
            anchor = "#" + normalize(link)
            return Link(t1, text, [anchor, t4])

"""
Normalize anchor link
"""
def normalize(link):
    # Replace .md file endings and numbers at the beginning
    link = re.sub(r'^\d+-|\.md', r'', link)
    # Replace #-, & and /-symbol in the middle
    link = re.sub(r'#|&|\/', r'-', link)
    # Prepend the #-symbol
    return link.lower()

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    toJSONFilter(preprocess)
