def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    # Write code here
    Y = []
    for row in X:
        Y_row = []
        for i in range(len(W[0])):
            W_col = [r[i] for r in W]
            Y_row.append(sum([j[0] * j[1] for j in zip(row, W_col)]) + b[i])
        Y.append(Y_row)
    return Y