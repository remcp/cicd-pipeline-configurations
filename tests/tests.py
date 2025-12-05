from src.cicd import hello_world

def test_helloworld():
    outcomes = [f"hello world{i}" for i in range(1, 4)]
    assert hello_world() in outcomes
    