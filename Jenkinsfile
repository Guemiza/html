pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'amelgm/project-adminlocallibrary:v2' // Remplacez par votre nom d'utilisateur, le nom de l'image et le tag
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Vous pouvez sauter cette étape si votre image est déjà construite
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").run('--rm -t python manage.py test')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Ajoutez vos étapes de déploiement ici, par exemple :
                    // docker-compose up -d
                    // ou kubectl apply -f k8s-deployment.yaml
                }
            }
        }
    }

    post {
        always {
            script {
                // Nettoyez après vous, par exemple, arrêtez et supprimez les conteneurs temporaires
                docker.image("${DOCKER_IMAGE}").stop()
                docker.image("${DOCKER_IMAGE}").remove()
            }
        }
    }
}
