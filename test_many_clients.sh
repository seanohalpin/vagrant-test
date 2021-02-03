#!/bin/bash
NUM_CLIENTS="${1-3}"
echo "$0: START $(date)"
echo "$0: Starting $NUM_CLIENTS workers"
for ((i=1; i < NUM_CLIENTS; i++)); do
  ./client_echo.py --echo "Client $i" &
done
jobs
wait
echo "$0: DONE $(date)"
