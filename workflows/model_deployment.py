import os
import typing
import subprocess
import runhouse as rh

from aws_logger import logger
from data_pull import data_pull


def deployment():
    logger.info(f"Model approved, start deployment")

    # deploy by seldon (This is only support on local excution)
    current_dir = os.path.dirname(__file__)
    script_path = os.path.join(current_dir, "..", "seldon_deployment.sh")
    subprocess.run(["sh", script_path])


def discard() -> int:
    logger.info(f"Model not approved, will not trigger deployment")
    return -1


def deployment_check(accuracy:float) -> bool:
    if accuracy > 0.6:
        return True
    else:
        return False


if __name__=="__main__":
    rh_cluster = rh.cluster(name="/leo/tennis-prediction-cluster").up_if_not()

    data_pull_fn = rh.function(name="/leo/data_pull")
    data_preprocess_fn = rh.function(name="/leo/data_preprocessing")
    data_split_fn = rh.function(name="/leo/data_split")
    train_fn = rh.function(name="/leo/train")
    evaluation_fn = rh.function(name="/leo/evaluation")

    data = data_pull()
    x_data, y_data = data_preprocess_fn(data)
    x_train, x_test, y_train, y_test = data_split_fn(x_data, y_data)
    model = train_fn(x_train, y_train)
    accuracy = evaluation_fn(model, x_test, y_test)
    if deployment_check(accuracy):
        deployment()