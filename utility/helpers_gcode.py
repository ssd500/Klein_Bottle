from __future__ import annotations
import math


# ============================================================================
# EXTRUSION CALCULATIONS
# ============================================================================


def extruded_area(width_mm: float, height_mm: float) -> float:
    """
    Calculate cross-sectional area using capsule model.

    (In-class activity from Lec 7)
    """

    return width_mm * height_mm + math.pi * (height_mm / 2) ** 2


def delta_E_for_move(
    L_mm: float,
    width_mm: float,
    height_mm: float,
    filament_d_mm: float,
    flow_mult: float = 1.0,
) -> float:
    """
    Calculate filament extrusion for a move of length L_mm.

    (In-class activity from Lec 7)
    """

    filament_area = math.pi * (filament_d_mm / 2) ** 2
    return extruded_area(width_mm, height_mm) * L_mm / filament_area * flow_mult / 1.0


# ============================================================================
# START AND END GCODE
# ============================================================================

def start_gcode_minimal(nozzle_temp: int = 215, bed_temp: int = 60):
    return [
        "; ===== Parametric Lamp Shade Slicer - Prusa MK4S =====",
        "; Generated with custom lamp shade slicer",
        "; printer_model = Prusa MK4S",
        "; nozzle_diameter = 0.4",
        "; filament_diameter = 1.75",
        "",
        "G21 ; set units to millimeters",
        "G90 ; use absolute coordinates for positioning",
        "M83 ; use relative distances for extrusion",
        "",
        "; Set acceleration limits for Prusa MK4S",
        "M201 X2500 Y2500 Z200 E2500 ; sets maximum accelerations, mm/sec^2",
        "M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm/sec",
        "M204 P1250 R1250 T1250 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2",
        "",
        "; Set temperatures",
        f"M104 S{nozzle_temp} ; set hotend temp",
        f"M140 S{bed_temp} ; set bed temp",
        f"M190 S{bed_temp} ; wait for bed temp",
        "M109 S170 ; wait for hotend temp (partial)",
        "",
        "; Home all axes",
        "G28 ; home all without mesh bed level",
        "",
        "; Heat to printing temperature",
        f"M109 S{nozzle_temp} ; wait for hotend temp",
        "",
        "; Reset extruder",
        "G92 E0 ; reset extruder position",
    ]


def end_gcode_minimal():
    return [
        "",
        "; ===== End of print =====",
        "G92 E0 ; reset extruder",
        "",
        "; Turn off hotend and bed",
        "M104 S0 ; turn off hotend temperature",
        "M140 S0 ; turn off heated bed temperature",
        "",
        "; Disable fan",
        "M107 ; turn off fan",
        "",
        "; Retract and raise Z",
        "G91 ; relative positioning",
        "G1 E-2 F2700 ; retract filament",
        "G1 Z10 F900 ; raise Z",
        "",
        "; Return to absolute positioning",
        "G90 ; absolute positioning",
        "",
        "; Disable motors",
        "M84 ; disable motors",
    ]
