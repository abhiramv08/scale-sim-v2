#!/bin/bash
#conda activate CSE530_FA23
config=$1
echo "config :"$1
topology="/topologies/conv_nets/"$2".csv"
echo "topology: "$topology
python3 run_scalesim.py ${config} $topology > logs/${2}_${1}.log &
wait
#rm -r ~/cse530-labfiles/scale-sim-v2/run_output/*/*/layer*
rm -r /scratch/abv5402/run_output/*/*/layer*
mkdir ~/cse530-labfiles/scale-sim-v2/run_output/${2}_${1}/
cp /scratch/abv5402/run_output/${2}_${1}/*/* ~/cse530-labfiles/scale-sim-v2/run_output/${2}_${1}/
