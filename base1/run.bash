#!/bin/bash
#BV1uv411q7Mv

filename="bv.txt"

while IFS= read -r line || [[ -n "$line" ]]; do
	echo "$line" | python3 get_info.py > temp.txt
	sleep 0.5
	python3 de_json.py < temp.txt >> result.txt
done < "$filename"