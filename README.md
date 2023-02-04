# Development Setup

<div align="center">

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/fedejaure/dev-setup?logo=github)](https://github.com/fedejaure/dev-setup/releases)
[![Tests](https://github.com/fedejaure/dev-setup/workflows/tests/badge.svg)](https://github.com/fedejaure/dev-setup/actions?workflow=tests)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://opensource.org/licenses/MIT)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)

</div>

My own Ansible collection for development setup (use by your own risk).

* GitHub repo: <https://github.com/fedejaure/dev-setup.git>
* Free software: MIT

## Features

* TODO

## Quickstart

### Starting from a brand-new Mac

1. Ensure Apple's command line tools are installed (xcode-select --install to launch the installer).

2. Download this repository to your local drive.

3. Install requirements:

    Create a temporary virtualenv, Active the virtualenv and install ansible: 
    
    ```shell session
    $ /usr/bin/python3 -m venv .venv
    $ . .venv/bin/activate
    (.venv)$ pip3 install ansible
    ```

4. Install ansible requirements `ansible-galaxy install -r requirements.yml`.

5. Copy `inventory.example` into `inventory`.

6. Run `ansible-playbook playbooks/main.yml --ask-become-pass -i inventory`.

> Note: You need to agree to Xcode's license.

### Configuring a remote Mac

### Starting from a configured machine

1. Clone this repository.

2. Install dependencies:

    ```shell session
    $ poetry install --no-root
    Using python3.10 (3.10.8)
    Creating virtualenv .venv
    Installing dependencies from lock file

    Package operations: 97 installs, 0 updates, 0 removals

    ...
    ```

3. Activate the virtual environment:

    ```shell session
    $ poetry shell
    Using python3.10 (3.10.8)
    Spawning shell within .venv
    (dev-setup)$
    ```

4. Install required Ansible roles:

    ```shell session
    (dev-setup)$ inv galaxy-install
    ```

5. Configure the `inventory` file:

    * Local target:
    
        >  Copy `inventory.example` into `inventory`.


    * Remote target:
    
        >    Configure the `inventory` file as:
        >
        >    ```ini
        >    [macos]
        >    <ip address or hostname of the target> ansible_user=<target user> ansible_python_interpreter=/usr/bin/python3
        >    ```
        >
        > #### On the target Mac:
        >    
        > 1. Ensure Apple's command line tools are installed (xcode-select --install to launch the installer).
        >
        > 2. Go to System Preferences > Sharing.
        >
        > 3. Enable 'Remote Login'.
        >
        >   > You can also enable remote login on the command line:
        >   > 
        >   > ```shell session
        >   > $ sudo systemsetup -setremotelogin on
        >   > ```
        >
        >   > Note: You need to agree to Xcode's license.

6. Run the playbook:

    ```shell session
    (dev-setup)$ inv playbook --ask-pass --ask-become-pass
    ```

7. Enjoy!

### Running a specific set of tagged tasks

The tags available are:

* always
* dock
* homebrew
* mas
* oh-my-zsh
* pipx
* pyenv

### Overriding Defaults

You can override the defaults configured in default.<system-os>.config.yml by creating a <system-os>.config.yml file and setting the overrides in that file. e.g.:

```yaml
---
mas_email: "example@example.com"

homebrew_installed_packages:
  - git
  - pipx
  - jesseduffield/lazydocker/lazydocker
  - awscli
  - tfenv

homebrew_cask_apps:
  - firefox
  - google-chrome
  - docker
  - openvpn-connect
  - hpedrorodrigues/tools/dockutil
  - visual-studio-code
  - zoom
  - tad
  - keybase
  - obsidian
  - google-cloud-sdk

pyenv_python_versions:
  - 3.7.15
  - 3.8.15
  - 3.9.15
  - 3.10.8
  - 3.11.0
```

Development

To display available tasks run:

```shell session
(dev-setu)$ inv --list
Available tasks:

  ansible-lint     Run ansible linter.
  clean            Run all clean sub-tasks.
  clean-python     Clean up python file artifacts.
  flake8           Run flake8.
  format           Format code.
  galaxy-install   Install ansible-galaxy requirements.
  hooks            Run pre-commit hooks.
  install-hooks    Install pre-commit hooks.
  lint             Run all linting.
  mypy             Run mypy.
  playbook         Run Ansible playbooks, executing the defined tasks on the targeted hosts.
  safety           Run safety.
  tests            Run ansible molecule test.
  version          Bump version.
  yamllint         Run yamllint, a linter for YAML files.
```

## Author Information

This playbook was created in 2020 by [Federico Jaureguialzo][fedejaure].

[fedejaure]: https://github.com/fedejaure
