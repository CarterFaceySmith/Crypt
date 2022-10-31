<h3 align="center">The Crypt</h3>

<p align="center">
  Encrypted P2P CLI chat.
</p>

## About The Project

After reading more into encryption and RSA, I was inspired to write up a lightweight CLI chat for use locally. Python itself makes this suprisingly easy, I'm generally not the biggest fan of the language but it definitely has its merits here.

The program can be run as a server or client instance, the server instance will bind to your IP and base itself there, meaning anyone running on the local network is able to connect if authentication is passed. Users outside the network can connect as long as you've set up port forwarding and your public IP access configuration.

### Built With

* Python

## Getting Started

To get started, you can initialise the project from npm, poetry or this repo.

### NPM
1. Run ```npm install @carterfaceysmith/thecrypt```
2. Run the code via ```python main.py```

### Poetry
1. Run ```poetry install theCrypt```
2. Run the code via ```poetry crypt```

### GitHub
1. Clone this repository
2. In the cloned directory run ```python main.py```

The program will prompt you to choose whether to run as client or server, and issue you some security warnings prior to confirmation if running server.

Please ensure you take necessary network measures to secure yourself if running publically, the server will expose your IP if you choose to do so.

### Prerequisites

* npm
  ```npm install npm@latest -g```

* poetry
```npm install poetry@latest```

* cryptography module
```pip install cryptography```

Note that the project relies on cryptography for security and hashing, if you install via poetry or npm it should install this dependency for you.

## Roadmap

- Migrate Crypt to asymmetric encryption
- Potentially migrate Crypt to a Flask-based web interface, or give the option
- Move from RSA-based encryption to something more secure like AES, this could be semi-overkill though

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

</br>
</br>

Godspeed.
