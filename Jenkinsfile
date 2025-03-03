// Pipeline version: v1.1.3
// @Library('ci-pipelines-lib') _

pipeline {
    agent { label 'jenkins-jenkins-agent' }

    environment {
        IMAGE_NAME      = "d4rkghost47/python-rollout-appv1"
        REGISTRY        = "https://index.docker.io/v1/"
        SHORT_SHA       = "${GIT_COMMIT[0..7]}"
        SONAR_PROJECT   = "python-rollout-appv1"
        SONAR_HOST      = "http://sonarqube-sonarqube.sonarqube.svc.cluster.local:9000"
        TRIVY_HOST      = "http://trivy.trivy-system.svc.cluster.local:4954"
        TZ              = "America/Guatemala"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    logUtils.logInfo("CHECKOUT", "Starting code checkout...")
                    checkout scm
                    logUtils.logSuccess("CHECKOUT", "Code checkout completed.")
                }
            }
        }

        stage('Static Code Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    script {
                        sonarUtils.runSonarQubeAnalysis(env.SONAR_PROJECT, env.SONAR_HOST, SONAR_TOKEN)
                    }
                }
            }
        }

        stage('Unit Tests') {
            steps {
                container('dind') {
                    script {
                        testUtils.runUnitTests()
                    }
                }
            }
        }

        stage('Build Image') {
            steps {
                container('dind') {
                    script {
                        dockerUtils.buildImage(env.IMAGE_NAME, env.SHORT_SHA)
                    }
                }
            }
        }

        stage('Push Image') {
            steps {
                container('dind') {
                    script {
                        withCredentials([string(credentialsId: 'docker-token', variable: 'DOCKER_TOKEN')]) {
                            dockerUtils.pushImage(env.IMAGE_NAME, env.SHORT_SHA, DOCKER_TOKEN)
                        }
                    }
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    securityUtils.runSecurityScan(env.TRIVY_HOST, env.IMAGE_NAME, env.SHORT_SHA)
                }
            }
        }
    }

    post {
        success {
            script {
                logUtils.logSuccess("PIPELINE", "Pipeline completed successfully.")
            }
        }
        
        failure {
            script {
                logUtils.logFailure("PIPELINE", "Pipeline failed.")
            }
        }
    }
}

