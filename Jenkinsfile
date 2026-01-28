pipeline {
    agent { 
        docker { 
            image 'python:3.10' 
            } 
    }

    environment {
        EC2_HOST = "ec2-user@35.154.224.150"   // Replace with your EC2 public IP
        REPO_URL = "https://github.com/harishkemkar/Automation_old_file_mover.git"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: "${REPO_URL}"
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt || true
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                source venv/bin/activate
                pip install flake8 || true
                flake8 --ignore=E501 .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pip install pytest || true
                pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                // Use Jenkins SSH credentials
                sshagent(['ec2_username']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ${EC2_HOST} "
                    pkill -f 'python3 app.py' || true &&
                    cd Automation_old_file_mover || git clone ${REPO_URL} Automation_old_file_mover &&
                    cd Automation_old_file_mover &&
                    git pull origin main &&
                    pip3 install -r requirements.txt &&
                    nohup python3 app.py > app.log 2>&1 &"
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
