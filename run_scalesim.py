from scalesim.scale_sim import scalesim
import sys

content_path = "/home/grads/abv5402/cse530-labfiles/scale-sim-v2"
config_name = sys.argv[1]
config = content_path + "/configs/" + config_name + ".cfg"
print(config)
#topo = content_path + "/topologies/CSV/LSTM.csv"
topo = content_path + sys.argv[2]
print(f"Topology file: {topo}")
top_name = sys.argv[2].split("/")[3].split(".")[0]
print(top_name)

s = scalesim(save_disk_space=False, verbose=True,
              config=config,
              topology=topo
              )

top = "/home/grads/abv5402/cse530-labfiles/scale-sim-v2/run_output/" + top_name + "_" + config_name
s.run_scale(top_path=top)
