pipeline {

    agent {
        docker {
            image 'python:3.8-slim-buster'
        }
    }

    stages {
        stage('Building Stage') {
            steps {
                sh 'python --version'
            }
        }

        stage("Testing Stage") {
            steps {
                sh 'echo /"Testing stage/"'
                sh 'python UnitTesting.py
            }
        }
    }
}