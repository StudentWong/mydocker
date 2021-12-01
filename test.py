import logging
import sys
import time
import os

logger = logging.getLogger(__name__)
env1 = os.getenv("environment1")
env2 = os.getenv("environment2")

def main():
    args = sys.argv
    count = 120
    logger.info('env1: ' + env1)
    logger.info('env2: ' + env2)
    if len(args) > 1:
        count = int(args[1])

    logger.info(f'count was {count}')

    idx = 0
    while idx < count:
        logger.info(f'loop at index {idx}.')
        idx += 1
        time.sleep(1)
    logger.info('complete')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger.info('参数列表:', str(sys.argv))
    main()