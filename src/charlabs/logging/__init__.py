from charlabs.logging import structlog
from charlabs.logging.default import LogsSettings, TaskLogger, setup_logs

try:
    from importlib.metadata import version

    __version__ = version("charlabs-logging")
except ImportError:
    # Fallback version for development installs
    __version__ = "0.0.0+dev"

__all__ = [
    "structlog",
    "LogsSettings",
    "setup_logs",
    "TaskLogger",
    "__version__",
]
