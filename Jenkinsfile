pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'flask-app:latest'
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/20BQ1A0458/jenkins-docker-k8s-pipeline.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Push to Local Registry') {
            steps {
                sh 'docker save $DOCKER_IMAGE | (eval $(minikube docker-env) && docker load)'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
        
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
