# if [ -f "terrace_output/15-18.txt.raxml.consensusTreeMRE" ]; then
#     echo "File exists."
#     rm -r "terrace_output/15-18.txt.raxml.consensusTreeMRE"
#     rm -r "terrace_output/15-18.txt.raxml.log"
# fi

./bin/raxml-ng --consense MRE --tree "$1" --prefix "$2"/"$3"
