from pytechecker import check, get_overflow

"""
Run these tests uting pytest.
"""

# TEST 1
def test_1_int_at_string_key():
    sample = {
        "string_key": {
            "required": True,
            "allowed_types": [str]
        }
    }
    obj = {
        "string_key": 5
    }

    succ, errors = check(sample, obj)
    assert (not succ), "Int at string key did not fail."

# TEST 2
def test_2_int_at_int_key():
    sample = {
        "string_key": {
            "required": True,
            "allowed_types": [int]
        }
    }
    obj = {
        "string_key": 5
    }

    succ, errors = check(sample, obj)
    assert (succ), "Int at int key failed."

# TEST 3
def test_3_float_at_int_key():
    sample = {
        "string_key": {
            "required": True,
            "allowed_types": [int]
        }
    }
    obj = {
        "string_key": 5.1
    }

    succ, errors = check(sample, obj)
    assert (not succ), "Float at int key failed."

# TEST 4
def test_4_string_at_number_key():
    sample = {
        "string_key": {
            "required": True,
            "allowed_types": [int, float]
        }
    }
    obj = {
        "string_key": "hello there"
    }

    succ, errors = check(sample, obj)
    assert (not succ), "String at number key failed."

# TEST 5
def test_5_optional_key():
    sample = {
        "string_key": {
            "required": True,
            "allowed_types": [str]
        },
        "number_key": {
            "required": False,
            "allowed_types": [int, float]
        }
    }
    obj = {
        "string_key": "hello there"
    }

    succ, errors = check(sample, obj)
    assert (succ), "Optional key supplied failed."

# TEST 6
def test_6_missing_required_key():
    sample = {
        "string_key": {
            "required": True,
            "allowed_types": [str]
        },
        "number_key": {
            "required": True,
            "allowed_types": [int, float]
        }
    }
    obj = {
        "string_key": "hello there"
    }

    succ, errors = check(sample, obj)
    assert (not succ) and len(errors) == 1, "Missing key didn't fail."

# TEST 7
def test_7_basic_embedded_objects_two_levels():
    sample = {
        "person": {
            "required": True,
            "allowed_types": [dict],
            "embedded_dict": {
                "name": {
                    "required": True,
                    "allowed_types": [str]
                },
                "age": {
                    "required": True,
                    "allowed_types": [int]
                },
                "company": {
                    "required": True,
                    "allowed_types": [dict],
                    "embedded_dict": {
                        "comp_name": {
                            "required": True,
                            "allowed_types": [str]
                        },
                        "employed_date": {
                            "required": False,
                            "allowed_types": [str]
                        }
                    }
                }
            }
        }
    }
    obj = {
        "person": {
            "name": "Daniel Cronqvist",
            "age": 21,
            "company": {
                "comp_name": "Hello World!",
                "employed_date": "2020-02-01"
            }
        }
    }

    succ, errors = check(sample, obj)
    assert (succ), "Basic person data object failed."

# TEST 8
def test_8_basic_embedded_objects_two_levels_without_optional():
    sample = {
        "person": {
            "required": True,
            "allowed_types": [dict],
            "embedded_dict": {
                "name": {
                    "required": True,
                    "allowed_types": [str]
                },
                "age": {
                    "required": True,
                    "allowed_types": [int]
                },
                "company": {
                    "required": True,
                    "allowed_types": [dict],
                    "embedded_dict": {
                        "comp_name": {
                            "required": True,
                            "allowed_types": [str]
                        },
                        "employed_date": {
                            "required": False,
                            "allowed_types": [str]
                        }
                    }
                }
            }
        }
    }
    obj = {
        "person": {
            "name": "Daniel Cronqvist",
            "age": 21,
            "company": {
                "comp_name": "Hello World!",
            }
        }
    }

    succ, errors = check(sample, obj)
    assert (succ), "Basic person data object without optionals failed."

# TEST 9
def test_9_basic_list_of_nums():
    sample = {
        "nums": {
            "required": True,
            "allowed_types": [list],
            "list_element": {
                "allowed_types": [int, float]
            }
        }
    }
    obj = {
        "nums": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0
        ]
    }

    succ, errors = check(sample, obj)
    assert (succ), "List of nums failed"

# TEST 10
def test_10_basic_list_of_strings():
    sample = {
        "strings": {
            "required": True,
            "allowed_types": [list],
            "list_element": {
                "allowed_types": [str]
            }
        }
    }
    obj = {
        "strings": [
            "Hejsan",
            "där",
            "du",
            "din",
            "lilla",
            "råtta"
        ]
    }

    succ, errors = check(sample, obj)
    assert (succ), "List of strings failed"

# TEST 11
def test_11_basic_list_of_strings_two_nums():
    sample = {
        "strings": {
            "required": True,
            "allowed_types": [list],
            "list_element": {
                "allowed_types": [str]
            }
        }
    }
    obj = {
        "strings": [
            "Hejsan",
            "där",
            "du",
            5,
            "din",
            "lilla",
            8,
            "råtta"
        ]
    }

    succ, errors = check(sample, obj)
    assert (not succ) and len(errors) == 2, "List of strings failed, with two nums."

