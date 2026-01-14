"""Smoke test for re-entrant runs."""

import math
import sys
import types

import hvy_global_bcon_data as bcon
import hvy_global_mat_data as mat
import hvy_global_mesh_data as mesh
import hvy_global_reg_data as reg
import hvy_global_time_data as time
import harvey


def _register_input_module(name, material_name, region_name):
    module = types.ModuleType(name)

    def define():
        mesh.geom = 0
        mesh.theta = 0.0
        mesh.xsize = 1.0
        mesh.dx = 0.1
        mesh.ncells = int(mesh.xsize / mesh.dx)
        mesh.xmin = 0.0

        dcon = 1.0
        time.dt = (mesh.dx * mesh.dx) / (6.0 * dcon)
        time.end = 0.01

        bcon.inner = {"type": "dirichlet", "value": 0.0}
        bcon.outer = {"type": "dirichlet", "value": 0.0}
        bcon.icon = {"type": "sin", "value": math.pi / mesh.xsize}

        mat.material(material_name, dcon)
        reg.region(region_name, material_name, mesh.xsize)

    module.define = define
    sys.modules[name] = module


def _assert_state(material_name, region_name):
    if set(mat.materials.keys()) != {material_name}:
        raise AssertionError("materials not reset between runs")
    if set(reg.regions.keys()) != {region_name}:
        raise AssertionError("regions not reset between runs")


def test_reset():
    _register_input_module("reset_input_a", "MatA", "RegA")
    _register_input_module("reset_input_b", "MatB", "RegB")

    harvey.main("reset_input_a", "reset_a.out", False)
    _assert_state("MatA", "RegA")

    harvey.main("reset_input_b", "reset_b.out", False)
    _assert_state("MatB", "RegB")

    return True
