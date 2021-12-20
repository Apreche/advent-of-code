import snailfish
import unittest
import utils


class TestSFNumber(unittest.TestCase):
    def test_parse(self):
        test_number = "[[[[30,0],[0,0]],1],4]"
        obj = snailfish.SFNumber(test_number)
        self.assertEqual(
            obj.number,
            ['[', '[', '[', '[', 30, 0, ']', '[', 0, 0, ']', ']', 1, ']', 4, ']']
        )
        self.assertEqual(
            str(obj), test_number
        )

    def test_explode_once(self):
        test_cases = [
            ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
            ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
            ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
            (
                "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
                "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
            ),
            (
                "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
                "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
            )
        ]
        for before, after in test_cases:
            obj = snailfish.SFNumber(before)
            obj._explode_one()
            self.assertEqual(str(obj), after)

    def test_split_once(self):
        test_cases = [
            (
                "[[[[0,7],4],[15,[0,13]]],[1,1]]",
                "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
            ),
            (
                "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
                "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
            )
        ]
        for before, after in test_cases:
            obj = snailfish.SFNumber(before)
            obj._split_one()
            self.assertEqual(str(obj), after)

    def test_addition(self):
        test_cases = [
            ("[1,2]", "[[3,4],5]", "[[1,2],[[3,4],5]]"),
            (
                "[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]",
                "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
            )
        ]
        for a, b, result in test_cases:
            obj = snailfish.SFNumber(a)
            obj.add(snailfish.SFNumber(b))
            self.assertEqual(str(obj), result)

    def test_full_reduction(self):
        test_cases = [
            (
                "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]",
                "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
            ),
        ]
        for before, after in test_cases:
            obj = snailfish.SFNumber(before)
            obj.reduce()
            self.assertEqual(str(obj), after)

    def test_magnitude(self):
        test_cases = [
            ("[[1,2],[[3,4],5]]", 143),
            ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
            ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
            ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
            ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
            ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
            ("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", 4140),
        ]
        for number, magnitude in test_cases:
            obj = snailfish.SFNumber(number)
            self.assertEqual(obj.magnitude, magnitude)

    def test_snail_list(self):
        test_cases = [
            (
                [
                    "[1,1]",
                    "[2,2]",
                    "[3,3]",
                    "[4,4]"
                ],
                "[[[[1,1],[2,2]],[3,3]],[4,4]]"
            ),
            (
                [
                    "[1,1]",
                    "[2,2]",
                    "[3,3]",
                    "[4,4]",
                    "[5,5]",
                ],
                "[[[[3,0],[5,3]],[4,4]],[5,5]]"
            ),
            (
                [
                    "[1,1]",
                    "[2,2]",
                    "[3,3]",
                    "[4,4]",
                    "[5,5]",
                    "[6,6]",
                ],
                "[[[[5,0],[7,4]],[5,5]],[6,6]]"
            ),
            (
                [
                    "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
                    "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
                    "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
                    "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
                    "[7,[5,[[3,8],[1,4]]]]",
                    "[[2,[2,2]],[8,[8,1]]]",
                    "[2,9]",
                    "[1,[[[9,3],9],[[9,0],[0,7]]]]",
                    "[[[5,[7,4]],7],1]",
                    "[[[[4,2],2],6],[8,7]]",
                ],
                "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
            ),
            (
                [
                    "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
                    "[[[5,[2,8]],4],[5,[[9,9],0]]]",
                    "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
                    "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
                    "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
                    "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
                    "[[[[5,4],[7,7]],8],[[8,3],8]]",
                    "[[9,3],[[9,9],[6,[4,9]]]]",
                    "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
                    "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
                ],
                "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
            )
        ]

        for before, after in test_cases:
            result = snailfish.process_snail_list(before)
            self.assertEqual(str(result), after)


class UtilTest(unittest.TestCase):

    def test_rightmost_null_case(self):
        test_list = ['a', 'b']
        result = utils.add_to_rightmost_int(test_list, 3)
        self.assertEqual(result, test_list)

    def test_rightmost_normal_case(self):
        test_list = ['a', 'b', 1]
        result = utils.add_to_rightmost_int(test_list, 3)
        self.assertEqual(result, ['a', 'b', 4])
        test_list = [1, 'a', 'b']
        result = utils.add_to_rightmost_int(test_list, 3)
        self.assertEqual(result, [4, 'a', 'b'])

    def test_rightmost_multiple_case(self):
        test_list = [5, 'a', 5, 'b']
        result = utils.add_to_rightmost_int(test_list, 3)
        self.assertEqual(result, [5, 'a', 8, 'b'])

    def test_leftmost_null_case(self):
        test_list = ['a', 'b']
        result = utils.add_to_leftmost_int(test_list, 3)
        self.assertEqual(result, test_list)

    def test_leftmost_normal_case(self):
        test_list = ['a', 'b', 1]
        result = utils.add_to_leftmost_int(test_list, 3)
        self.assertEqual(result, ['a', 'b', 4])
        test_list = [1, 'a', 'b']
        result = utils.add_to_leftmost_int(test_list, 3)
        self.assertEqual(result, [4, 'a', 'b'])

    def test_leftmost_multiple_case(self):
        test_list = [5, 'a', 5, 'b']
        result = utils.add_to_leftmost_int(test_list, 3)
        self.assertEqual(result, [8, 'a', 5, 'b'])


if __name__ == '__main__':
    unittest.main()
