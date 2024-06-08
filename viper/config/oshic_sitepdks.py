# HDL21 site pdk setup  
from pathlib import Path
import sky130

sky130_pdk_root = Path("/foss/pdks/sky130A")
sky130.install = sky130.Install(
    # pdk_path=Path(os.environ["PDK_ROOT"] + "/" + os.environ["PDK"]),
    pdk_path=sky130_pdk_root,
    lib_path=Path("libs.tech/ngspice/sky130.lib.spice"),
    model_ref=Path("libs.ref/sky130_fd_pr/spice"),
)
