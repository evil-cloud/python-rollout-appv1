def runSonarQubeAnalysis(projectKey, sonarHost, sonarToken) {
    logUtils.logInfo("ANALYSIS", "Running static code analysis with SonarQube...")
    sh """
        sonar-scanner \
            -Dsonar.projectKey=${projectKey} \
            -Dsonar.sources=src \
            -Dsonar.language=py \
            -Dsonar.host.url=${sonarHost} \
            -Dsonar.login=${sonarToken}
    """
    logUtils.logSuccess("ANALYSIS", "SonarQube analysis completed successfully.")
}

