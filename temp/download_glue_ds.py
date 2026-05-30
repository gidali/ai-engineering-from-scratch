from datasets import load_dataset

ds = load_dataset("nyu-mll/glue", "mrpc", split="train")
print(ds)
for i in range(1):
    print(ds[i])
