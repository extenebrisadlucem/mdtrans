mdtrans
==========

## Table des matières
- [Introduction](#Introduction)  
- [Sponsors](#Sponsors)  
- [Documentation](#documentation)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
    - [Paramètres](#paramètres)
- [Garanties de sécurité](#garanties-de-sécurité)
  - [Limites de sécurité](#limites-de-sécurité)
  - [Responsabilités légales](#responsabilités-légales)
- [Versions](#versions)
- [Licence](#licence)

---

&nbsp;

[Français](README.FR.md), [English](../README.md), [Español](README.ES.md), [German](README.DE.md), [Dutch](README.NL.md), [简体中文](README.CN.md) , [繁體中文](README.TW.md) , [日本語](README.JP.md)


# Introduction

`mdtrans` est un outil léger pour traduire des fichiers Markdown tout en préservant la structure, les blocs de code, les tableaux, et les tokens spéciaux.  
Le programme utilise LibreTranslate pour effectuer la traduction et protège les segments sensibles via des tokens afin de maintenir l'intégrité du Markdown.

---

## Sponsors
Ce projet est communautaire.  
Si vous le trouvez utile et souhaitez contribuer à son développement, pensez à :
-  :beers: [Support via PayPal](https://www.paypal.com/donate/?hosted_button_id=59CQFU7TNSWP2)
-  Soumettre vos remarques et bugs
-  Partager avec vos collègues ou amis

[<img src="../assets/don_paypal.png" width="50"/>](../assets/don_paypal.png)  


---

# Documentation

## Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/ton-compte/mdtrans.git
cd mdtrans
```

2. Installer les dépendances (exemple pour Python) :

```bash
pip install -r requirements.txt
```

3. S'assurer que LibreTranslate est accessible, soit en local, soit via un serveur distant.
Vous pouvez l'installer à l'aide de podman ou docker
```bash
podman search LibreTranslate
podman run -it -p 5000:5000  --host 0.0.0.0 libretranslate/libretranslate
# Si vous voulez y accéder via un autre port, changez le premier 5000 ...
# P.ex.: ... -p 5005:5000 ...
```

## Utilisation

Lancer le script principal avec les paramètres nécessaires :

```bash
python src/mdtrans.py --source fr --target en --o README.md  --api http://localhost:5000/translate doc/README.fr.md 
```

### Paramètres

* `--source / -s` : Langue source du Markdown (`fr`, `en`, etc.)
* `--target / -t` : Langue cible (`en`, `fr`, etc.)
* `--output / -o` : Chemin du fichier traduit
* `--api`         : URL de l’instance LibreTranslate
* `--api_key`     : (optionnel) clé API si nécessaire
* `--noref / -n`  : Pas de lien sous votre texte
* `inputfile.md`  : Le dernier paramètre doit être le fichier à traduire
---

# Garanties de sécurité

`mdtrans` ne stocke aucun contenu sensible et n'exécute aucun code présent dans les fichiers Markdown. Tous les blocs de code et tokens spéciaux sont protégés pour éviter toute altération.

## Limites de sécurité

* La traduction repose sur LibreTranslate ; aucun contrôle n’est effectué sur les phrases traduites.
* Les tokens sont générés localement et préservent la structure Markdown, mais des erreurs de traduction peuvent modifier ponctuation et retours à la ligne.

## Responsabilités légales

L’utilisateur est responsable des fichiers traduits et de leur diffusion.
Aucun droit n’est revendiqué sur les fichiers traités ou sur le contenu original.

---

# Versions

Voir [CHANGELOG.md](../changelog.md) pour l'historique des versions.

# Licence

CC-BY-NC-SA -> [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Licence Creative Commons" style="border-width:0" src="../assets/Cc-by-nc-sa_icon.png" /></a>

<br><br><br><sub>Translated by [mdtrans](https://github.com/extenebrisadlucem/mdtrans)/[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate.git)</sub>
<sub><small>ON7AUR - CC-BY-NC-SA ®</small></sub>
