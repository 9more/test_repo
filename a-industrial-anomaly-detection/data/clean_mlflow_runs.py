import mlflow
from mlflow.tracking import MlflowClient

experiment_name = "regression-model-comparison"

client = MlflowClient()

experiment = client.get_experiment_by_name(experiment_name)

if experiment is None:
    print(f"Experiment not found: {experiment_name}")
else:
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        filter_string="attributes.status = 'FAILED'",
        max_results=1000,
    )

    for run in runs:
        client.delete_run(run.info.run_id)
        print(f"Deleted failed run: {run.info.run_id}")

    print(f"Finished. Deleted {len(runs)} failed runs.")
