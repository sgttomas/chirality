"""Local configuration adapters."""

from .loop_registry import JsonLoopRegistry, LoopRegistryConfigError

__all__ = ["JsonLoopRegistry", "LoopRegistryConfigError"]
