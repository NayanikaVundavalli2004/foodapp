pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/NayanikaVundavalli2004/foodapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("nayanika3664/foodapp:latest")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh '''
                    docker login -u nayanika3664 -p Niharika@2010
                    docker push nayanika3664/foodapp:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml --validate=false'
                sh 'kubectl apply -f service.yaml --validate=false'
            }
        }
    }
}
