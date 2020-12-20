import os

logDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Logs/')
currentPositionPath = logDirectory + 'current-position.config'

def getCurrentPosition():
  if not os.path.exists(currentPositionPath):
    return 1

  currentPositionFile = open(currentPositionPath)

  for line in currentPositionFile:
    return float(line)

  return 1

def saveCurrentPosition(currentPosition):
  log = open(currentPositionPath, 'w')
  log.write(str(currentPosition))
  log.close()
