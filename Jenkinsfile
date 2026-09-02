pipeline {
    agent {
        label 'docker-agent'
    }
    stages {
        stage('checkout scm'){
            steps{
                echo "doing checkout of scm git"
                checkout scm
            }
        }

        stage('install requirements for python'){
            steps{
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    which python
                    which python3
                    which pip
                    pwd
                    ls -ld requirements.txt
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Docker image creation'){
            steps{
                sh '''
                    echo "build number : ${BUILD_NUMBER}"
                    docker build -t jenkins-demo:${BUILD_NUMBER} .
                    docker image ls 
                '''
            }
        }

        stage('Start Docker'){
            steps{
                sh '''
                    docker run -itd --name demo -p 5000:5000 jenkins-demo:${BUILD_NUMBER}
                    docker container ls
                '''
            }
        }

    }
}