# TEST 12
def test_12_basic_list_of_objects():
    sample = {
        "people": {
            "required": True,
            "allowed_types": [list],
            "list_element": {
                "allowed_types": [dict],
                "embedded_dict": {
                    "name": {
                        "required": True,
                        "allowed_types": [str]
                    },
                    "age": {
                        "required": True,
                        "allowed_types": [int]
                    },
                    "interests": {
                        "required": True,
                        "allowed_types": [list],
                        "list_element": {
                            "allowed_types": [str]
                        }
                    }
                }
            }
        }
    }
    obj = {
        "people": [
            {
                "name": "Daniel Cronqvist",
                "age": 21,
                "interests": [
                    "programming",
                    "games"
                ]
            },
            {
                "name": "Saga Kortesaari",
                "age": 21,
                "interests": [
                    "programming",
                    "games",
                    "painting"
                ]
            }
        ]
    }

    succ, errors = check(sample, obj)
    assert (succ), "List of people failed."

# TEST 13
def test_13_basic_list_of_objects():
    sample = {
        "people": {
            "required": True,
            "allowed_types": [list],
            "list_element": {
                "allowed_types": [dict],
                "embedded_dict": {
                    "name": {
                        "required": True,
                        "allowed_types": [str]
                    },
                    "age": {
                        "required": True,
                        "allowed_types": [int]
                    },
                    "interests": {
                        "required": True,
                        "allowed_types": [list],
                        "list_element": {
                            "allowed_types": [str]
                        }
                    }
                }
            }
        }
    }
    obj = {
        "people": [
            {
                "name": "Daniel Cronqvist",
                "age": 21,
                "interests": [
                    "programming",
                    "games",
                    5
                ]
            },
            {
                "name": "Saga Kortesaari",
                "age": "21",
                "interests": [
                    "programming",
                    "games",
                    "painting"
                ],
                "extra_key_should_fail": 25
            }
        ]
    }

    succ, errors = check(sample, obj)
    assert (not succ) and len(errors) == 3, "List of people failed."

# TEST 14
def test_14_basic_tuple_key():
    sample = {
        "tuple": {
            "required": True,
            "allowed_types": [tuple],
            "tuple_order": [str, int, int, float]
        }
    }
    obj = {
        "tuple": ("Daniel", 5, "10", 21.5674)
    }

    succ, errors = check(sample, obj)
    assert (not succ) and len(errors) == 1, "Basic tuple failed."

# TEST 15
def test_15_basic_tuple_key():
    sample = {
        "tuple": {
            "required": True,
            "allowed_types": [tuple],
            "tuple_order": [str, int, int, float]
        }
    }
    obj = {
        "tuple": ("Daniel", 5, "10")
    }

    succ, errors = check(sample, obj)
    assert (not succ) and len(errors) == 1, "Basic tuple with different lengths failed."

# TEST 16
def test_16_basic_tuple_key():
    sample = {
        "tuple": {
            "required": True,
            "allowed_types": [tuple],
            "tuple_order": [str, int, int, float]
        }
    }
    obj = {
        "tuple": ("Daniel", 5, 10, 121.67)
    }

    succ, errors = check(sample, obj)
    assert (succ) and len(errors) == 0, "Basic tuple with correct order and same length failed."

# TEST 17
def test_17_checking_basic_overflow():
    sample = {
        "tuple": {
            "required": True,
            "allowed_types": [tuple],
            "tuple_order": [str, int, int, float]
        }
    }
    obj = {
        "tuple": ("Daniel", 5, 10, 121.67),
        "cool_key": "Hello World!"
    }

    overflow = get_overflow(sample, obj)
    assert overflow == ["cool_key"], "Basic overflow test failed."

# TEST 17
def test_17_checking_two_depth_overflow():
    sample = {
        "person": {
            "required": True,
            "allowed_types": [dict],
            "embedded_dict": {
                "name": {
                    "required": True,
                    "allowed_types": [str]
                }
            }
        }
    }
    obj = {
        "person": {
            "name": "Daniel Cronqvist",
            "age": 21
        }
    }

    overflow = get_overflow(sample, obj, all_sub=True)
    assert overflow == ["age"], "Basic overflow test with depth failed."


# TEST 18
def test_18_checking_high_depth_overflow():
    sample = {
        "person": {
            "required": True,
            "allowed_types": [dict],
            "embedded_dict": {
                "name": {
                    "required": True,
                    "allowed_types": [str]
                },
                "address": {
                    "required": True,
                    "allowed_types": [dict],
                    "embedded_dict": {
                        "city": {
                            "required": True,
                            "allowed_types": [str]
                        },
                        "street": {
                            "required": True,
                            "allowed_types": [str]
                        }
                    }
                }
            }
        }
    }
    obj = {
        "person": {
            "name": "Daniel Cronqvist",
            "age": 21,
            "address": {
                "city": "Göteborg",
                "street": "Pilegårdsgatan 20B",
                "postal_code": "41877"
            }
        }
    }

    overflow = get_overflow(sample, obj, all_sub=True)
    assert overflow == ["age", "postal_code"], "Basic overflow test with multiple depth failed."
