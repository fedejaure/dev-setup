# Third-party Roles

This playbook uses several third-party roles to streamline macOS configuration. Below is a list of
the third-party roles used, along with a brief description of their functionality, links to their
GitHub repositories, and docs.

## [elliotweiser.osx-command-line-tools](https://github.com/elliotweiser/ansible-osx-command-line-tools)

- **Purpose**: Installs the macOS command line tools, which provide essential utilities and compilers (like `git`, `clang`, etc.) needed for many software development tasks.
- **Why it's needed**: Many tools, including Homebrew, require these command-line utilities to function correctly.
- **Configuration**: [documentation](https://github.com/elliotweiser/ansible-osx-command-line-tools)

## Roles from the [geerlingguy.mac](https://github.com/geerlingguy/ansible-collection-mac) collection

### geerlingguy.mac.homebrew

- **Purpose**: Manages the installation and configuration of Homebrew, a popular package manager for macOS.
- **Why it's needed**: This role ensures that Homebrew is installed and configured correctly, allowing you to manage packages and applications on macOS easily.
- **Configuration**: [documentation](https://github.com/geerlingguy/ansible-collection-mac/blob/master/roles/homebrew/)

### geerlingguy.mac.mas

- **Purpose**: Automates the installation of applications from the Mac App Store using `mas-cli`.
- **Why it's needed**: This role provides a streamlined way to install and manage Mac App Store applications through Ansible, without needing manual intervention.
- **Configuration**: [documentation](https://github.com/geerlingguy/ansible-collection-mac/blob/master/roles/mas/)

### geerlingguy.mac.dock

- **Purpose**: Configures the macOS Dock by adding, removing, or reordering applications.
- **Why it's needed**: This role allows you to customize the Dock layout to your preferences, making frequently used applications easily accessible.
- **Configuration**: [documentation](https://github.com/geerlingguy/ansible-collection-mac/blob/master/roles/dock/)

For more information on these roles, you can also explore their documentation on [Ansible Galaxy](https://galaxy.ansible.com/).
