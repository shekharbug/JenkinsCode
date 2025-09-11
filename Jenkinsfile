pipeline{
    agent any
    parameters {
        string(name: 'BRANCH_TO_BUILD', defaultValue: 'main', description: 'The Git branch to checkout and build')
    }

    stages{
        stage('Test parametes'){
            steps{
                echo "podname: ${params.podname}"
            }
        }
    }
}