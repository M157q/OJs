# https://www.hackerrank.com/contests/the-linux-bash-fest/challenges/lonely-integer-2

read N
IFS=' ' read -a array


for i in ${array[@]}
do
    a[$i]=0
done

for i in ${array[@]}
do
    a[$i]+=$((a[$i] + 1))
done

for i in ${array[@]}
do
    if [ ${a[$i]} -eq 1 ]; then
        echo $i
        exit 0
    fi
done

