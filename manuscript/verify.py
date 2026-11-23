import json
from fractions import Fraction
from math import comb, factorial, gcd


def catalan(index):
    return comb(2 * index, index) // (index + 1)


def valuation_two(integer):
    assert integer > 0
    return (integer & -integer).bit_length() - 1


def minimal_exponent(index):
    value = Fraction((2 * index + 1) * catalan(index), 4 ** index)
    denominator = value.denominator
    assert denominator & (denominator - 1) == 0
    return denominator.bit_length() - 1


def main():
    bound = 1000
    partial_sum = Fraction(0)
    denominator_prefix = [1, 2, 16, 32, 128, 256, 4096, 8192, 32768, 65536]
    numerator_prefix = [1, 3, 29, 65, 281, 595, 9949, 20613, 84883, 173965]
    for index in range(1, bound + 1):
        number = catalan(index)
        summand = Fraction(number, 4 ** (index - 1))
        partial_sum += summand
        assert partial_sum == 4 - (2 * index + 1) * summand
        assert partial_sum.denominator == summand.denominator
        assert valuation_two(number) == (index + 1).bit_count() - 1
        exponent = minimal_exponent(index)
        assert exponent == 2 * index + 1 - (index + 1).bit_count()
        assert partial_sum.denominator == 2 ** (exponent - 2)
        assert exponent == index + valuation_two(factorial(index + 1))
        assert partial_sum.numerator == 4 * partial_sum.denominator - (2 * index + 1) * (number >> valuation_two(number))
        companion = (2 ** index - Fraction(comb(2 * index + 2, index + 1), 2 ** (index + 1))) * gcd(factorial(index + 1), 2 ** (index + 1))
        assert companion == partial_sum.numerator
        if index <= len(denominator_prefix):
            assert partial_sum.denominator == denominator_prefix[index - 1]
            assert partial_sum.numerator == numerator_prefix[index - 1]
    exponents = [minimal_exponent(index) for index in range(bound + 5)]
    assert exponents[0] == 0
    for index in range(bound + 1):
        assert exponents[index + 1] - exponents[index] == 1 + valuation_two(index + 2)
        assert exponents[index + 4] - exponents[index] == 7 + valuation_two((index + 5) // 4)
    for index in range(1, 251):
        assert -exponents[4 * index - 1] - exponents[4 * index] + exponents[4 * index + 1] + exponents[4 * index + 2] == 6
    for index in range(501):
        assert exponents[2 * index + 1] - exponents[2 * index + 2] - exponents[2 * index + 3] + exponents[2 * index + 4] == 0
    for index in range(1, 201):
        convolution = Fraction(sum(comb(2 * (term + 1), term + 1) * comb(2 * (index - term), index - term) for term in range(index)), 4 ** index)
        closed_form = 4 - Fraction(2 * comb(2 * index + 2, index + 1), 4 ** index)
        assert convolution == closed_form
    assert Fraction(24, 16).numerator == 3
    assert 2 % 2 == 0
    assert all(2 % (2 ** exponent) == 2 for exponent in range(2, 101))
    for degree in range(bound + 1):
        coefficient = sum(value for power, value in [(1, 2), (2, 1), (3, 3), (4, 1)] if degree >= power)
        scale = 8
        while scale - 1 <= degree:
            for offset in range(4):
                if degree >= scale - 1 + offset and (degree - (scale - 1 + offset)) % scale == 0:
                    coefficient += 1
            scale *= 2
        assert coefficient == exponents[degree] - (exponents[degree - 4] if degree >= 4 else 0)
    result = {
        'status': 'pass',
        'arithmetic': 'exact integers and reduced rational numbers',
        'main_identity_and_denominators': {'first': 1, 'last': bound},
        'valuation_and_companion_numerator': {'first': 1, 'last': bound},
        'A283208_first_difference_and_four_step_recurrence': {'first': 0, 'last': bound},
        'first_Serodio_identity': {'first': 1, 'last': 250},
        'second_Serodio_identity': {'first': 0, 'last': 500},
        'corrected_convolution_identity': {'first': 1, 'last': 200},
        'A283208_generating_function_coefficients': {'first': 0, 'last': bound},
        'OEIS_numerator_and_denominator_prefix_terms': 10,
        'universal_coverage': 'The note supplies written proofs; the pinned Lean declaration covers the main denominator equality.'
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
