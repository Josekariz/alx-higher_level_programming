#!/bin/bash
# sends a GET request, and displays the body of the response for a 200 status code.
curl -sL -w "%{http_code}" "$1" -o /dev/null | [ "$(tail -c 3)" == "200" ] && curl -s "$1"
