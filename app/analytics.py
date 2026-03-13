import pandas as pd
import numpy as np


def generate_analytics(rows):

    df = pd.DataFrame(rows, columns=["id", "amount", "category", "date"])

    if df.empty:
        return {"message": "No expenses found"}

    amounts = np.array(df["amount"])

    result = {
        "total_spent": float(np.sum(amounts)),
        "average_expense": float(np.mean(amounts)),
        "max_expense": float(np.max(amounts)),
        "min_expense": float(np.min(amounts)),
        "category_summary": df.groupby("category")["amount"].sum().to_dict()
    }

    return result