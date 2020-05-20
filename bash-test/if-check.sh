#!/usr/bin/env bash
result = `grep "Hello" index.html | wc -l`

echo $result

if ["$result" = "1"]
then
	echo 'OK!'
    exit 0
else
	echo 'FAIL!'
    exit 1
fi