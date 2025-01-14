X_trn, X_tst, y_trn, y_tst = train_test_split(
    X,
    y,
    test_size=tst_size,
    random_state=seed
)