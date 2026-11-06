"""step — step.

A minimal scaffold. Genesis didn't have enough knowledge about this
topic in its concept network to compose a full knowledge-base module.
"""

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for step."""
    logger.info("step starting")
    print("Hello from step")
    print("step")


if __name__ == "__main__":
    main()
