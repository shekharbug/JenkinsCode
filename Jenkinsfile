pipeline {
    agent any
    stages {
        stage('Test code'){
            steps{
                sh '''
                    source /home/oracle/venv/bin/activate
                    cat hello.py
                    python3 hello.py
                '''
            }
        }
    }
}