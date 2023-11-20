import numpy as np


def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  threexthree = np.array(list).reshape(3, 3)
  calculations = {}
  calculations['mean'] = [
      np.mean(threexthree, axis=0).tolist(),
      np.mean(threexthree, axis=1).tolist(),
      np.mean(threexthree).tolist()
  ]
  calculations['variance'] = [
      np.var(threexthree, axis=0).tolist(),
      np.var(threexthree, axis=1).tolist(),
      np.var(threexthree)
  ]
  calculations['standard deviation'] = [
      np.std(threexthree, axis=0).tolist(),
      np.std(threexthree, axis=1).tolist(),
      np.std(threexthree)
  ]
  calculations['max'] = [
      np.max(threexthree, axis=0).tolist(),
      np.max(threexthree, axis=1).tolist(),
      np.max(threexthree).tolist()
  ]
  calculations['min'] = [
      np.min(threexthree, axis=0).tolist(),
      np.min(threexthree, axis=1).tolist(),
      np.min(threexthree).tolist()
  ]
  calculations['sum'] = [
      np.sum(threexthree, axis=0).tolist(),
      np.sum(threexthree, axis=1).tolist(),
      np.sum(threexthree).tolist()
  ]
  return calculations
