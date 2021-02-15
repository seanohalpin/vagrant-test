#!/bin/sh
CMD="${1-/bin/bash}"
exec docker run -v "$PWD":/docker -it --rm soha/server01 "$CMD"
