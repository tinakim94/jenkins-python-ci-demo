pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                bat 'python -m unittest -v'
            }
        }

        stage('Run') {
            steps {
                bat 'python app.py'
            }
        }
    }
}