pipeline {
    agent any
    stages {
        stage('Test code'){
            steps{
                bash '''
                    . /home/oracle/venv/bin/activate
                    cat hello.py
                    python3 hello.py
                '''
            }
        }
    }
}