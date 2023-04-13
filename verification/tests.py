"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [8, [(4, 2), (5, 2), (2, 1), (8, 3)]],
            "answer": 21,
        },
        {
            "input": [20, [(5, 9), (4, 10)]],
            "answer": 10,
        },
        {
            "input": [8, [(10, 10)]],
            "answer": 0,
        },
    ],
    "Extra": [
        {
            "input": [10, [(4, 3), (2, 2), (6, 4), (3, 1)]],
            "answer": 30,
        },
        {
            "input": [15, [(7, 4), (8, 5), (6, 3), (9, 6)]],
            "answer": 30,
        },
        {
            "input": [20, [(10, 5), (15, 8), (7, 4), (12, 6), (4, 2)]],
            "answer": 40,
        },
        {
            "input": [30, [(20, 10), (15, 8), (18, 12), (10, 5), (8, 4), (5, 3)]],
            "answer": 60,
        },
        {
            "input": [9, [(2, 1), (3, 1), (5, 2)]],
            "answer": 27,
        },
    ]
}
