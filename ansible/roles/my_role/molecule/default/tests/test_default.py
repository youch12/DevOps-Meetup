import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_apache2_is_installed(host):
    apachePack = host.package("apache2")
    assert apachePack.is_installed
    assert apachePack.version.startswith("2")

def test_apache2_running_and_enabled(host):
    apacheServ = host.service("apache2")
    assert apacheServ.is_running
    assert apacheServ.is_enabled

def test_devopsmeetup_group_exist(host):
    assert host.group("devopsmeetup").exists

def test_dev_user(host):
    user = host.user("dev")
    assert user.exists
    assert user.name == "dev"
    assert user.group == "devopsmeetup"
    assert user.groups == ["devopsmeetup"]

def test_conf_file(host):
    f = host.file("/etc/apache2/ports.conf")
    assert f.exists
    assert f.is_file
    assert f.contains("Listen 8090")

def test_index_file(host):
    f = host.file("/var/www/html/index.html")
    assert f.exists
    assert f.is_file
    assert f.contains("Welcome to DevOps Rabat Meetup")
   

