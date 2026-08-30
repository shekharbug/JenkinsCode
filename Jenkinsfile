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
    post {
        always{
            echo "This code always run"
        }
        success{
            echo "code success"
        }
        cleanup{
            echo "Do cleanup"
        }
        failure {
            cleanWs() # do cleanup of workspace
        }
    }
}