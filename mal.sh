for i in {0..9}; do 
    echo "MAL-0$i.PL0";
    ./test.py res/mal/MAL-0$i.PL0;
    echo;
done
