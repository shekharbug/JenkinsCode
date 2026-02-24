// The @Library name must match the name you set in Step 3
@Library('my-shared-library') _ 

pipeline {
    agent any
    stages {
        stage('Intro') {
            steps {
                // We call the filename we created in the vars/ folder
                sayHello('Gemini User') 
            }
        }
    }
}

