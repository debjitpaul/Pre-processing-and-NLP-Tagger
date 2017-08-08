#!/bin/bash

for file in ./raw/*;
do
  echo "$file" 
  BASENAME= basename $file
  echo $BASENAME
  python3 prepossing_html.py "$BASENAME" > ../raw_clean/"$BASENAME".clean;
done
