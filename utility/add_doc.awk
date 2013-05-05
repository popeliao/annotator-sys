awk '/^<http/ {print "</doc>\n<doc>"} {print}' associated_header.txt > r.txt
additional work needed, put the first </doc> at the end