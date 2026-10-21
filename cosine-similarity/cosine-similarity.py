import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    ret = float((a @ b)/ (np.sqrt(a @ a) * np.sqrt(b @ b)))
    return float(0) if np.isnan(ret) else ret