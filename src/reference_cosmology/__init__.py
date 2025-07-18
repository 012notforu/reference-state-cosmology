"""
Reference State Cosmology Framework

A comprehensive implementation of cosmological models based on structured 
vacuum reference states, providing mathematical foundations for dark energy,
the Great Attractor, and cosmic web structure.

Key Classes:
    CosmologicalConstants: Physical constants and cosmological parameters
    ReferenceStateField: Fundamental field theory implementation
    DarkEnergyModel: Dark energy from reference state pressure
    GreatAttractorModel: Phase coherence model for large-scale attraction
    CosmicWebModel: Cosmic web structure from phase domains
    ObservationalPredictions: Testable predictions and observables
    ReferenceStateSimulation: Numerical simulation framework
    CosmologyVisualizer: Visualization and plotting tools

Example Usage:
    >>> from reference_cosmology import CosmologicalConstants, DarkEnergyModel
    >>> constants = CosmologicalConstants()
    >>> dark_energy = DarkEnergyModel(constants)
    >>> rho_DE = dark_energy.dark_energy_density(1.0)
    >>> print(f"Dark energy density: {rho_DE:.3e} kg/m³")
"""

__version__ = "0.1.0"
__author__ = "012notforu"
__email__ = "your.email@example.com"

# Import main classes and functions
from .core import (
    CosmologicalConstants,
    ReferenceStateField,
    DarkEnergyModel,
    GreatAttractorModel,
    CosmicWebModel,
    ObservationalPredictions,
    ReferenceStateSimulation,
    CosmologyVisualizer
)

# Define public API
__all__ = [
    "CosmologicalConstants",
    "ReferenceStateField", 
    "DarkEnergyModel",
    "GreatAttractorModel",
    "CosmicWebModel",
    "ObservationalPredictions",
    "ReferenceStateSimulation",
    "CosmologyVisualizer"
]

def get_version():
    """Return the version string."""
    return __version__

def get_info():
    """Return package information."""
    return {
        "name": "reference-state-cosmology",
        "version": __version__,
        "author": __author__,
        "email": __email__,
        "description": "Framework for reference state cosmological models"
    }
