from factory_agent_langchain.course import DSA, construct_course


def test_import() -> None:
    import factory_agent_langchain  # noqa: F401

    assert "Empty test to ensure pytest passes."

def test_dsa() -> None:
    import factory_agent_langchain  # noqa: F401
    dsa = DSA()
    create_course = construct_course(DSA)
    print(create_course)
    assert create_course.fee == 8000
    assert create_course.batches == 5
