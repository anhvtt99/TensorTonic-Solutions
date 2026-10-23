def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    # Write code here
    Y = []
    n = len(X)
    d_in = len(W[0])
    for X_row in X:
        Y_row = []
        for i in range(d_in):
            W_col = [W_row[i] for W_row in W]
            Y_row.append(sum([j[0] * j[1] for j in zip(X_row, W_col)]) + b[i])
        Y.append(Y_row)
    return Y