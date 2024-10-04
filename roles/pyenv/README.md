# pyenv

This Ansible role automates the installation and configuration of [pyenv](https://github.com/pyenv/pyenv) on macOS.
`pyenv` is a popular tool that allows you to easily switch between multiple versions of Python. The role handles the installation of `pyenv`,
required packages, multiple Python versions, and the configuration of shell environment files for `pyenv` to work seamlessly.

# Requirements

- **macOS**: This role is specifically designed for macOS systems.
    - **Homebrew**: Homebrew must be pre-installed on the target machine before running this role.

# Role Variables

This role provides several variables for configuration. Below are the key variables that can be set, including default values from `defaults/main.yml`:

- `pyenv_root`: (Default: `"{{ ansible_env.HOME }}/.pyenv"`)
  The directory where pyenv will be installed.

- `pyenv_python_versions`: (Default: `[3.9, 3.10, 3.11, 3.12]`)
  A list of Python versions to be installed by pyenv.

- `pyenv_update`: (Default: `false`)
  If set to `true`, this option will trigger an update of the pyenv interpreter list.

- `pyenv_configure_rc_path`: (Default: `false`)
  If `true`, the role will configure the shell environment by adding pyenv to the user's rc file (`~/.zshrc` by default).

# Dependencies

This role relies on the following Ansible collections and roles:

- **community.general**: Specifically for the `homebrew` module, which is used to install pyenv dependencies on macOS.

## Example Playbook

Below is an example playbook that demonstrates how to use this role to install pyenv and configure it with multiple Python versions:

```yaml
- name: Example playbook
  hosts: example_target
  roles:
    - role: fedejaure.dev_setup.pyenv
      vars:
        pyenv_update: true
        pyenv_configure_rc_path: true
```

## License

MIT

## Author Information

This role was created in 2020 by [Federico Jaureguialzo][fedejaure].

[fedejaure]: https://github.com/fedejaure
