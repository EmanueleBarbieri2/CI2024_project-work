import numpy as np

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: ...


def f3(x: np.ndarray) -> np.ndarray: ...


def f4(x: np.ndarray) -> np.ndarray:
    return np.exp(np.exp(np.cos(x[1]))) - np.sqrt(5)


def f5(x: np.ndarray) -> np.ndarray:
    return np.log(np.abs(np.cos(x[1]))) / np.exp(np.exp(np.pi))


def f6(x: np.ndarray) -> np.ndarray:
    return x[1] - np.abs(x[0] * np.cos(np.sqrt(np.abs(np.log(5)+np.pi)*2)))


def f7(x: np.ndarray) -> np.ndarray:
    return 7 * np.abs(x[0]) * x[1] * x[1]


def f8(x: np.ndarray) -> np.ndarray: 
    return x[5] * (np.exp(7) * np.log(np.pi))