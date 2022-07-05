#!/bin/bash

echo "started processing $*.."
sleep $((1 + RANDOM % 3)); 
python3 attackerController.py
echo finished processing "$*";


# referred from: https://www.baeldung.com/linux/processing-commands-in-parallel
