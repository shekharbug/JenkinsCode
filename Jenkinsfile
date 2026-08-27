pipeline {

    agent any

    stages {

        stage('Welcome') {
            steps {
                echo 'Welcome to Jenkins Pipeline'
            }
        }

        stage('System Information') {
            steps {
                sh '''
                    echo "Hostname:"
                    hostname

                    echo "Current User:"
                    whoami

                    echo "Current Directory:"
                    pwd
                '''
            }
        }

        stage('Git Version') {
            steps {
                sh 'git --version'
            }
        }

    }
}
