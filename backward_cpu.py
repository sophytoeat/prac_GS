import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import numpy as np
# from gsplat.sh_coef import *
# from gsplat.gau_io import *


def project(pc, fx, fy, cx, cy, calc_J=False):
    x, y, z = pc
    z_2 = z * z
    u = np.array([x * fx / z + cx, y * fy / z + cy])
    if (calc_J is True):
        du_dpc = np.array([[fx / z, 0, -fx * x / z_2], [0, fy / z, -fy * y / z_2]])

        return u, du_dpc
    else:
        return u