import os
import sys


def init():
    if "DATALAB_ROOT" not in os.environ:
        if "PROJECT_ID" in os.environ:
            os.environ["DATALAB_ROOT"] = '/content/datalab/'

        else:
            print("INFO: Using local envs")
            cur_dir = os.path.abspath(__file__)
            sys.path.append("/".join(cur_dir.split("/")[:-3]))
            os.environ["DATALAB_ROOT"] = "/".join(cur_dir.split("/")[:-3]) + "/"

    if "AIRCRAFT_DATA" not in os.environ:
        os.environ["AIRCRAFT_DATA"] = os.environ.get("DATALAB_ROOT") + 'data/fgvc-aircraft-2013b/data'

    print("Home path: {}".format(os.environ["DATALAB_ROOT"]))
    print("Aircraft data path: {}".format(os.environ["AIRCRAFT_DATA"]))

