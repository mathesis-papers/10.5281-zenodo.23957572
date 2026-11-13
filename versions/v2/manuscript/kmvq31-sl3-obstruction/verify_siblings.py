from itertools import product
import json

from verify import bracket, multiply, rank, zero_matrix


def derivation_equations(squares):
    size = len(squares)
    equations = []
    for left, right, target in product(range(size), repeat=3):
        equation = [0] * (size * size)
        for inner in range(size):
            if left == right:
                equation[target * size + inner] += squares[left][inner]
            if inner == right:
                equation[inner * size + left] -= squares[right][target]
            if left == inner:
                equation[inner * size + right] -= squares[left][target]
        equations.append(equation)
    return equations


def diagonal_forms():
    results = []
    for dimension in range(1, 7):
        for negative in range(dimension + 1):
            weights = [-1] * negative + [1] * (dimension - negative)
            size = dimension + 1
            squares = [[0] * dimension + [weight] for weight in weights + [1]]
            equations = derivation_equations(squares)
            actual = size * size - rank(equations, size * size)
            expected = dimension * (dimension - 1) // 2
            assert actual == expected
            candidates = []
            for left in range(dimension):
                for right in range(left + 1, dimension):
                    candidate = [0] * (size * size)
                    candidate[left * size + right] = weights[right]
                    candidate[right * size + left] = -weights[left]
                    assert all(sum(value * coefficient for value, coefficient
                                   in zip(candidate, equation)) == 0
                               for equation in equations)
                    candidates.append(candidate)
            assert rank(candidates, size * size) == expected
            results.append({'dimension': dimension, 'negative_squares': negative,
                            'derivation_dimension': actual})
    return results


def zero_product():
    size = 3
    equations = derivation_equations([[0] * size for row in range(size)])
    assert rank(equations, size * size) == 0
    units = []
    for row, column in product(range(size), repeat=2):
        matrix = zero_matrix(size)
        matrix[row][column] = 1
        units.append(matrix)
    commutators = [bracket(left, right) for left, right in product(units, repeat=2)]
    assert all(sum(matrix[index][index] for index in range(size)) == 0
               for matrix in commutators)
    derived_dimension = rank([sum(matrix, []) for matrix in commutators], size * size)
    assert derived_dimension == 8
    return {'algebra_dimension': 3, 'derivation_dimension': 9,
            'commutator_ideal_dimension': derived_dimension}


def split_action():
    size = 6
    gram = zero_matrix(size)
    for index in range(3):
        gram[index][index + 3] = gram[index + 3][index] = 1
    basis = []
    for row, column in product(range(3), repeat=2):
        if row != column:
            matrix = zero_matrix(3)
            matrix[row][column] = 1
            basis.append(matrix)
    basis.extend([[[1, 0, 0], [0, -1, 0], [0, 0, 0]],
                  [[0, 0, 0], [0, 1, 0], [0, 0, -1]]])

    def embedding(matrix):
        result = zero_matrix(size)
        for row, column in product(range(3), repeat=2):
            result[row][column] = matrix[row][column]
            result[row + 3][column + 3] = -matrix[column][row]
        return result

    images = [embedding(matrix) for matrix in basis]
    for matrix in images:
        transposed = [list(row) for row in zip(*matrix)]
        first = multiply(transposed, gram)
        second = multiply(gram, matrix)
        assert all(first[row][column] + second[row][column] == 0
                   for row, column in product(range(size), repeat=2))
    for left, right in product(basis, repeat=2):
        assert embedding(bracket(left, right)) == bracket(embedding(left), embedding(right))
    assert rank([sum(matrix, []) for matrix in images], size * size) == 8
    return {'symmetric_space_dimension': 6, 'faithful_action_dimension': 8,
            'algebra_with_two_dimensional_square_dimension': 8,
            'bracket_pairs_checked': len(basis) ** 2}


def rank_dimension():
    matches = []
    for special_dimension in range(2, 101):
        for orthogonal_dimension in [2 * (special_dimension - 1),
                                     2 * (special_dimension - 1) + 1]:
            if (special_dimension * special_dimension - 1
                    == orthogonal_dimension * (orthogonal_dimension - 1) // 2):
                matches.append([special_dimension, orthogonal_dimension])
    assert matches == [[2, 3], [4, 6]]
    return {'special_linear_n_min': 2, 'special_linear_n_max': 100,
            'rank_and_dimension_matches': matches}


def natural_bases():
    for parameter in range(1, 26):
        first = [1, parameter]
        second = [-parameter, 1]
        assert first[0] * second[0] + first[1] * second[1] == 0
        assert first[0] * second[1] - first[1] * second[0] == 1 + parameter ** 2
    for first_parameter, second_parameter in product(range(1, 26), repeat=2):
        no_swap_determinant = second_parameter - first_parameter
        swap_determinant = 1 + first_parameter * second_parameter
        assert (no_swap_determinant == 0) == (first_parameter == second_parameter)
        assert swap_determinant > 0
    return {'parameter_min': 1, 'parameter_max': 25, 'ordered_parameter_pairs': 625,
            'full_automorphism_count_in_written_proof': 2}


def main():
    result = {'diagonal_forms': diagonal_forms(), 'zero_product': zero_product(),
              'split_action': split_action(), 'rank_dimension': rank_dimension(),
              'natural_basis_separation': natural_bases(),
              'scope': 'Exact rational finite examples; universal statements have written proofs in note.tex.',
              'status': 'ALL_CHECKS_OK'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
