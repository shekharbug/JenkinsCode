pipeline {
    agent any
    stages {
        stage('Test code'){
            steps{
                sh '''
                    source /home/oracle/venv/bin/activate
                    which python3
                    python3 hello.py
                '''
            }
        }
    }
}