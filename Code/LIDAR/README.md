# Code LIDAR CDR 2025

Ce code permet de gérer les données que renvoie le LIDAR.

## Commencer avec ce projet

Ce projet utilise des [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) : ce sont en gros des répertoires Git dans des répertoires Git. Pour cloner ce projet, il y a alors plusieurs options.

Si vous êtes capables de cloner le répertoire via la ligne de commance, vous pouvez faire :

```console
git clone --recurse-submodules <url du projet>
```

Si vous avez téléchargé le code source dans un fichier `zip` ou une _tarball_, n'oubliez pas d'éxécuter la commande suivante une fois dans votre répertoire :

```console
git submodule update --init --recursive
```

Le `Makefile` inclut le _build_ du SDK, pas besoin donc de le construire séparément. Si vous voulez les projets exemples, ils sont disponibles dans `rplidar_sdk/app`, mais je vous conseille de faire `make` dans le répertoire `rplidar_sdk`. Lorsque vous lancez ces projets exemples, pensez à donner le [baudrate](#informations-essentielles-au-développement).

## Informations essentielles au développement

| Information | Valeur | Commentaire |
|---|---|---|
| Baudrate | 460800 | Marqué dans la datasheet mais les programmes d'exemple ne gèrent pas la valeur par défaut |

## Changelog

Pour plus de détails que marqué en-dessous, merci de regarder les commits et différentes branches.

### 17/11/24

Le boilerplate de base a été installé, ce qui nous permet de repartir sur de bonnes bases quand on vient aux erreurs. Le code d'exemple faisait pas mal d'assomptions sur les types `Result` (qu'il a lui-même introduit), donc j'ai enlevé ces assertions pour nous permettre de gérer _absolument tous_ les cas d'erreurs, et ainsi éviter un crash du robot en pleine CDR.

Un `Makefile` a aussi été mis en place pour permettre une compilation efficace du projet. Pensez à le modifier en conséquence si vous rajoutez des fichiers. Pour compiler le projet en mode `DEBUG`:

```console
make DEBUG=1
```
