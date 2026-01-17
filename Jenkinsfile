pipeline {
    agent any

    environment {
        // Use your GitHub credentials ID from Jenkins
        GIT_CREDENTIALS = 'aa6df17f-c53e-482c-a244-850ffe34f949'
        REPO_URL = 'https://github.com/harishkemkar/Automation_old_file_mover.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: "${REPO_URL}",
                    credentialsId: "${GIT_CREDENTIALS}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Adjust if you have a tests/ folder or specific test runner
                sh 'pytest --maxfail=1 --disable-warnings -q || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t automation-old-file-mover:latest .'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }

        stage('Health Check') {
            steps {
                script {
                    try {
                        sh 'curl -f http://localhost:8080/health || exit 1'
                    } catch (Exception e) {
                        error("Health check failed: ${e}")
                    }
                }
            }
        }
    }

    post {
        always {
            // Collect test results and logs if available
            junit 'tests/*.xml'
            archiveArtifacts artifacts: '**/logs/*.log', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}