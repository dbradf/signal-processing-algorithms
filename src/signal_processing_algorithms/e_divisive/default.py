"""Default implementations for E-Divisive."""

from signal_processing_algorithms.e_divisive.base import EDivisiveCalculator
from signal_processing_algorithms.e_divisive.calculators import cext_calculator, numpy_calculator
from signal_processing_algorithms.e_divisive.e_divisive import EDivisive
from signal_processing_algorithms.e_divisive.significance_test import (
    QHatPermutationsSignificanceTester,
)


def default_implementation(impl: str) -> EDivisive:
    """
    Create a default implementation of E-Divisive.

    :return: The default implementation.
    """
    if impl == "cext":
        assert cext_calculator.C_EXTENSION_LOADED
        # TODO: Remove mypy exception once implemented: https://github.com/python/mypy/issues/5018
        print("Cext")
        calculator: EDivisiveCalculator = cext_calculator  # type: ignore
    else:
        print("numpy")
        calculator = numpy_calculator  # type: ignore
    tester = QHatPermutationsSignificanceTester(
        calculator=calculator, pvalue=0.05, permutations=100
    )
    return EDivisive(seed=1234, calculator=calculator, significance_tester=tester)
