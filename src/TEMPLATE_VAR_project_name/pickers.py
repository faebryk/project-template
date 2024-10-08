# This file is part of the faebryk project
# SPDX-License-Identifier: MIT

import logging

import faebryk.library._F as F
from faebryk.core.module import Module
from faebryk.libs.picker.lcsc import LCSC_Part
from faebryk.libs.picker.picker import PickerOption, pick_module_by_params

logger = logging.getLogger(__name__)

"""
This file is for picking actual electronic components for your design.
You can make use of faebryk's picker & parameter system to do this.
"""

# part pickers --------------------------------------------


# Example
def pick_resistor(resistor: F.Resistor):
    pick_module_by_params(
        resistor,
        [
            PickerOption(
                part=LCSC_Part(partno="C25076"),
                params={"resistance": F.Constant(100)},
            ),
        ],
    )


# Example
def pick_led(module: F.LED):
    pick_module_by_params(
        module,
        [
            PickerOption(
                part=LCSC_Part(partno="C2286"),
                params={
                    "color": F.Constant(F.LED.Color.GREEN),
                    "max_brightness": F.Constant(285e-3),
                    "forward_voltage": F.Constant(3.7),
                    "max_current": F.Constant(100e-3),
                },
                pinmap={"1": module.cathode, "2": module.anode},
            ),
            PickerOption(
                part=LCSC_Part(partno="C72041"),
                params={
                    "color": F.Constant(F.LED.Color.BLUE),
                    "max_brightness": F.Constant(28.5e-3),
                    "forward_voltage": F.Constant(3.1),
                    "max_current": F.Constant(100e-3),
                },
                pinmap={"1": module.cathode, "2": module.anode},
            ),
        ],
    )


# ----------------------------------------------------------


def add_app_pickers(module: Module):
    lookup = {
        F.Resistor: pick_resistor,
        F.LED: pick_led,
    }

    F.has_multi_picker.add_pickers_by_type(
        module,
        lookup,
        F.has_multi_picker.FunctionPicker,
    )
