pipeline {

    agent {
        docker {
            image 'python:3.8.11-buster'
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
                sh 'python -m unittest UnitTesting.py
            }
        }
    }
}