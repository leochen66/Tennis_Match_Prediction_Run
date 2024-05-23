import runhouse as rh

from data_pull import data_pull
from data_preprocess import data_preprocessing, data_split
from model_train import train, evaluation


packages = [
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "opendatasets",
    "boto3",
    "watchtower",
]

if __name__ == "__main__":

    env = rh.env(name="tennis_env", env_vars=cert, reqs=packages)

    cluster = rh.ondemand_cluster(
        name="tennis-prediction-cluster",
        instance_type="CPU:2+",
        provider="aws",
        default_env=env
    ).up_if_not()

    remote_data_pull_fn = rh.function(data_pull).to(cluster)
    remote_data_preprocess_fn = rh.function(data_preprocessing).to(cluster)
    remote_data_split_fn = rh.function(data_split).to(cluster)
    remote_train_fn = rh.function(train).to(cluster)
    remote_evaluation_fn = rh.function(evaluation).to(cluster)

    cluster.save()
    remote_data_pull_fn.save()
    remote_data_preprocess_fn.save()
    remote_data_split_fn.save()
    remote_train_fn.save()
    remote_evaluation_fn.save()