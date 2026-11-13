from fractions import Fraction
from itertools import product
import json


def zero_matrix(size):
    return [[0 for column in range(size)] for row in range(size)]


def multiply(left, right):
    size = len(left)
    return [[sum(left[row][inner] * right[inner][column] for inner in range(size))
             for column in range(size)] for row in range(size)]


def bracket(left, right):
    forward = multiply(left, right)
    backward = multiply(right, left)
    return [[forward[row][column] - backward[row][column]
             for column in range(len(left))] for row in range(len(left))]


def rank(rows, columns):
    pivots = {}
    for original in rows:
        vector = list(map(Fraction, original))
        for column in range(columns):
            if not vector[column]:
                continue
            if column in pivots:
                coefficient = vector[column]
                vector = [value - coefficient * pivot
                          for value, pivot in zip(vector, pivots[column])]
            else:
                coefficient = vector[column]
                pivots[column] = [value / coefficient for value in vector]
                break
    return len(pivots)


def determinant(matrix):
    reduced = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for column in range(len(reduced)):
        pivot = next((row for row in range(column, len(reduced))
                      if reduced[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            reduced[pivot], reduced[column] = reduced[column], reduced[pivot]
            result = -result
        scale = reduced[column][column]
        result *= scale
        for row in range(column + 1, len(reduced)):
            coefficient = reduced[row][column] / scale
            reduced[row] = [value - coefficient * upper
                            for value, upper in zip(reduced[row], reduced[column])]
    assert result.denominator == 1
    return int(result)


def derivation_rank(orthogonal_dimension):
    size = orthogonal_dimension + 1
    structure = [[[0 for target in range(size)] for right in range(size)]
                 for left in range(size)]
    for index in range(size):
        structure[index][index][-1] = 1
    equations = []
    for left, right, target in product(range(size), repeat=3):
        equation = [0] * (size * size)
        for inner in range(size):
            equation[target * size + inner] += structure[left][right][inner]
            equation[inner * size + left] -= structure[inner][right][target]
            equation[inner * size + right] -= structure[left][inner][target]
        equations.append(equation)
    actual = size * size - rank(equations, size * size)
    expected = orthogonal_dimension * (orthogonal_dimension - 1) // 2
    assert actual == expected, (orthogonal_dimension, actual, expected)
    for left in range(orthogonal_dimension):
        for right in range(left + 1, orthogonal_dimension):
            candidate = [0] * (size * size)
            candidate[left * size + right] = 1
            candidate[right * size + left] = -1
            assert all(sum(value * coefficient for value, coefficient
                           in zip(candidate, equation)) == 0 for equation in equations)
    return {'m': orthogonal_dimension, 'derivation_dimension': actual}


def killing_matrix():
    basis = []
    off_diagonal = [(row, column) for row in range(3) for column in range(3)
                    if row != column]
    for row, column in off_diagonal:
        matrix = zero_matrix(3)
        matrix[row][column] = 1
        basis.append(matrix)
    basis.extend([[[1, 0, 0], [0, -1, 0], [0, 0, 0]],
                  [[0, 0, 0], [0, 1, 0], [0, 0, -1]]])
    adjoint = []
    for left in basis:
        columns = []
        for right in basis:
            commutator = bracket(left, right)
            assert sum(commutator[index][index] for index in range(3)) == 0
            columns.append([commutator[row][column] for row, column in off_diagonal]
                           + [commutator[0][0], -commutator[2][2]])
        adjoint.append([list(row) for row in zip(*columns)])
    killing = []
    for left_index, left in enumerate(adjoint):
        row = []
        for right_index, right in enumerate(adjoint):
            composition = multiply(left, right)
            value = sum(composition[index][index] for index in range(8))
            expected = 6 * sum(multiply(basis[left_index], basis[right_index])[index][index]
                               for index in range(3))
            assert value == expected
            row.append(value)
        killing.append(row)
    actual = determinant(killing)
    assert actual == -5038848
    return {'dimension': len(basis), 'killing_matrix': killing, 'determinant': actual}


def dimension_obstruction():
    factors = [(size, size * (size - 1) // 2) for size in range(3, 6)]
    small = [(size, dimension) for size, dimension in factors if dimension <= 8]
    assert small == [(3, 3), (4, 6)]
    reachable = {0}
    for total in range(9):
        if total in reachable:
            reachable.update(total + dimension for size, dimension in small
                             if total + dimension <= 8)
    assert sorted(reachable) == [0, 3, 6]
    assert 8 not in reachable
    return {'factor_dimensions_at_most_eight': small,
            'reachable_dimensions_at_most_eight': sorted(reachable)}


def main():
    result = {
        'orthogonal_examples': [derivation_rank(size) for size in range(1, 8)],
        'sl3': killing_matrix(),
        'dimension_obstruction': dimension_obstruction(),
        'scope': 'Exact rational finite checks; the general statements have written proofs in note.tex.',
        'status': 'ALL_CHECKS_OK',
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
