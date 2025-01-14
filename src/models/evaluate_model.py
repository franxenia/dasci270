trn_acc = accuracy_score(y_trn, trn_pred)
trn_prc = precision_score(y_trn, trn_pred)
trn_rec = recall_score(y_trn, trn_pred)

tst_acc = accuracy_score(y_tst, tst_pred)
tst_prc = precision_score(y_tst, tst_pred)
tst_rec = recall_score(y_tst, tst_pred)

print(f"Training accuracy:  {trn_acc:.2f}")
print(f"Training precision: {trn_prc:.2f}")
print(f"Training recall:    {trn_rec:.2f}")

print(f"Test accuracy:      {tst_acc:.2f}")
print(f"Test precision:     {tst_prc:.2f}")
print(f"Test recall:        {tst_rec:.2f}")