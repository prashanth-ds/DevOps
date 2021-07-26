pipeline
{
    agent none
    stages
    {
        stage('Build')
        {
            agent
            {
                docker
                {
                    image 'python:3.8-slim-buster'
                }
            }
            steps
            {
                sh 'python --version'
            }
        }

        stage('Testing')
        {
            agent
            {
                docker
                {
                    image 'python:3.8-slim-buster'
                }
            }
            steps
            {
                sh 'echo "Testing stage"'
                sh 'python UnitTesting.py'
            }
        }
    }
}