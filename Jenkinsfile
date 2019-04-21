node('master'){
    stage('prepare')
            {
                checkout scm
            }
    stage('Molecule create'){
        sh 'cd ansible/roles/my_role && molecule create'
    }
    stage('Molecule converge'){
        sh 'cd ansible/roles/my_role && molecule converge'
    }

    stage('Molecule verify'){
        sh 'cd ansible/roles/my_role && molecule verify'
    }

    stage('Molecule destroy '){
        sh 'cd ansible/roles/my_role && molecule destroy'
    }
}
