def runSecurityScan(trivyHost, imageName, shortSha) {
    logUtils.logInfo("SECURITY SCAN", "Running Trivy security scan...")
    sh """
        trivy image --server ${trivyHost} ${imageName}:${shortSha} --severity HIGH,CRITICAL --quiet
    """
    logUtils.logSuccess("SECURITY SCAN", "Security scan completed successfully.")
}

