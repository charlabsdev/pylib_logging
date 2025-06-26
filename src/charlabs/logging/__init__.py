from charlabs.logging import structlog
from charlabs.logging.default import LogsSettings, TaskLogger, setup_logs

__version__ = "0.1.8"

__all__ = [
    "structlog",
    "LogsSettings",
    "setup_logs",
    "TaskLogger",
    "__version__",
]
