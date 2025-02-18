import sys

from lib import Utils
from lib.logger import Log4j

if __name__ == '__main__':

    spark = Utils.get_spark_session('LOCAL')
    logger = Log4j(spark)

    logger.info("Finished creating Spark Session")
