def logInfo(stage, message) {
    echo "[${stage}] [INFO] ${getTimestamp()} - ${message}"
}

def logSuccess(stage, message) {
    echo "[${stage}] [SUCCESS] ${getTimestamp()} - ${message}"
}

def logFailure(stage, message) {
    echo "[${stage}] [FAILURE] ${getTimestamp()} - ${message}"
}

def getTimestamp() {
    return sh(script: "TZ='America/Guatemala' date '+%Y-%m-%d %H:%M:%S'", returnStdout: true).trim()
}

