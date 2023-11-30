#!/bin/bash
# List the accepted HTTP methods for a given URL's server.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
