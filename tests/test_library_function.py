from scikit_build_core_minimal_shared_library_example import library_function


def test_library_function_returns_integer():
    return_value = library_function()
    assert return_value == 4
