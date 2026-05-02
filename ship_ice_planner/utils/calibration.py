import pickle
from multiprocessing import Queue
from typing import List

import numpy as np

from ship_ice_planner.launch import launch
from ship_ice_planner.utils.utils import DotDict


def get_calibration_data_for_collision_cost_weight(
        cfg_file, exp_data, calibration_dump_file='calibration_data_alpha.pkl'
):

    cfg = DotDict.load_from_file(cfg_file)
    cfg.costmap.collision_cost_weight = 1
    cfg.costmap.ice_resistance_weight = 1
    cfg.a_star.weight = 0
    cfg.max_replan = 1
    cfg.horizon = 0
    cfg.planner = 'lattice'
    cfg.plot.show = False  # set to True to see the expanded nodes which generate a nice looking lattice
    cfg.save_paths = True
    cfg.optim = False
    cfg.prim.prim_name = 'PRIM_GO_STRAIGHT'

    swaths = []

    for ice_concentration in [0.2, 0.3, 0.4, 0.5]:
        for ice_field_idx in range(100):
            obstacles = exp_data[ice_concentration][ice_field_idx]['obstacles']
            queue = Queue()
            queue.put(dict(
                goal=[100, 1100],
                ship_state=(100, 0, np.pi / 2),
                obstacles=[ob['vertices'] for ob in obstacles],
                masses=[ob['mass'] for ob in obstacles]

            ))
            cfg.output_dir = None
            results = launch(cfg=cfg, debug=False, logging=True, queue=queue)

            swaths.append({
                'concentration': ice_concentration,
                'ice_field_idx': ice_field_idx,
                'swath_cost': results[0]['swath_cost'],
                'path_length': results[0]['path_length']
            })

    pickle.dump(swaths, open(calibration_dump_file, 'wb'))


def calibrate_collision_cost_weight(control_effort: List,
                                    ship_ke_loss: List,
                                    swath_cost: List,
                                    path_length: List,
                                    scale: float
                                    ) -> float:
    """
    :param control_effort: total control effort or energy use (J) in each trial
    :param ship_ke_loss: total ship kinetic energy loss (J) from collision with ice in each trial
    :param swath_cost: swath cost values in each trial
    :param path_length: path length (m) values in each trial
    :param scale: the scaling factor for the costmap, divide by scale to get world units i.e. meters
    """
    assert len(control_effort) == len(ship_ke_loss) == len(swath_cost) == len(path_length)
    weight_list = []

    for idx in range(len(control_effort)):
        ratio = ship_ke_loss[idx] / control_effort[idx]
        # ratio < 1 since cannot have a larger amount of kinetic energy loss than the total energy put in,
        # if the ratio is greater than 1 than it should not be part of the calibration trials
        assert ratio < 1

        weight_list.append(
            (ratio * path_length[idx] * scale) / (swath_cost[idx] - ratio * swath_cost[idx])
        )

    return np.mean(weight_list)
