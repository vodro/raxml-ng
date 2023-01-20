#!/bin/bash
DataList="1-2, 3-4, 5-6, 7-8, 9-10, 11-12, 13-14, 15-16, 17-18, 19-20, 21-22, 23-24, 25-26, 27-28, 29-30, 31-32"
Field_Separator=$IFS

# set comma as internal field separator for the string list
IFS=", "
mkdir -p terrace_output
for val in $DataList;
do
 x=$val
 ./run_preProcessor.sh $x > terrace_output/$x.txt
done

IFS=$Field_Separator