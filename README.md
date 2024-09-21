# Development Setup

<div markdown="span" align="center">

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

### Mac OS

- [x] Applications installed with Mac App Store.
- [x] Applications installed with Homebrew Cask.
- [x] Tools/Package installed with Homebrew.
- [x] Tools installed with pipx.

### Linux

Comming soon ...

## Quickstart

### Starting from a brand-new machine.

1. Download this repository to your local drive.

3. Install requirements:

    Create a temporary virtualenv, activate the virtualenv and install ansible:

    <!-- termynal -->

    ```console
    $ /usr/bin/python3 -m venv .venv
    $ . .venv/bin/activate
    (.venv)$ pip3 install ansible
    ---> 100%
    Installed
    ```

4. Install ansible requirements `ansible-galaxy install -r requirements.yml`.

5. Copy `inventory.example` into `inventory` and set the desired `<target-os>` (`macos`):

    ```ini
    [<target-os>]
    127.0.0.1 ansible_connection=local ansible_python_interpreter=/usr/bin/python3
    ```

    to e.g.:

    ```ini
    [macos]
    127.0.0.1 ansible_connection=local ansible_python_interpreter=/usr/bin/python3
    ```

6. Run `ansible-playbook playbooks/main.yml --ask-become-pass -i inventory`.

    > On a target Mac:
    >
    > 1. Ensure Apple's command line tools are installed (`xcode-select --install` to launch the installer).
    >
    >   > Note: You need to agree to Xcode's license.
    >   >
    >   > ```console
    >   > $ sudo xcodebuild -license
    >   > ```

### Starting from a configured machine (Configuring a remote one)

1. Clone this repository.

2. Install dependencies:

    <!-- termynal -->

    ```console
    $ poetry install --no-root
    Using python3.10 (3.10.8)
    Creating virtualenv .venv
    Installing dependencies from lock file

    Package operations: 97 installs, 0 updates, 0 removals

    ...
    ```

3. Activate the virtual environment:

    <!-- termynal -->

    ```console
    $ poetry shell
    Using python3.10 (3.10.8)
    Spawning shell within .venv
    (dev-setup)$
    ```

4. Install required Ansible roles:

    <!-- termynal -->

    ```console
    (dev-setup)$ inv galaxy-install
    Starting galaxy role install process
    ...
    Starting galaxy collection install process
    ...
    fedejaure.dev_setup was installed successfully
    ```

5. Configure the `inventory` file and set the desired `<target-os>` (`macos`):

    ```ini
    [<target-os>]
    <ip address or hostname of the target> ansible_user=<target user> ansible_python_interpreter=/usr/bin/python3
    ```

    > On a target Mac:
    >
    > 1. Ensure Apple's command line tools are installed (`xcode-select --install` to launch the installer).
    >
    > 2. Go to System Preferences > Sharing.
    >
    > 3. Enable 'Remote Login'.
    >
    >   > You can also enable remote login on the command line:
    >   >
    >   > ```console
    >   > $ sudo systemsetup -setremotelogin on
    >   > ```
    >
    >   > Note: You need to agree to Xcode's license.
    >   >
    >   > ```console
    >   > $ sudo xcodebuild -license
    >   > ```

6. Run the playbook:

    <!-- termynal -->

    ```console
    (dev-setup)$ inv playbook --ask-pass --ask-become-pass
    SSH password:
    BECOME password[defaults to SSH password]:

    PLAY [Mac OSX Playbook] ***************************************************

    TASK [Gathering Facts] ****************************************************
    ok: [127.0.0.1]

    ...
    ```

## Author Information

This playbook was created in 2020 by [Federico Jaureguialzo][fedejaure].

[fedejaure]: https://github.com/fedejaure
