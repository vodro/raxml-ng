# $1="3-4"
#mkdir -p in
#cp dataset/taxa-37/gene-tree/noscale.200g.500b/1_gt.tre in/
#cp dataset/15-taxon/100gene-100bp/1_gt.tre in/
#python preprocessor.py
#python postprocessor.py
cp out/incomplete/$1/astral/1_gt_species.out.tre input.nwk
cp out/incomplete/$1/gt/1_gt.tre gt.tre
jupyter nbconvert --to script processor.ipynb
python processor.py
./bin/raxml-ng input.nwk input.data