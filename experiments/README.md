# Smaragdine Experiments

This directory contains the experiments used to produce the data in the `Smaragdine` publication. The instructions to 

# Running the experiments

First, you will need to deploy the `Smaragdine` server. You can follow the instructions in the top-level readme. Then, you should pull down the CoLA dataset used for fine-tuning:

```bash
python setup_glue_data.py --tasks CoLA --data_dir glue_data
```

The experiment scripts available here can be run with the following:

```bash
cd experiments/bert
bash bert_experiments.sh
bash variant_experiments.sh
```

```bash
cd experiments/albert
bash albert_experiments.sh
```

Once the raw data is collected, the plots can be produced with:

```bash
python experiments/plotting.py
```

and will be available at `experiments/plots`.
