import logging
import json
import os
import os.path as osp
import torch
import torch.backends.cudnn
import random
import numpy as np
from collections import namedtuple
from typing import Optional


def print_namedtuple(
    t: namedtuple,
    logger: logging.Logger,
    level: str="debug"):
    """
    Pretty logging for namedtuple
    """
    if level == "debug":
        logger.debug("\033[35m{}\033[0m: {}".format(
            t.__class__.__name__, json.dumps(t._asdict(), indent=2)))
    elif level == "info":
        logger.info("\033[35m{}\033[0m: {}".format(
            t.__class__.__name__, json.dumps(t._asdict(), indent=2)))
    else:
        raise ValueError("level must be debug or info")


def setup_random_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = False


def setup_logger(logger: logging.Logger, debug_mode: bool, log_file: Optional[str]):
    """
    Setup logger format
    """
    if debug_mode:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logger.setLevel(level)
    formatter = logging.Formatter(
        "--------%(asctime)s-%(name)s[line:%(lineno)d]-%(levelname)s--------\n%(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)
    if log_file is not None:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)


def print_args(args, logger: logging.Logger):
    """
    Print arguments
    """
    logger.info("--------Args--------")
    for arg in vars(args):
        logger.info("{}: {}".format(arg, getattr(args, arg)))
    logger.info("--------------------")
