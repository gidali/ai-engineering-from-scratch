from datasets import load_dataset

ds = load_dataset("cornell-movie-review-data/rotten_tomatoes", split="train")

split1 = ds.train_test_split(test_size=0.30, seed=42)
train_ds = split1["train"]

split2 = split1["test"].train_test_split(test_size=0.50, seed=42)
val_ds = split2["train"]
test_ds = split2["test"]

total = len(train_ds) + len(val_ds) + len(test_ds)
print(f"Total: {total}")
print(f"Train: {len(train_ds)} ({len(train_ds)/total:.1%})")
print(f"Val:   {len(val_ds)} ({len(val_ds)/total:.1%})")
print(f"Test:  {len(test_ds)} ({len(test_ds)/total:.1%})")
