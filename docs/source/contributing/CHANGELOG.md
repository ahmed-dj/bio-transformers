# Change log

# [0.0.9] - 2021-06-14
Note on the release

Features:
 - Add BIO_LOG_LEVEL environnement variable to control logging message

Fixed:
 - Add shuffling in batch_sampler
 - Fix tokens argument

Changed:


# [0.0.8] - 2021-06-03
Note on the release

Features:
 - Merge ESM/protbert for finetuning model with pytorch-lightning
 - Possibility to restore a training session.

Fixed:
 - Fix conflicts when saving model with DDP
 - Fix loading checkpoint created by pytorch-lightning


# [0.0.7] - 2021-05-12
Note on the release

Features:
 - Add fasta files support for each compute function.
 - Add train_masked function to finetune model on custom dataset. (Only ESM for the moment, protbert is coming.)

Docs:
 - Update documentation to add tutorial on training.

Changed:
 - GPU is used by default if found, even if not specified.

# [0.0.6] - 2021-05-24
Note on the release

Fixed:
 - Update torch dependencies to be less restrictive. Create conflict with other packages.

# [0.0.5] - 2021-05-12

Note on the release

Added
 - added multi-gpu support for inference
 - added function to finetuned a model on a specific dataset on multi-gpu

Changed

Fixed