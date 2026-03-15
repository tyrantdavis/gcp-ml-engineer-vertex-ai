import subprocess


def run_training():

    subprocess.run(["bash", "training/run_training.sh"], check=True)


if __name__ == "__main__":
    run_training()

#  Orchestration entry-point
