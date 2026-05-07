import pyvista as pv
import numpy as np

# ============================================================================
# VISUALIZE HELPER USING PYVISTA
# ============================================================================


def visualize(points: np.ndarray, point_size: float = 5.0):
    # Create a PyVista PolyData object
    cloud = pv.PolyData(points)

    # Create a plotter
    plotter = pv.Plotter()
    plotter.add_mesh(cloud, color="cyan", point_size=point_size, render_points_as_spheres=True)
    plotter.show_grid()
    plotter.show()
