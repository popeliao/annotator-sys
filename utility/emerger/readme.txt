ABOUT THE DATA
psb_first_50_200_annotated.txt is the annotated doc you gave me.

psb_first_50_200_unannotated.txt is produced by delete extra '<' and '>' from the raw data doc you gave me.


ABOUT THE TOOL
usage: 
python emerger.py file1 file2 file3

input: 
file 1: unannotated docs without '<' '>' other than '<doc>'
file 2: annotated docs maybe with extra '<' '>'

file 3: the name of merged doc you want to be written in

The screen would print where the difference occurs if there's one.