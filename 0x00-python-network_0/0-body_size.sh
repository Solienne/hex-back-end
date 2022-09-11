#!/bin/bash
#Display the the body size of the response
curl -sI $1 | grep "Content-Length" | cut -d " " -f
