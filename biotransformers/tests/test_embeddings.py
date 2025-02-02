"""Test module for testing embeddings function"""
import numpy as np
import pytest

test_sequences = ["AAAA", "AKKF", "AHHFK", "KKKKKKKLLL"]
test_fasta = "data/fasta/example_fasta.fasta"
length_fasta = [538, 508, 393, 328, 354, 223]

test_params = [
    (1, ["cls", "mean"]),
    (2, ["full", "mean", "cls"]),
    (10, ["cls", "full"]),
]


@pytest.mark.parametrize("batch_size, pool_mode", test_params)
def test_embeddings_type_and_shape(init_model, batch_size, pool_mode):
    test_trans = init_model
    embeddings = test_trans.compute_embeddings(
        test_sequences,
        batch_size=batch_size,
        pool_mode=pool_mode,
    )

    assert isinstance(embeddings, dict)
    if "full" in pool_mode:
        for emb, sequence in zip(embeddings["full"], test_sequences):
            assert emb.shape[0] == len(sequence)
    if "cls" in pool_mode:
        assert isinstance(embeddings["cls"], np.ndarray)

    if "mean" in pool_mode:
        assert isinstance(embeddings["mean"], np.ndarray)


@pytest.mark.parametrize("batch_size, pool_mode", test_params)
def test_embeddings_type_and_shape_fasta(init_model, batch_size, pool_mode):
    test_trans = init_model
    embeddings = test_trans.compute_embeddings(
        test_fasta,
        batch_size=batch_size,
        pool_mode=pool_mode,
    )
    if "full" in pool_mode:
        for emb, length in zip(embeddings["full"], length_fasta):
            assert emb.shape[0] == length

    assert isinstance(embeddings, dict)
    if "cls" in pool_mode:
        assert isinstance(embeddings["cls"], np.ndarray)

    if "mean" in pool_mode:
        assert isinstance(embeddings["mean"], np.ndarray)
