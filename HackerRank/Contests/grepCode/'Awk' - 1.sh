# https://www.hackerrank.com/contests/the-linux-bash-fest/challenges/awk-1

awk '{ if ($2 =="" || $3 == "" || $4 == "") print "Not all scores are available for", $1;}'
