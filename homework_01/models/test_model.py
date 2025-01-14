clf.fit(X_tst, y_tst)

tst_acc = accuracy_score(y_tst, tst_pred)
tst_prc = precision_score(y_tst, tst_pred)
tst_rec = recall_score(y_tst, tst_pred)

print(f"Test accuracy:      {tst_acc:.2f}")
print(f"Test precision:     {tst_prc:.2f}")
print(f"Test recall:        {tst_rec:.2f}")