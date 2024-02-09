pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        ANSIBLE_PLAYBOOK = '/home/devops/BureauFiles/DjangoProject-Admin/locallibrary/ansible.yml'
        INVENTORY_FILE = '/home/devops/BureauFiles/DjangoProject-Admin/locallibrary/inventory.ini'  // Correction ici
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                script {
                    def ansiblePlaybookPath = "${WORKSPACE}/path/vers/votre/ansible.yml"
                    def inventoryFilePath = "${WORKSPACE}/path/vers/votre/inventory.ini"

                    // Appeler Ansible pour le déploiement
                    sh """
                        ansible-playbook -i ${inventoryFilePath} ${ansiblePlaybookPath}
                    """
                }
            }
        }
    }
    
    post {
        always {
            script {
                sh 'docker stop $(docker ps -a -q)'
                sh 'docker rm $(docker ps -a -q)'
            }
        }
    }
}

