pipeline{
    agent any
    parameters {
        string(name: 'BRANCH_TO_BUILD', defaultValue: 'main', description: 'The Git branch to checkout and build')
        boolean(name: 'SKIP_TESTS', defaultValue: false, description: 'If true, tests will be skipped'),
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'production'], description: 'Target deployment environment'),
        text(name: 'DEPLOYMENT_NOTES', defaultValue: 'No specific notes.', description: 'Notes for this deployment'),
        password(name: 'DB_PASSWORD', defaultValue: '', description: 'Database password for deployment')
    }

    stages{
        stage('Test parametes'){
            steps{
                echo "podname: ${params.podname}"
            }
        }
    }
}