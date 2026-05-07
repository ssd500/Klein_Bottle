class PrinterSpecs:
    """Prusa MK4S printer specifications"""

    BED_CENTER = (125, 105, 0.2)  # mm (X, Y) since bed size is (250, 210)
    FILAMENT_DIAMETER = 1.75  # mm


class KleinBottleParams:
    """Parameters for Klein Bottle generation and printing"""

    def __init__(self):
        # Geometry parameters
        self.a: float = 2.0
        self.b: float = 3.0
        self.c: float = 6.0
        self.d: float = 4.0
        self.k: float = 27.0
        self.l: float = 30.0
        self.w: float = 18.0
        self.aspect: float = 3 # Only this should be changed for different sizes
        self.points_per_ellipse: int = 60

        # Printing parameters
        self.layer_height: float = 0.20  # mm
        self.line_width: float = 0.48  # mm (slightly wider than nozzle)
        self.print_speed: float = 1500.0  # mm/min
        self.travel_speed: float = 6000.0  # mm/min
        self.flow_multiplier: float = 1.0  # extrusion multiplier

        # Temperature settings (PLA)
        self.nozzle_temp: int = 215  # Celcius
        self.bed_temp: int = 60  # Celcius
