node {
    try {
        stage('Build') {
            echo 'Building the application...'
        }
        stage('Test') {
            echo 'Running tests...'
            // Simulating a failed test with 'error' step
            error('Tests failed!')
        }
    }
    catch (e) {
        // This acts like the 'failure' block
        echo 'The build failed. Sending a notification...'
        currentBuild.result = 'FAILURE'
        throw e
    }
    finally {
        // This acts like the 'always' block
        echo 'This will always run for cleanup tasks.'
        // Additional conditional logic can be added here
        if (currentBuild.result == 'SUCCESS') {
            // This is the equivalent of a 'success' block
            echo 'The build was successful! Proceeding with deployment...'
        }
    }
}