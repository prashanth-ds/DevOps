pipeline
{
    agent
    {
        docker
        {
            image 'python:3.8-slim-buster'
        }
    }

    stages
    {
        stage('Build')
        {
            steps
            {
                sh 'python --version'
            }
        }

        stage('Testing')
        {
            steps
            {
                sh 'echo "Testing stage"'
                sh 'python UnitTesting.py'
            }
        }
    }
}