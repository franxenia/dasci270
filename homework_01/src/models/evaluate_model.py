trn_acc = accuracy_score(y_trn, trn_pred)
trn_prc = precision_score(y_trn, trn_pred)
trn_rec = recall_score(y_trn, trn_pred)

print(f"Training accuracy:  {trn_acc:.2f}")
print(f"Training precision: {trn_prc:.2f}")
print(f"Training recall:    {trn_rec:.2f}")