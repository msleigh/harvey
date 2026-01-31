"""User input functions."""

## @brief Process command-line arguments
##
## Process the command-line arguments

import importlib.util
import re
import sys
from pathlib import Path

import hvy_global_mesh_data as mesh
import hvy_global_mat_data as mat
import hvy_global_reg_data as reg
import hvy_global_time_data as time
import hvy_global_bcon_data as bcon


def _load_user_input(input_file):
    if not isinstance(input_file, str):
        print("    Error: input file name must be a string")
        sys.exit(1)

    raw_input = Path(input_file)
    input_name = raw_input.stem if raw_input.suffix == ".py" else input_file

    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", input_name):
        print(
            "    Error: input file name must be a valid module identifier (letters, "
            "numbers, underscores)"
        )
        sys.exit(1)

    existing_module = sys.modules.get(input_name)
    if existing_module is not None and getattr(existing_module, "__file__", None) is None:
        return existing_module

    repo_root = Path(__file__).resolve().parents[1]
    src_root = Path(__file__).resolve().parent
    allowed_roots = {Path.cwd().resolve(), src_root.resolve(), repo_root.resolve()}

    def _is_within_root(path, root):
        try:
            path.resolve().relative_to(root)
            return True
        except ValueError:
            return False

    search_paths = [Path.cwd(), src_root]
    for path_entry in sys.path:
        if not path_entry:
            continue
        candidate = Path(path_entry)
        if candidate.exists() and _is_within_root(candidate.resolve(), repo_root):
            search_paths.append(candidate)

    module_path = None
    if raw_input.suffix == ".py" or raw_input.parent != Path("."):
        candidate_path = raw_input
        if not candidate_path.is_absolute():
            candidate_path = (Path.cwd() / candidate_path).resolve()
        if not candidate_path.is_file():
            print("    Error: input file path does not exist")
            sys.exit(1)
        if not any(_is_within_root(candidate_path, root) for root in allowed_roots):
            print("    Error: input file must be within the project directory")
            sys.exit(1)
        module_path = candidate_path
    else:
        for candidate in search_paths:
            candidate_path = candidate / f"{input_name}.py"
            if candidate_path.is_file():
                module_path = candidate_path
                break
        if module_path is None:
            print(
                "    Error: input file not found in project search paths"
            )
            sys.exit(1)
    spec = importlib.util.spec_from_file_location(input_name, module_path)
    if spec is None or spec.loader is None:
        print("    Error: unable to load input module")
        sys.exit(1)

    module = importlib.util.module_from_spec(spec)
    sys.modules[input_name] = module
    spec.loader.exec_module(module)
    return module


def read(input_file):
    """
    @brief   Reads input deck (by importing).

    @details Reads input deck with user-specified problem-specific
             information.
    @param   None
    @return  None
    """
    # There is no default input file name (initialised to None in import)
    print()
    print("Processing user input file...")
    if input_file is None:
        print("    Error: no input file specified")
        sys.exit()

    bcon.reset()
    mesh.reset()
    mat.reset()
    reg.reset()
    time.reset()

    print(f"    Specified input file name = {input_file}")
    print("    Importing...")
    harvin = _load_user_input(input_file)
    print("    Running...")
    if not hasattr(harvin, "define") or not callable(harvin.define):
        print("    Error: input module must define a callable define() function")
        sys.exit(1)
    harvin.define()


def echo():
    """Echo user input back out."""
    print()
    print("Echoing user input...")

    print(f"    mesh.geom      {mesh.geom}")
    print(f"    mesh.theta     {mesh.theta}")
    print(f"    mesh.ncells    {mesh.ncells}")
    print(f"    mesh.xmin      {mesh.xmin}")
    print(f"    mesh.xsize     {mesh.xsize}")
    print(f"    mesh.dx        {mesh.dx}")

    print(f"    time.dt        {time.dt}")
    print(f"    time.end       {time.end}")

    print(f"    mat.nmats      {mat.nmats}")
    for matname in mat.materials.keys():
        print(f"    mat.name    {matname}")
        print(f"    mat.dcoeff  {mat.materials[matname]['d']}")

    print(f"    reg.nregs      {reg.nregs}")
    for regname in reg.regions.keys():
        print(f"    reg.name   {regname}")
        print(f"    reg.mat    {reg.regions[regname]['mat']}")
        print(f"    reg.xbound {reg.regions[regname]['xbound']}")


def initialize_counts():
    """Initialize material and region counts after input definition."""
    mat.nmats = len(mat.materials)
    reg.nregs = len(reg.regions)
