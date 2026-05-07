from config import PrinterSpecs, KleinBottleParams
import numpy as np


# ============================================================================
# COMPONENT TOOLPATHS
# ============================================================================


def toolpath_points_for_component_0(params: KleinBottleParams) -> np.ndarray:
    """
    Add toolpath points for the last component which is the base of the elliptic hyperboloid aka elliptic ring.
    """
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 0.0
    start = 2 * np.sqrt((params.l - params.k)/(params.l - params.w))
    end = np.sqrt(1 + ((- params.w)/params.d) ** 2)
    for u in np.linspace(0, end - start, 90, endpoint=False):
        for v in np.linspace(0, 2 * np.pi, params.points_per_ellipse):
            exp_factor = start + u
            x = cx + (params.a * exp_factor * np.cos(v)) * params.aspect
            y = cy + (params.b * exp_factor * np.sin(v)) * params.aspect
            z = cz
            points.append([x, y, z, idx])
            idx = idx + 0.0000001
    return points


def toolpath_points_for_component_1(params: KleinBottleParams) -> np.ndarray:
    """
    Add toolpath points for the first component which is the elliptic hyperboloid.
    """
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 1.0
    for u in np.linspace(0, params.w, 350):
        for v in np.linspace(0, 2 * np.pi, params.points_per_ellipse):
            exp_factor = np.sqrt(1 + ((u - params.w)/params.d) ** 2)
            x = cx + (params.a * exp_factor * np.cos(v)) * params.aspect
            y = cy + (params.b * exp_factor * np.sin(v)) * params.aspect
            z = cz + u * params.aspect
            points.append([x, y, z, idx])
    return points

def toolpath_points_for_component_2(params: KleinBottleParams) -> np.ndarray:
    """
    Add toolpath points for the second component which is the elliptic paraboloid.
    """
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 2.0
    for u in np.linspace(0, params.k - params.w, 175):
        for v in np.linspace(0, 2 * np.pi, params.points_per_ellipse):
            exp_factor = np.sqrt(1 - u/(params.l - params.w))
            x = cx + (params.a * exp_factor * np.cos(v)) * params.aspect
            y = cy + (params.b * exp_factor * np.sin(v)) * params.aspect
            z = cz + (u + params.w) * params.aspect
            points.append([x, y, z, idx])
    return points

def toolpath_points_for_component_3(params: KleinBottleParams) -> np.ndarray:
    """
    Add toolpath points for the third component which is the elliptic toroid.
    """
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 3.0
    for u in np.linspace(0, 5 * np.pi / 4, 100):
        for v in np.linspace(0, 2 * np.pi, params.points_per_ellipse):
            scale_factor = np.sqrt((params.l - params.k)/(params.l - params.w))
            xz_radius = params.c + params.a * scale_factor * np.cos(v)
            x = cx + ((xz_radius) * np.cos(u) - params.c) * params.aspect
            y = cy + (params.b * scale_factor * np.sin(v)) * params.aspect
            z = cz + ((xz_radius) * np.sin(u) + params.k) * params.aspect
            points.append([x, y, round(z, 3), idx])
    return points

def toolpath_points_for_component_4(params: KleinBottleParams) -> np.ndarray:
    """
    Add toolpath points for the fourth component which is the elliptic cylinder.
    """
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 4.0
    for u in np.linspace(0, 2 * params.c, 50):
        for v in np.linspace(0, 2 * np.pi, params.points_per_ellipse):
            scale_factor = np.sqrt((params.l - params.k)/(params.l - params.w))
            a0 = params.a * scale_factor
            b0 = params.b * scale_factor
            x0 = params.c + (params.c - params.k) / np.sqrt(2)
            z0 = - (params.c + params.k) / np.sqrt(2)
            x_old = x0 + a0 * np.cos(v)
            z_old = z0 + u
            x_new = cx + (x_old * np.cos(5 * np.pi / 4) - z_old * np.sin(5 * np.pi / 4)) * params.aspect
            y = cy + (b0 * np.sin(v)) * params.aspect
            z_new = cz + (x_old * np.sin(5 * np.pi / 4) + z_old * np.cos(5 * np.pi / 4)) * params.aspect
            points.append([x_new, y, round(z_new, 3), idx])
    return points

def toolpath_points_for_component_5(params: KleinBottleParams) -> np.ndarray:
    """
    Add toolpath points for the fifth component which is the elliptic toroid.
    """
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 5.0
    for u in np.linspace(0, np.pi/4, 25):
        for v in np.linspace(0, 2 * np.pi, params.points_per_ellipse):
            scale_factor = np.sqrt((params.l - params.k)/(params.l - params.w))
            xz_radius = params.c - params.a * scale_factor * np.cos(v)
            x = cx + ((xz_radius) * np.cos(u) - params.c) * params.aspect
            y = cy + (params.b * scale_factor * np.sin(v)) * params.aspect
            z = cz + ((xz_radius) * np.sin(u) + params.k - 2 * np.sqrt(2) * params.c) * params.aspect
            points.append([x, y, round(z, 3), idx])
    return points

def toolpath_points_for_component_6(params: KleinBottleParams) -> np.ndarray:
    """
    Add toolpath points for the sixth component which is the elliptic cone.
    """
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 6.0
    limit = params.k - 2 * np.sqrt(2) * params.c
    for u in np.linspace(0, limit, 200, endpoint=False):
        for v in np.linspace(0, 2 * np.pi, params.points_per_ellipse):
            scale_factor = np.sqrt((params.l - params.k)/(params.l - params.w))
            exp_factor = 2 - u/limit
            x = cx + (exp_factor * params.a * scale_factor * np.cos(v)) * params.aspect
            y = cy + (exp_factor * params.b * scale_factor * np.sin(v)) * params.aspect
            z = cz + u * params.aspect
            points.append([x, y, z, idx])
    return points

def toolpath_points_for_supports(params: KleinBottleParams) -> np.ndarray:
    cx, cy, cz = PrinterSpecs.BED_CENTER
    points = []
    idx = 10.0
    y_min = - params.b * np.sqrt((params.l - params.k)/(params.l - params.w))
    y_max = + params.b * np.sqrt((params.l - params.k)/(params.l - params.w))
    start = -params.a*np.sqrt(1 + ((- params.w)/params.d) ** 2)
    end = -params.c - params.a * np.sqrt((params.l - params.k)/(params.l - params.w)) - params.c
    for u in np.linspace(start, end, 20, endpoint=False):
        for i in np.linspace(0, 0.1, 10):
            for j in np.linspace(y_min, y_max, 10):
                for h in np.linspace(0, -2*u, 100):
                    x = cx + (u * (1 + i)) * params.aspect
                    y = cy + (j) * params.aspect
                    z = cz + (h) * params.aspect
                    points.append([x, y, z, idx])
    return points
        
