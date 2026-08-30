pipeline {
    agent any
    stages {
        stage('Test code'){
            steps{
                sh '''
                    cat hello.py
                    python3 hello.py
                '''
            }
        }
    }
}