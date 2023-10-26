"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = adversarial_misspell.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys
import random
from homoglyph import homoglyph
from leetspeak import leetspeak

from adversarial_misspell import __version__

__author__ = "Kevin Coleman"
__copyright__ = "Kevin Coleman"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from adversarial_misspell.skeleton import fib`,
# when using this Python module as a library.


def all(input, K=1, N=1):
    """user all modifiers

    Args:
      N (int): integer - Number of words
      K (int): integer - Max modifications per word

    Returns:
      list[string]: array of mispelled words
    """
    assert N >= 0
    assert K >= 0

    inputs = [(list(input), set()) for _ in range(N)]
    for i in range(len(inputs)):
        for _ in range(K):
            modifier_function = random.randint(0, 1)
            if modifier_function == 1:
                inputs[i] = leetspeak.leetspeak(inputs[i][0], seen=inputs[i][1])
            elif modifier_function == 0:
                inputs[i] = homoglyph.homoglyph(inputs[i][0], seen=inputs[i][1])
    res = []
    for modified_input in inputs:
        res.append(''.join(modified_input[0]))

    return res

def refresh():
    """refreshes mappings

    Returns:
      bool: True for success, false otherwise.
    """

    return homoglyph.refresh()

# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Generate Adversial Misspellings")
    parser.add_argument(
        "--version",
        action="version",
        version=f"adversarial_misspell {__version__}",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )

    parser.add_argument("function", 
                    nargs="?",
                    choices=['all', 'refresh'],
                    default='refresh',
                    )
    args, sub_args = parser.parse_known_args()

    if args.function == "all":
        parser = argparse.ArgumentParser()
        parser.add_argument(dest="input", help="input string", type=str, metavar="STR")
        parser.add_argument(dest="N", help="Number of mutations to generate", type=int, metavar="INT")
        parser.add_argument(dest="K", help="Max Number of mutations per generation", type=int, metavar="INT")
   
        sub_args = parser.parse_args(sub_args)
        return args, sub_args
    elif args.function == "refresh":
        return args
    return args, sub_args


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args, subargs = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")

    if args.function == "refresh":
        print(refresh())
    elif args.function == "all":
        print(all(subargs.input, K=subargs.K, N=subargs.N))
    _logger.info("Script ends here")

def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m adversarial_misspell.skeleton 42
    #
    run()
