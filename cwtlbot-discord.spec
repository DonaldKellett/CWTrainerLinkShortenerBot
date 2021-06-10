%global appname cwtlbot-discord
%global version 0.1.1

Name: %{appname}
Version: %{version}
Release: 1%{?dist}
Summary: Codewars Trainer Link Bot for Discord
License: AGPLv3+
URL: https://github.com/DonaldKellett/%{appname}
Source0: https://github.com/DonaldKellett/%{appname}/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch
Requires: nodejs

%description
A Discord bot for detecting links to the Codewars trainer and converting them
to direct Kata links.

%prep
%setup -q

%install
mkdir -p %{buildroot}/%{_datadir}/%{appname}
cp package.json %{buildroot}/%{_datadir}/%{appname}/package.json
cp package-lock.json %{buildroot}/%{_datadir}/%{appname}/package-lock.json
cp index.js %{buildroot}/%{_datadir}/%{appname}/index.js
cp README.md %{buildroot}/%{_datadir}/%{appname}/README.md
cp LICENSE %{buildroot}/%{_datadir}/%{appname}/LICENSE
mkdir -p %{buildroot}/%{_sysconfdir}/%{appname}
echo YOUR_BOT_LOGIN_TOKEN_HERE > %{buildroot}/%{_sysconfdir}/%{appname}/token
chmod 600 %{buildroot}/%{_sysconfdir}/%{appname}/token
echo YOUR_BOT_USERNAME_HERE > %{buildroot}/%{_sysconfdir}/%{appname}/username
cat > %{appname}.sh << EOF
#!/bin/bash

if [[ \$# -gt 1 ]]; then
  echo "On first usage:"
  echo ""
  echo "\$ sudo su -"
  echo "# %{appname} --init"
  echo "# exit"
  echo ""
  echo "Thereafter:"
  echo "- \$ sudo %{appname}"
  echo "- \$ %{appname} --version"
  exit 1
fi

if [[ \$# -eq 0 ]]; then
  if [[ "\$(whoami)" != root ]]; then
    echo "Fatal error: %{appname} must be run as root when no option is specified"
    exit 1
  fi
  cd %{_datadir}/%{appname}
  CONFIG_PATH=%{_sysconfdir}/%{appname} npm start
  exit
fi

if [[ "\$1" = --init ]]; then
  if [[ "\$(whoami)" != root ]]; then
    echo "Fatal error: %{appname} must be run as root when the --init option is specified"
    exit 1
  fi
  echo -n "Enter the login token for your Discord bot: "
  IFS= read -r token
  echo "\$token" > %{_sysconfdir}/%{appname}/token
  echo -n "Enter the username for your Discord bot: "
  IFS= read -r username
  echo "\$username" > %{_sysconfdir}/%{appname}/username
  cd %{_datadir}/%{appname}
  npm install
  exit
fi

if [[ "\$1" == --version ]]; then
  echo "%{version}"
  exit
fi

echo "On first usage:"
echo ""
echo "\$ sudo su -"
echo "# %{appname} --init"
echo "# exit"
echo ""
echo "Thereafter:"
echo "- \$ sudo %{appname}"
echo "- \$ %{appname} --version"
exit 1
EOF
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{appname}.sh %{buildroot}/%{_bindir}/%{appname}
cat > %{appname}.service << EOF
[Unit]
Description=Codewars Trainer Link Bot for Discord
Documentation=https://github.com/DonaldKellett/%{appname}

[Service]
Type=simple
ExecStart=%{_bindir}/%{appname}

[Install]
WantedBy=multi-user.target
EOF
mkdir -p %{buildroot}/usr/lib/systemd/system
cp %{appname}.service %{buildroot}/usr/lib/systemd/system/%{appname}.service

%files
%{_datadir}/%{appname}/package.json
%{_datadir}/%{appname}/package-lock.json
%{_datadir}/%{appname}/index.js
%doc %{_datadir}/%{appname}/README.md
%license %{_datadir}/%{appname}/LICENSE
%config(noreplace) %{_sysconfdir}/%{appname}/token
%config(noreplace) %{_sysconfdir}/%{appname}/username
%{_bindir}/%{appname}
/usr/lib/systemd/system/%{appname}.service

%changelog
* Thu Jun 10 2021 Donald Sebastian Leung <donaldsebleung@gmail.com> - 0.1.1-1
- Reduce verbosity of bot by disabling link preview
* Wed Jun 9 2021 Donald Sebastian Leung <donaldsebleung@gmail.com> - 0.1.0-1
- Initial app release
