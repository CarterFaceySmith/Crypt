<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<img src="https://user-images.githubusercontent.com/43100930/193440676-8f3970d0-4272-462f-8d72-f33969fd1646.gif" width="350" height="350" />
  
<h3 align="center">The Crypt</h3>

  <p align="center">
    An opensource, enCRYPTed peer-to-peer command line chat.
    <br />
    <a href="https://github.com/carterfaceysmith/Crypt"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/carterfaceysmith/Crypt/issues">Report Bug</a>
    ·
    <a href="https://github.com/carterfaceysmith/Crypt/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

After reading more into encryption and RSA, I was inspired to write up a lightweight CLI chat for use locally. Python itself makes this suprisingly easy, I'm generally not the biggest fan of the language but it definitely has its merits here.

The program can be run as a server or client instance, the server instance will bind to your IP and base itself there, meaning anyone running on the local network is able to connect if authentication is passed. Users outside the network can connect as long as you've set up port forwarding and your public IP access configuration.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
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

The program will prompt you to choose whether to run as client or server, and issue you some security warnings prior to confirm if running server.

Please ensure you take necessary network measures to secure yourself if running publically.

### Prerequisites

* npm
  ```npm install npm@latest -g```

* poetry
```npm install poetry@latest```

* cryptography module
```pip install cryptography```

Note that the project relies on cryptography for security and hashing, if you install via poetry or npm it should install this dependency for you.

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- Migrate Crypt to asymmetric encryption
- Potentially migrate Crypt to a Flask-based web interface, or give the option
- Move from RSA-based encryption to something more secure like AES, this could be semi-overkill though

See the [open issues](https://github.com/carterfaceysmith/Crypt/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you want to add something, let me know or feel free to contribute to this, it's a super simple and lightweight project and the aim is to keep it that way.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

</br>
</br>

Godspeed.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/carterfaceysmith/Crypt.svg?style=for-the-badge
[contributors-url]: https://github.com/carterfaceysmith/Crypt/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/carterfaceysmith/Crypt.svg?style=for-the-badge
[forks-url]: https://github.com/carterfaceysmith/Crypt/network/members
[stars-shield]: https://img.shields.io/github/stars/carterfaceysmith/Crypt.svg?style=for-the-badge
[stars-url]: https://github.com/carterfaceysmith/Crypt/stargazers
[issues-shield]: https://img.shields.io/github/issues/carterfaceysmith/Crypt.svg?style=for-the-badge
[issues-url]: https://github.com/carterfaceysmith/Crypt/issues
[license-shield]: https://img.shields.io/github/license/carterfaceysmith/Crypt.svg?style=for-the-badge
[license-url]: https://github.com/carterfaceysmith/Crypt/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png

