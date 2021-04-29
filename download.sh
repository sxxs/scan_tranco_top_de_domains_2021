#!/usr/bin/bash

cd out/

while IFS= read -r line; do
	privacyscanner scan -m chromedevtools http://$line;
done < <(head -12621 ../de.csv)

