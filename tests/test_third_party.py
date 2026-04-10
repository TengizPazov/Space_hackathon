def test_numpy_installed():
    try:
        import numpy as np
        assert np.__version__ is not None
        print(f" numpy {np.__version__} установлен")
    except ImportError:
        assert False, " numpy не установлен"

def test_matplotlib_installed():
    try:
        import matplotlib
        assert matplotlib.__version__ is not None
        print(f" matplotlib {matplotlib.__version__} установлен")
    except ImportError:
        assert False, " matplotlib не установлен"

def test_numpy_works():
    import numpy as np
    a = np.array([1, 2, 3])
    assert a.sum() == 6
    print(" numpy работает корректно")

def test_matplotlib_works():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
    plt.close(fig)
    print(" matplotlib работает корректно")

if __name__ == "__main__":
    test_numpy_installed()
    test_matplotlib_installed()
    test_numpy_works()
    test_matplotlib_works()
    print("\n Все тесты пройдены, окружение работает!")