import pickle

with open("data/reference_db/features.pkl", "rb") as f:
    db = pickle.load(f)

print("Indexed Pills:")
for k in db.keys():
    print("-", k)
