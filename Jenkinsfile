pipeline {
    agent any
    stages {
        stage('checkout scm'){
            steps{
                echo "doing checkout of scm git"
                checkout scm
            }

        stage('install requirements for python'){
            steps{
                sh '''
                    python3 -m vev venv
                    . venv/bin/activate
                    which python
                    which python3
                    which pip
                '''
            }
        }
        }
    }
}