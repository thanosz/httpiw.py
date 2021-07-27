pipeline {
    agent {
        docker {
            image 'httpiw:master'
            args '-p 8080:9080' 
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t httpiw .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo this should be the test invocation'
            }
        }
    }
}
