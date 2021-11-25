import pandas as pd

df = pd.DataFrame({
    "name": ["Kevin", "Jack", "Mary"],
    "score": [80, 90, 95],
    "class": ["A", "B", "A"],
    "sex": ["M", "M", "F"]
}, index=["K", "J", "M"])

df
