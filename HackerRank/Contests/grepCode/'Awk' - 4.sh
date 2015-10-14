# https://www.hackerrank.com/contests/the-linux-bash-fest/challenges/awk-4

awk ' ORS = NR%2 ? ";" : "\n" '
