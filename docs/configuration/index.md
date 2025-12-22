# Configuration Overview

The playbooks comes with a set of default configuration values that you can customize to suit your
specific environment. These defaults are defined in the `default.<target-os>.config.yml` file,
and you can override them by creating a `<target-os>.config.yml` file in your project and
specifying your custom values.

## Defaults

Below is a list of the key default variables available in `default.macos.config.yml` and what they control. You can override any of these by creating your own configuration file.

### Homebrew Configuration

- `homebrew_prefix`: The base path for Homebrew installation, determined by system architecture.

    !!! info "Default"

        `"/opt/homebrew"` (for **ARM**) or `"/usr/local"` (for **x86**)

- `homebrew_install_path`: Full path where Homebrew is installed.

    !!! info "Default"

        ```yaml
        "{homebrew_prefix}/Homebrew"
        ```

- `homebrew_brew_bin_path`: Location of Homebrew's binary files (`bin`).

    !!! info "Default"

        ```yaml
        "{homebrew_prefix}/bin"
        ```

- `homebrew_brew_sbin_path`: Location of Homebrew's superuser binary files (`sbin`).

    !!! info "Default"

        ```yaml
        "{homebrew_prefix}/sbin"
        ```

- `homebrew_taps`: List of additional Homebrew taps to add (repositories for formulas and casks).

    !!! info "Default"

        ```yaml
        ["esolitos/ipa"]
        ```

- `homebrew_installed_packages`: List of packages to install via Homebrew.

    !!! info "Default"

        ```yaml
        - git
        - openssl
        - readline
        - xz
        - sqlite
        - gcc
        - cmake
        - zlib
        - tcl-tk
        - dockutil
        - pipx
        - luarocks
        - neovim
        - tmux
        - chezmoi
        - jesseduffield/lazydocker/lazydocker
        - sshpass
        - htop
        - dust
        - duf
        - bat
        - fish
        - starship
        - btop
        ```

- `homebrew_cask_appdir`: Directory where cask applications will be installed.

    !!! info "Default"

        ```yaml
        "/Applications"
        ```

- `homebrew_cask_apps`: List of GUI applications to install via Homebrew Cask.

    !!! info "Default"

        ```yaml
        - firefox
        - google-chrome
        - docker
        - openvpn-connect
        - visual-studio-code
        - font-terminess-ttf-nerd-font
        - font-ubuntu-nerd-font
        - font-ubuntu-mono-nerd-font
        - font-xkcd
        - font-xkcd-script
        - zoom
        - tad
        - keybase
        - obsidian
        - ultimaker-cura
        - elgato-stream-deck
        - spotify
        - alacritty
        - discord
        ```

- `configure_homebrew_bin_rc_path`: Adds Homebrew binary (`bin`) path to the shell configuration.

    !!! info "Default"

        ```yaml
        true
        ```

- `configure_homebrew_sbin_rc_path`: Adds Homebrew superuser binary (`sbin`) path to the shell
configuration.

    !!! info "Default"

        ```yaml
        true
        ```

### Mac App Store (MAS) Configuration

- `mas_email`: Email used to authenticate with the Mac App Store for installing apps.

    !!! warning "Required"

        You should add your mas email in order to use this feature.

- `mas_installed_apps`: List of applications to install from the Mac App Store, defined by their app IDs.

    !!! info "Default"

        ```yaml
        - id: 497799835
          name: "Xcode"
        - id: 803453959
          name: "Slack"
        - id: 310633997
          name: "WhatsApp"
        - id: 747648890
          name: "Telegram"
        ```

### Dock Configuration

- `configure_dock`: Enables or disables dock configuration tasks.

    !!! info "Default"

        ```yaml
        true
        ```

- `dockutil_install`: If `true`, installs `dockutil`, a command-line utility for configuring the macOS Dock.

    !!! info "Default"

        ```yaml
        false
        ```

- `dockitems_remove`: List of applications to remove from the Dock.

    !!! info "Default"

        ```yaml
        - Safari
        - Messages
        - Mail
        - Photos
        - FaceTime
        - TV
        - Music
        - Podcasts
        - Keynote
        - Numbers
        - Pages
        ```

- `dockitems_persist`: Applications to add or pin to the Dock, with specific positions.

    !!! info "Default"

        ```yaml
        - name: "Firefox"
          path: "/Applications/Firefox.app/"
          pos: 2
        - name: "Google Chrome"
          path: "/Applications/Google Chrome.app/"
          pos: 3
        - name: "Terminal"
          path: "/Applications/Utilities/Terminal.app/"
          pos: 4
        - name: "Visual Studio Code"
          path: "/Applications/Visual Studio Code.app/"
          pos: 5
        ```

### pyenv Configuration

- `pyenv_configure_rc_path`: If `true`, configures `pyenv` to be added to shell initialization
files (like `.zshrc`).

    !!! info "Default"

        ```yaml
        true
        ```

### pipx Configuration

- `pipx_installed_packages`: List of Python applications to install via `pipx`. Supports injecting additional
packages into some applications.

    !!! info "Default"

        ```yaml
        - cookiecutter
        - pipenv
        - name: poetry
          inject_packages:
            - poetry-plugin-export
        - name: nox
          inject_packages:
            - nox-poetry
        - uv
        ```

- `configure_pipx_bin_rc_path`: Adds the `pipx` installation path to the shell configuration.

    !!! info "Default"

        ```yaml
        true
        ```

## Overriding Defaults

You can override the defaults configured in `default.<target-os>.config.yml` by creating
a `<target-os>.config.yml` file and setting the overrides in that file. e.g.:

!!! warning "Example `macos.config.yml`"

    Below is an example of a custom configuration file for macOS. In this case, we're configuring
    the Mac App Store email, overriding the list of Homebrew-installed packages, and specifying
    custom versions of Python via `pyenv`:

    ```yaml
    ---
    mas_email: "example@example.com"

    homebrew_installed_packages:
      - git
      - openssl
      - readline
      - xz
      - sqlite
      - gcc
      - cmake
      - zlib
      - tcl-tk
      - dockutil
      - pipx
      - luarocks
      - neovim
      - tmux
      - chezmoi
      - "jesseduffield/lazydocker/lazydocker"
      - sshpass
      - htop
      - dust
      - duf
      - bat
      - fish
      - starship
      - btop
      - awscli
      - tfenv
      - ffmpeg

    homebrew_cask_apps:
      - firefox
      - google-chrome
      - docker
      - openvpn-connect
      - font-terminess-ttf-nerd-font
      - font-ubuntu-nerd-font
      - font-ubuntu-mono-nerd-font
      - font-xkcd
      - font-xkcd-script
      - visual-studio-code
      - zoom
      - tad
      - keybase
      - obsidian
      - google-cloud-sdk
      - ultimaker-cura
      - elgato-stream-deck
      - spotify
      - alacritty
      - discord
      - inkscape

    pyenv_python_versions:
      - 3.11.14
      - 3.12.12
      - 3.13.11
      - 3.14.2
    ```

!!! tip "Advanced Role Configuration"

    For detailed configurations specific to each role, check the sections on
    [Third-party Roles](third_party_roles.md) and [First-party Roles](first_party_roles/index.md).

By customizing these configurations, you can fine-tune the behavior of the playbook and optimize it for your specific setup.
