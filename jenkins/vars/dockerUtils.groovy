def buildImage(imageName, shortSha) {
    logUtils.logInfo("BUILD", "Building Docker image...")
    sh """
        docker build --no-cache -t ${imageName}:${shortSha} .
        docker tag ${imageName}:${shortSha} ${imageName}:latest
    """
    logUtils.logSuccess("BUILD", "Build completed.")
}

def pushImage(imageName, shortSha, dockerToken) {
    logUtils.logInfo("PUSH", "Uploading Docker image...")
    sh """
        echo "${dockerToken}" | docker login -u "d4rkghost47" --password-stdin > /dev/null 2>&1
        docker push ${imageName}:${shortSha}
        docker push ${imageName}:latest
    """
    logUtils.logSuccess("PUSH", "Image pushed successfully.")
}

