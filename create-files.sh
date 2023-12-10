for dir in */
do
    echo $dir
    if ! [[ $dir == *"01"* ]] && ! [[ $dir == *"02"* ]] && ! [[ $dir == *"03"* ]] && ! [[ $dir == *"04"* ]] && ! [[ $dir == *"05"* ]]&& ! [[ $dir == *"06"* ]]; then
        newfile="${dir}program.py"
        cp template.py $newfile
    fi
done