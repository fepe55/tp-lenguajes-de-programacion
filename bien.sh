for i in {0..9}; do 
    echo "BIEN-0$i.PL0";
    ./test.py res/bien/BIEN-0$i.PL0;
    echo;
done
