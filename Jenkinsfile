pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker build -t cicd:5000/httpiw:' + env.BRANCH_NAME + ' .'
                sh 'docker push cicd:5000/httpiw:' + env.BRANCH_NAME
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker run -d -p 8888:8888 cicd:5000/httpiw:' + env.BRANCH_NAME
            }
        }
    }
}
