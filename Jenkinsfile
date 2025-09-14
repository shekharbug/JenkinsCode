pipeline{
    agent any
    stages {
        stage('git Pull'){
            steps{
                git branch: 'main', url: 'https://github.com/shekharbug/JenkinsCode.git'
            }
        }
        stage('Setting virtual env'){
            steps{
                script{
                    sh '. /mnt/c/shekhar/pCode/venv/bin/activate'
                }
            }
        }
        stage('Execute Ansible code'){
            steps{
                ansiblePlaybook credentialsId: 'dbhost_private_id', become: true, installation: 'Ansible', inventory: 'ansibleCode/inv/hosts', playbook: 'ansibleCode/os_system_info.yml', vaultTmpPath: ''
            }
        }
    }
}