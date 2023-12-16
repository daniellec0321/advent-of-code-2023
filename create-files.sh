for dir in */
do
    echo $dir
    newfile="${dir}program.py"
    cp template.py $newfile
done