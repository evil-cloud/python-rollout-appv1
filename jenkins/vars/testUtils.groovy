def runUnitTests() {
    logUtils.logInfo("TESTS", "Running unit tests...")
    try {
        sh """
        docker build -t python-tests -f Dockerfile.test .
        docker run --rm -v $(pwd)/tests:/app/tests python-tests
        """
        logUtils.logSuccess("TESTS", "Unit tests passed successfully.")
    } catch (Exception e) {
        logUtils.logFailure("TESTS", "Unit tests failed: ${e.message}")
        error("Stopping pipeline due to unit test failure.")
    }
}

