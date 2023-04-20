# HDL21 site pdk setup  
from pathlib import Path
import sky130

sky130_pdk_root = Path("/foss/pdks/sky130A/libs.tech/ngspice")
sky130.install = sky130.Install(model_lib=sky130_pdk_root / "sky130.lib.spice")
