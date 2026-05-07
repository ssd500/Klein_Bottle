import numpy as np

from config import KleinBottleParams
from component_geometries import (
    toolpath_points_for_component_0,
    toolpath_points_for_component_1,
    toolpath_points_for_component_2,
    toolpath_points_for_component_3,
    toolpath_points_for_component_4,
    toolpath_points_for_component_5,
    toolpath_points_for_component_6,
    toolpath_points_for_supports,
)
from gcode_instructions import (
    write_gcode,
)

from utility.helpers_viz import visualize

# https://www.desmos.com/3d/4tgew7eitq
def main():

    # Create parameters
    params = KleinBottleParams()
    toolpath_points = []

    print("\nAdding toolpath points for component 0...")
    toolpath_points.extend(toolpath_points_for_component_0(params))
    
    print("\nAdding toolpath points for component 1...")
    toolpath_points.extend(toolpath_points_for_component_1(params))

    print("\nAdding toolpath points for component 2...")
    toolpath_points.extend(toolpath_points_for_component_2(params))

    print("\nAdding toolpath points for component 3...")
    toolpath_points.extend(toolpath_points_for_component_3(params))

    print("\nAdding toolpath points for component 4...")
    toolpath_points.extend(toolpath_points_for_component_4(params))

    print("\nAdding toolpath points for component 5...")
    toolpath_points.extend(toolpath_points_for_component_5(params))

    print("\nAdding toolpath points for component 6...")
    toolpath_points.extend(toolpath_points_for_component_6(params))
    
    print("\nAdding toolpath points for supports...")
    toolpath_points.extend(toolpath_points_for_supports(params))
    
    toolpath = np.asarray(toolpath_points, dtype=float)
    
    # Lex sort them first by z and then by component order
    path = toolpath[np.lexsort((toolpath[:, 3], toolpath[:, 2]))]
    print(path)

    # PyVista helper
    visualize(path[:, :-1])

    print("\nWriting G-code...")
    output_file = f"output/klein_bottle.gcode"
    write_gcode(path, params, output_file)

    print("\nDONE!")

if __name__ == "__main__":
    main()
