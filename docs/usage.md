# Usage Guide

This guide provides detailed instructions on how to set up and run the Ansible playbooks on
the differents supported targets.

## MacOS

!!! info "Ensure Apple's command line tools are installed"

    On a terminal launch the installer:
    ```console
    $ xcode-select --install
    ```

!!! warning "Agree Xcode's license"
    You need to agree to Xcode's license.

    ```console
    $ sudo xcodebuild -license
    ```

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

4. Install required Ansible roles:

    <!-- termynal -->

    ```console
    (dev-setup)$ ansible-galaxy install -r requirements.yml
    Starting galaxy role install process
    ...
    Starting galaxy collection install process
    ...
    fedejaure.dev_setup was installed successfully
    ```

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

6. Run the playbook:

    <!-- termynal -->

    ```console
    (dev-setup)$ ansible-playbook playbooks/main.yml --ask-become-pass -i inventory
    BECOME password[defaults to SSH password]:

    PLAY [Mac OSX Playbook] ***************************************************

    TASK [Gathering Facts] ****************************************************
    ok: [127.0.0.1]

    ...
    ```

### Starting from a configured machine (Configuring a remote one)

1. Clone this repository.

2. Install dependencies:

    <!-- termynal -->

    ```console
    $ poetry install --no-root
    Using python3.11 (3.11.11)
    Creating virtualenv .venv
    Installing dependencies from lock file

    Package operations: 97 installs, 0 updates, 0 removals

    ...
    ```

3. Activate the virtual environment:

    <!-- termynal -->

    ```console
    $ poetry shell
    Using python3.11 (3.11.11)
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

    !!! note "Enable 'Remote Login'"
        1. Go to System Preferences > Sharing.
        2. Enable 'Remote Login'.

        ??? tip "You can also enable remote login on the command line"

            <!-- termynal -->

            ```console
            $ sudo systemsetup -setremotelogin on
            ```

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

??? warning "Homebrew Cask Apps Failing with 'sudo'?"
    If you're installing Homebrew Cask apps on a **remote macOS machine** and encounter permission issues requiring `sudo`, a workaround is available — but **it's not recommended for general use**.

    You can try:

    - Defining `ansible_become_password` directly in your `inventory` file.
    - Reviewing [this related GitHub issue](https://github.com/geerlingguy/ansible-collection-mac/issues/102) for context and alternatives.

    ⚠️ This workaround is **only suggested if you're stuck** and working on a remote Mac. It is better to ensure proper local privilege escalation via `--ask-become-pass` whenever possible.


## Linux

!!! warning
    Linux support is in development and will be added in a future release.
