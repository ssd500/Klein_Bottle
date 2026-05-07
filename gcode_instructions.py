"""
G-Code Generation
"""

import numpy as np
import time
from typing import Dict
from pathlib import Path

from config import PrinterSpecs, KleinBottleParams
from utility.helpers_gcode import delta_E_for_move, start_gcode_minimal, end_gcode_minimal


# ============================================================================
# G-CODE WRITING
# ============================================================================


def write_gcode(
    path: np.ndarray, params: KleinBottleParams, output_file: str
) -> Dict:
    """
    Write complete G-code file for spiral lamp shade printing.
    """

    start_time = time.time()
    gcode_lines = []

    # Header (includes all Prusa MK4S validation requirements)
    gcode_lines.extend(start_gcode_minimal(params.nozzle_temp, params.bed_temp))
    gcode_lines.append("")
    gcode_lines.append("; ===== KLEIN BOTTLE TOOLPATH =====")
    gcode_lines.append(f"; Total points: {len(path)}")
    gcode_lines.append("")

    # Travel to first point (no extrusion)
    x0, y0, z0, idx0 = path[0]
    gcode_lines.append(f"G1 Z{z0:.3f} F900 ; move to start Z")
    gcode_lines.append(
        f"G1 X{x0:.3f} Y{y0:.3f} F{params.travel_speed:.0f} ; travel to start"
    )
    gcode_lines.append("")
    gcode_lines.append("; Begin printing")

    prev_point = None
    total_distance = 0.0
    special = {5.0: 8.0, 4.0: 10.0, 3.0: 10.0}

    for x, y, z, idx in path:
        if prev_point is not None:
            z = max(z, prev_point[2])  # Ensure Z never decreases
            dx = x - prev_point[0]
            dy = y - prev_point[1]
            dz = z - prev_point[2]
            distance = np.linalg.norm([dx, dy, dz])
            total_distance += distance
            dE = 0.0 if np.ceil(idx) != np.ceil(prev_point[3]) or (idx in special.keys() and distance > special[idx]) else delta_E_for_move(distance, params.line_width, params.layer_height, PrinterSpecs.FILAMENT_DIAMETER, params.flow_multiplier)
            gcode_lines.append(f"G1 X{x:.3f} Y{y:.3f} Z{z:.3f} E{dE:.5f} F{params.print_speed:.0f} ; print point")
        prev_point = (x, y, z, idx)

    # Footer
    gcode_lines.append("")
    gcode_lines.append("; ===== END =====")
    gcode_lines.extend(end_gcode_minimal())

    # Write file
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(gcode_lines) + "\n"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    # Calculate statistics
    generation_time = time.time() - start_time
    file_size = len(content.encode("utf-8"))

    print(f"  Wrote G-code to: {output_file}")
    print(f"  Generation time: {generation_time:.2f}s")
    print(f"  File size: {file_size/1024:.1f} KB")
    print(f"  Total distance: {total_distance/1000:.2f} m")
