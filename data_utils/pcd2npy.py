import open3d as o3d
import numpy as np
import os
import os.path as osp
from tqdm import tqdm

# Load PCD file
folder = "../mydata/pcd"
save_p = '../mydata/npy'

for f in tqdm(os.listdir(folder)):
    if not f.endswith('pcd'):
        continue
    pcd = o3d.io.read_point_cloud(osp.join(folder, f))
    points = np.asarray(pcd.points)
    np.save(osp.join(save_p, f.replace('.pcd', '.npy')), points)

print('done')
