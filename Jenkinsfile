pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.8'
                }
            }
            steps {
                sh 'python3 -m py_compile src/table_select_window.py src/table_ticket.py src/category_window.py src/items_window.py src/db_context_manager.py'
                stash(name: 'compiled-results', includes: 'src/*.py*') 
            }
        }
	    stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/src:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python3'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F table_select_window.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/src/dist/table_manager"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}