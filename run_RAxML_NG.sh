cp out/incomplete/$1/astral/1_gt_species.out.tre input.nwk
cp out/incomplete/$1/gt/1_gt.tre gt.tre
jupyter nbconvert --to script processor.ipynb
python3 processor.py
./bin/raxml-ng input.nwk input.data