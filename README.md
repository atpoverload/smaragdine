# Smaragdine

`Smaragdine` is a universal accounting system designed for Intel server systems that support NVIDIA graphics cards. Below is our paper abstract about this work:

```
With the rapid growth of Artificial Intelligence (AI) applications supported by deep learning (DL), the energy efficiency of these applications has an increasingly large impact on sustainability. We introduce Smaragdine, a new energy accounting system for tensor-based DL programs implemented with TensorFlow. At the heart of Smaragdine is a novel white-box methodology of energy accounting: Smaragdine is aware of the internal structure of the DL program, which we call tensor-aware energy accounting. With Smaragdine, the energy consumption of a DL program can be broken down into units aligned with its logical hierarchical decomposition structure. We apply Smaragdine for understanding the energy behavior of BERT, one of the most widely used language models. Layer-by-layer and tensor-by-tensor, Smaragdine is capable of identifying the highest energy/power-consuming components of BERT. Furthermore, we conduct two case studies on how Smaragdine supports downstream toolchain building, one on the comparative energy impact of hyperparameter tuning of BERT, the other on the energy behavior evolution when BERT evolves to its next generation, ALBERT.
```

## Experiment reproduction

Our experiments can be reproduced either through a Docker image or directly through this artifact.

**NOTE**: The data reported in the paper was produced through an evaluation with the system described below. As energy consumption varies from system to system, e.g., the number of cores, the OS schedulers, the python runtime behavior, etc., a reproduction on a different system may not produce identical results as we reported in the paper. Specifically, `smaragdine` requires the use of [RAPL](https://en.wikipedia.org/wiki/Perf_(Linux)#RAPL), which only works on Intel cpus, and can also work with NVIDIA graphic cards if the [NVML]() is setup. `RAPL` can be enabled by running `modprobe msr`.

  > - Single socket Intel Xeon Gold E5-2630 v4 2.20 GHz (20 cores)
  > - Quadro P5000 NVIDIA Gpu
  > - Hyper threading enabled
  > - 64 GB DDR4 RAM
  > - Debian 11
  > - Debian default `powersave` governor
  > - Python version 3.8

### Build with Docker

To re-run the experiment with Docker, you directly run the hosted image or build the provided one:

```bash
docker run --privileged --cap-add=ALL -it -v /dev:/dev -v /lib/modules:/lib/modules smaragdine/smaragdine:latest
```

```bash
docker build -t smaragdine-icse24 .
docker run --privileged --cap-add=ALL -it -v /dev:/dev -v /lib/modules:/lib/modules smaragdine/smaragdine:latest
```

### Build from source

`Smaragdine` can also be rebuilt from scratch. The server-side code is implemented in `rust`:

```bash
cargo build --release
```

The python-side client used in the experiments can be installed as a wheel:

```bash
pip install . -r requirements.txt
```

This process is automated and smoke-tested through `bash setup.sh`. Simple `rust` and `python` clients are also provided for direct testing or integration into user-code.

### Running the experiments

First, you will need to deploy the `Smaragdine` server. This can be done either as separate process or in the background with `sudo target/release/smaragdine`. This will run a `grpc` srever that samples the system for energy data. NOTE: You must run this as a privileged process as it talks to the MSR through [`powercap`](). If you successfully built the image or ran the smoke test, you should be able to successfully run the server.

If you want to use a GPU for the experiments, please follow the instructions here to setup TensorFlow's GPU support through `conda`. The experiment scripts are available in `smaragdine/experiments` and can be run with the following once the server works:

```bash
cd smaragdine/experiments/bert
bash bert_experiments.sh
bash variant_experiments.sh
```

```bash
cd smaragdine/experiments/albert
bash albert_experiments.sh
```

Once the raw data is collected, the plots can be produced with:

```bash
python experiments/plotting.py
```

and will be available at `experiments/plots`.
