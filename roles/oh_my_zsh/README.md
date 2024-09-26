# oh-my-zsh

This Ansible role automates the installation and configuration of [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) on macOS.
`Oh My Zsh` is an open-source framework for managing Zsh configurations. This role handles the installation of `Oh My Zsh`,
required packages, and the configuration of the user's shell environment to work seamlessly with `Oh My Zsh`.

# Requirements

- **macOS**: This role is specifically designed for macOS systems.
    - **Homebrew**: Homebrew must be pre-installed on the target machine before running this role.

# Role Variables

This role provides a few key variables for configuration. Below are the variables that can be set, including default values from `defaults/main.yml`:

- `oh_my_zsh_root`: (Default: `"{{ ansible_env.HOME }}/.oh-my-zsh"`)
  The directory where Oh My Zsh will be installed.

# Dependencies

This role relies on the following Ansible collections and roles:

- **community.general**: Specifically for the `homebrew` module, which is used to install required dependencies on macOS.

## Example Playbook

Below is an example playbook that demonstrates how to use this role to install Oh My Zsh:

```yaml
- name: Example playbook
  hosts: example_target
  roles:
    - role: fedejaure.dev_setup.oh_my_zsh
```

## License

MIT

## Author Information

This role was created in 2020 by [Federico Jaureguialzo][fedejaure].

[fedejaure]: https://github.com/fedejaure
