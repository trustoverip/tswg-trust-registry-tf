# Copyright (c) 2020 ToIP Foundation

# Pull base image from official PanDocs Latex repo
FROM pandoc/latex:2.6

# Add bash as alternative to default ash shell env in Alpine
RUN apk add --no-cache --upgrade bash python py-pip

# Add make command utility
RUN apk add --update --no-cache make=4.2.1-r2

# Add PanDoc dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade pandocfilters

# Set working directory to the name of a Docker Volume
WORKDIR /host_pandocs
