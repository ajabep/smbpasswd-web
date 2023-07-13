# smbpasswd-web-light


**STILL IN DEVELOPMENT; DO NOT USE IT FOR NOW**


## What is it?

More than only "inspired" by [`smbpasswd-web`](https://github.com/Gurkengewuerz/smbpasswd-web), this project aims to be
a web interface to let users change their password on a remote SMB/CIFS server. Same shit as the previous project: "no
user adding, no machine account, nothing, plain simple changing a password", to make users autonomous.

The goal of this project is really to make users fully autonomous:

* No actions from the
administrator (as the stuff with token of the original project) is needed. It's also just a silly and light container to
run.
* Usage of a web browser is the ONLY requirement for users.

It's also extensible: it exposes an API.

It tries to be as safe as possible, thus, if you find a security vulnerability, do not hesitate to report it to me, and
we will see, depending on the criticism of the finding, how may I give you a reward. #BugBounty


## Sneak peek

The UI is silly and simple: just fields, nothing else. Colors are adapted to the color-scheme's device preference.

![UI is light when the user displays their device with a light color scheme.](./docs/light.png)

![UI is dark when the user displays their device with a dark color scheme.](./docs/dark.png)

There are also some small user-side checks.

![When the password mismatches its confirmation, the user is not able to submit the form.](./docs/password_mismatch.png)

Also, error messages are displayed with details.

![Error messages during an authentication failure.](./docs/authn_failure.png)

![Success message when the password has been correctly changed.](./docs/success.png)


## How it works?

When a user needs to change his password, the user accesses the website and changes its password. Done. That's all.


## Installation

To install this software, you have to use the container. To install the container, here are the instructions:

1. Pull the docker image [`ghcr.io/ajabep/smbpasswd-web-light:main`](https://ghcr.io/ajabep/smbpasswd-web-light:main);
2. The container has to be linked to the SMB server;
3. The environment variables are to are the following.
 - `REMOTE`: (string; an IP or a domain name) The address of the remote SMB server;
 - `VERBOSE`: (Optional; positive integer) When used, the logs will be verbose;


The application files are putted in the `/app` directory.

Logs are available on the STDOUT.


## TODO

Check issues and fix some of them!


## License

*smbpasswd-web-light* is released under the Unlicensed license. See the [./LICENSE](LICENSE) file.

Based on the idea (and not only the idea) of [`Gurkengewuerz's smbpasswd-web`](https://github.com/Gurkengewuerz/smbpasswd-web); App icon by [icons8](https://icons8.com/).
