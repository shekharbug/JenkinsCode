pipeline {
    agent any
    stages {
        stage('Test code'){
            steps{
                sh '''
                    source /home/oracle/venv/bin/activate
                    which python
                    python hello.py
                '''
            }
        }
    }
}