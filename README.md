# Development Setup

<div align="center">

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/fedejaure/dev-setup?logo=github)](https://github.com/fedejaure/dev-setup/releases)
[![Tests](https://github.com/fedejaure/dev-setup/workflows/tests/badge.svg)](https://github.com/fedejaure/dev-setup/actions?workflow=tests)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://opensource.org/licenses/MIT)

[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)

</div>

My own Ansible collection for development setup (use by your own risk).

* GitHub repo: <https://github.com/fedejaure/dev-setup.git>
* Free software: MIT

## Features

* TODO

## Quickstart

1. Ensure Apple's command line tools are installed (xcode-select --install to launch the installer).

2. Download this repository to your local drive.

3. Install requirements:
    b. Create a temporary virtualenv `/usr/bin/python3 -m venv .venv`.
    c. Active the virtualenv `. .venv/bin/activate`.
    d. Install ansible `pip3 install ansible`.

4. Install ansible requirements `ansible-galaxy install -r requirements.yml`.

5. Copy `inventory.example` into `inventory`.

6. Run `ansible-playbook main.yml --ask-become-pass`.


### Using a remote Host

1. (On the target Mac:) Go to System Preferences > Sharing.

2. Enable 'Remote Login'.

> You can also enable remote login on the command line:
> 
> ```
> sudo systemsetup -setremotelogin on
> ```

3. On the Host machine set the `inventory` file as:

```
[macos]
<ip address or hostname of the target mac> ansible_user=<target mac user> ansible_python_interpreter=/usr/bin/python3
```

### Overriding Defaults

You can override the defaults configured in default.<system-os>.config.yml by creating a <system-os>.config.yml file and setting the overrides in that file. e.g.:

```
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

## Author Information

This playbook was created in 2020 by [Federico Jaureguialzo][fedejaure].

[fedejaure]: https://github.com/fedejaure
