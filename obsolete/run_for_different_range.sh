#!/bin/bash
# DataList="1-2, 3-4, 5-6, 7-8, 9-10, 11-12, 13-14, 15-16, 17-18, 19-20, 21-22, 23-24, 25-26, 27-28, 29-30"
#DataList="1-2, 3-4, 5-6, 7-8, 9-10, 11-12, 13-14, 15-16, 17-18, 19-20"
echo "Running Preprocessing......................";
./run_preProcessor.sh

echo "Finding Terraces for different ranges......";
DataList="15-18"
Field_Separator=$IFS

# set comma as internal field separator for the string list
IFS=", "
mkdir -p terrace_output
for val in $DataList;
do
 x=$val
 ./run_RAxML_NG.sh $x> terrace_output/$x.txt
done

IFS=$Field_Separator

echo "Calculating RF Score............";
python checkRF_Score.py
# echo "Running Analysis................";
# jupyter nbconvert --to script analyzer.ipynb
# python analyzer.py
# echo "Calculating Quartet Score........";
# python checkQuartetScore.py
echo "Done..............................";
