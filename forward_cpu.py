from gsplat.gausplat import *
from gsplat.gau_io import *

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--gs", help="the input 3d gaussians path")
    args = parser.parse_args()

    if args.gs:
        ply_fn = args.gs
        print("Try to load %s ..." % ply_fn)
        gs = load_gs(ply_fn)
    else:
        print("not gaussians file.")
        gs = get_example_gs()

    # Camera info
    tcw = np.array([1.03796196, 0.42017467, 4.67804612])
    Rcw = np.array([[0.89699204,  0.06525223,  0.43720409],
                    [-0.04508268,  0.99739184, -0.05636552],
                    [-0.43974177,  0.03084909,  0.89759429]]).T

    width = int(979)
    height = int(546)

    fx = 581.6273640151177
    fy = 578.140202494143
    cx = width / 2
    cy = height / 2

    #twc represents the translation vector from the world coordinate system to the camera coordinate system
    twc = np.linalg.inv(Rcw) @ (-tcw)

    fig, ax = plt.subplots()
    array = np.zeros(shape=(height, width, 3))
    im = ax.imshow(array)

    pws = gs['pw']

    us, pcs = project(pws, Rcw, tcw, fx, fy, cx, cy)

    depths = pcs[: , 2]