mdtrans
=======

## Contents
- [Introduction](#introduction)  
  - [Sponsors](#sponsors)  
- [Documentation](#documentation)
  - [Installation](#installation)
  - [Usage](#use)
    - [Settings](#settings)
- [Security guarantees](#security-guarantees)
  - [Safety limits](#safety-limits)
  - [Legal Responsibilities](#legal-responsibilities)
- [Versions](#versions)
- [License](#license)

---

[Français](doc/README.FR.md) , [English](README.md) , [Español](doc/README.ES.md) , [German](doc/README.DE.md) , [Dutch](doc/README.NL.md) , [简体中文](doc/README.CN.md) , [繁體中文](doc/README.TW.md) , [日本語](doc/README.JP.md)


# Introduction

`mdtrans`is a lightweight tool to translate Markdown files while preserving structure, code blocks, tables, and special tokens.
The program uses FreeTranslate to perform translation and protects sensitive segments via tokens to maintain the integrity of the Markdown.

---

## Sponsors
This project is community based.
If you find it useful and wish to contribute to its development, consider:
-:beers: [Support via PayPal](https://www.paypal.com/donate/?hosted_button_id=59CQFU7TNSWP2)
- Submit your comments and bugs
- Share with your colleagues or friends

[<img src="assets/don_paypal.png" width="50"/>](assets/don_paypal.png)  


---

# Documentation

## Installation

1. Close repository:
```bash
git clone https://github.com/ton-compte/mdtrans.git
cd mdtrans
```

2. Install dependencies (e.g. Python):

```bash
pip install -r requirements.txt
```

3. Ensure that LibreTranslate is accessible, either locally or via a remote server.
You can install it with podman or docker
```bash
podman search LibreTranslate
podman run -it -p 5000:5000  --host 0.0.0.0 libretranslate/libretranslate
# If you want to run it on another port, change the first 5000 ...
# I.e.: ... -p 5005:5000 ...
```

## Use

Lancer the main script with the necessary parameters:

```bash
python src/mdtrans.py --source fr --target en --o README.md  --api http://localhost:5000/translate doc/README.fr.md 
```

### Settings

* `--source / -s`: Source language of the Markdown (`fr`,`en`, etc.)
* `--target / -t`: Target language (`en`,`fr`, etc.)
* `--output / -o`: Path to translated file
* `--api`        : FreeTranslate instance URL
* `--api_key`    : (optional) API key if necessary
* `--noref / -n` : No links under your text.
* `inputfile.md` : The last parameter must be the file to translate
---

# Security guarantees

`mdtrans`does not store any sensitive content and does not execute any code present in Markdown files. All special code blocks and tokens are protected to avoid any alteration.

## Safety limits

* Translation is based on FreeTranslation; No checks are carried out on translated sentences.
* Tokens are generated locally and preserve the Markdown structure, but translation errors can change punctuation and return to line.

## Legal Responsibilities

User is responsible for the translated files and their dissemination.
No rights are claimed on the processed files or on the original content.

---

# Versions

[CHANGELOG.md](changelog.md) for version history.

# License

CC-BY-NC-SA ->[https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Licence Creative Commons" style="border-width:0" src="assets/Cc-by-nc-sa_icon.png" /></a>

<br><br><br><sub>Translated by [mdtrans](https://github.com/extenebrisadlucem/mdtrans)/[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate.git)</sub>
<sub><small>ON7AUR - CC-BY-NC-SA ®</small></sub>
