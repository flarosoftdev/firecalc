import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


logging.info("Loading 'math' module...")
import math
logging.info("Loading 'random' module...")
import random
logging.info("Loading 're' module...")
import re
logging.info("Loading 'cmath' module...")
import cmath
logging.info("Loading 'datetime' module...")
import datetime
logging.info("Loading 'sympy' module...")
import sympy as sp
logging.info("Loading 'matplotlib.pyplot' module...")
import matplotlib.pyplot as plt
logging.info("Loading 'numpy' module...")
import numpy as np
logging.info("Loading 'telebot' module...")
import telebot
logging.info("Loading 'types' from 'telebot' module...")
from telebot import types
logging.info("Loading 'requests' module...")
import requests
logging.info("Loading 'time' module...")
import time
logging.info("Loading 'os' module...")
import os
logging.info("Loading 'sys' module...")
import sys
logging.info("Loading 'AI21Client' from 'ai21' module...")
from ai21 import AI21Client
logging.info("Loading 'ChatMessage', 'ResponseFormat' from 'ai21.models.chat' module...")
from ai21.models.chat import ChatMessage, ResponseFormat

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

messages = {
    "en": {
        "start": """👋🏻 Hello!

*I am a modern smart calculator*, designed to solve a wide range of mathematical problems.

My system is capable of *performing both elementary and complex analytical calculations*, providing *accurate* and *reasonable* solutions. 🧮

*Enter a mathematical expression or equation, and I will immediately perform the necessary calculations, providing you with a reliable solution!* 😉

👥 If you need a smart calculator in your group, just [add me](tg://resolve?domain=FireCalcTG_bot&startgroup=new), and I will be ready to work in no time! (Reply to my message with your expression, and I will solve it)""",
        "random_result": "Random number: *{}*",
        "currency": "Currency conversion",
        "temperature": "Temperature conversion",
        "result": "Result: *{}*",
        "error": "Error! 😞",
        "solve": "Solving equation: *{}*",
        "plot": "Graph plot generated: *{}*",
        "unknown_command": "Unknown command or format!",
        "error_invalid_expression": "Error: Invalid expression!",
        "error_invalid_currency": "Error: Invalid currency!",
        "error_invalid_temperature": "Error: Invalid temperature conversion!",
        "error_unknown_function": "Error: Unknown function!",
        "help": """*Available commands*:

1. `/start` - Start the bot and select a language.
2. `/help` - Show this help message.
3. `solve <equation>` - Solve a mathematical equation. Example: `solve x^2 - 5 * x + 6 = 0`
4. `plot <function>, <x_min>, <x_max>` - Plot a function on a given interval. Example: `plot x**3,-14,134` (sign ^ = **)
5. `random <min>, <max>` - Generate a random number between min and max. Example: `random 1, 100`
6. `convert_currency <amount> <from_currency> <to_currency>` - Convert currencies. Example: `convert_currency 100 USD EUR`. Please note: this function does not work yet, but the developer is already fixing this bug.
7. `kg_to_lb <kg>` - Convert kilograms to pounds. Example: `kg_to_lb(50)`
8. `lb_to_kg <pounds>` - Convert pounds to kilograms. Example: `lb_to_kg(110)`
9. `c_to_f <c>` - Convert Celsius to Fahrenheit. Example: `c_to_f(25)`
10. `f_to_c <f>` - Convert Fahrenheit to Celsius. Example: `f_to_c(77)`
11. `c_to_k <c>` - Convert Celsius to Kelvin. Example: `c_to_k(25)`
12. `k_to_c <k>` - Convert Kelvin to Celsius. Example: `k_to_c(298)`
13. `decide <problem>` - Solve a math word problem. Example: `decide Vanya and Petya together have 20 candies. Vanya has 4 more candies than Petya. How many candies does each of them have?`

*Note:* Use simple mathematical expressions such as `2 + 3 * 5` or `10 / 2` for calculations.

*Full documentation on how to use the bot*: https://telegra.ph/FireCalc--your-personal-math-assistant-in-Telegram-03-17

[Terms of Use](https://telegra.ph/FireCalc-Terms-of-Use-03-21)
""",
        "cleared": "*Cleared!* 🧹",
        "about": """*About the Bot and Its Developer*

*FireCalc* is designed to help users solve a wide range of tasks — *from simple mathematical calculations to generating random numbers, plotting graphs, and many other functions*. With an intuitive interface and quick response, it will become your reliable tool for effective interaction.

The bot supports several languages, including Russian and English. *Whether you need to solve a simple problem or perform more complex calculations, this bot is ready to help*.

*About the Developer*

This bot was created and is supported by *Flarosoft* — an independent developer who is passionate about programming and strives to create useful tools for others. Flarosoft's main goal is to make everyday tasks easier and more efficient for users around the world.

As an open source developer, Flarosoft strives to contribute to the tech community by creating accessible, customizable, and reliable software. If you enjoy using this bot, please feel free to *leave feedback* (@flarosoft) to help improve future versions.""",
"thinking": "I'm thinking...",
"decide_please": "Please enter the task after the 'decide' command."
    },
    "ru": {
        "start": """👋🏻 Здравствуйте!

*Я представляю собой современный интеллектуальный калькулятор*, разработанный для решения широкого спектра математических задач.

Моя система способна *выполнять как элементарные, так и сложные аналитические вычисления*, обеспечивая *точные* и *обоснованные* решения. 🧮

*Введите математическое выражение или уравнение, и я незамедлительно проведу необходимые вычисления, предоставив вам достоверное решение!* 😉

👥 Если вам нужен интеллектуальный калькулятор в вашей группе, просто [добавьте меня](tg://resolve?domain=FireCalcTG_bot&startgroup=new), и я сразу буду готов к работе! (Отправьте в ответ на моё сообщение ваше выражение, и я его решу).

📢 *Канал с новостями*: @flarosoftdev
""",
        "random_result": "Случайное число: *{}*",
        "currency": "Конвертация валют",
        "temperature": "Конвертация температуры",
        "result": "Результат: *{}*",
        "error": "Ошибка! 😞",
        "solve": "Решение уравнения: *{}*",
        "plot": "График построен: *{}*",
        "unknown_command": "Неизвестная команда или формат!",
        "error_invalid_expression": "Ошибка: Неверное выражение!",
        "error_invalid_currency": "Ошибка: Неверная валюта!",
        "error_invalid_temperature": "Ошибка: Неверная конвертация температуры!",
        "error_unknown_function": "Ошибка: Неизвестная функция!",
        "help": """
*Доступные команды*:

1. `/start` - Запустите бота и выберите язык.
2. `/help` - Показать это справочное сообщение.
3. `solve <уравнение>` - Решить математическое уравнение. Пример: `solve x^2 - 5 * x + 6 = 0`
4. `plot <функция>, <x_min>, <x_max>` - Построить график функции на заданном интервале. Пример: `plot x**3,-14,134`
5. `random <min>, <max>` - Сгенерировать случайное число между `min` и `max`. Пример: `random 1, 100`
6. `convert_currency <сумма> <из_валюта> <в_валюта>` - Конвертация валют. Пример: `convert_currency 100 USD EUR`. Обратите внимание: данная функция пока не работает, но разработчик уже исправляет данную ошибку.
7. `kg_to_lb <кг>` - Конвертировать килограммы в фунты. Пример: `kg_to_lb(50)`
8. `lb_to_kg <фунты>` - Конвертировать фунты в килограммы. Пример: `lb_to_kg(110)`
9. `c_to_f <c>` - Конвертировать Цельсий в Фаренгейт. Пример: `c_to_f(25)`
10. `f_to_c <f>` -  Конвертировать Фаренгейт в Цельсий. Пример: `f_to_c(77)`
11. `c_to_k <c>` - Конвертировать Цельсий в Кельвин. Пример: `c_to_k(25)`
12. `k_to_c <k>` -  Конвертировать Кельвин в Цельсий. Пример: `k_to_c(298)`
13. `decide <задача>` - Решить текстовую математическую задачу. Пример: `decide у Вани и Пети вместе 20 конфет. У Вани на 4 конфеты больше, чем у Пети. Сколько конфет у каждого из них?`

*Примечание*: Используйте простые математические выражения, например, `2 + 3 * 5` или `10 / 2` для вычислений.

*Полная документация по использованию бота*: https://telegra.ph/FireCalc--vash-lichnyj-matematicheskij-pomoshchnik-v-Telegram-03-17

▶️ *Видео на YouTbue с примером использования бота*: https://youtu.be/VkXxSuK5zVQ

[Условия использования](https://telegra.ph/Usloviya-ispolzovaniya-FireCalc-03-20)
    """, "cleared": "*Очищено!* 🧹",
        "about": """*О боте и его разработчике*

*FireCalc* создан для того, чтобы помогать пользователям решать широкий спектр задач — *от простых математических вычислений до генерации случайных чисел, построения графиков и многих других функций*. С интуитивно понятным интерфейсом и быстрым откликом, он станет вашим надежным инструментом для эффективного взаимодействия.

Бот поддерживает несколько языков, включая русский и английский. *Независимо от того, хотите ли вы решить простую задачу или выполнить более сложные вычисления, этот бот готов помочь*.

*О разработчике*

Этот бот был создан и поддерживается *Flarosoft* — независимым разработчиком, увлечённым программированием и стремящимся создавать полезные инструменты для других. Главная цель Flarosoft — сделать повседневные задачи более легкими и эффективными для пользователей по всему миру.

Как открытый разработчик, Flarosoft стремится внести вклад в техническое сообщество, создавая доступное, настраиваемое и надежное программное обеспечение. Если вам нравится использовать этот бот, не стесняйтесь *оставлять отзывы* (@flarosoft), чтобы помочь улучшить будущие версии.""",
"thinking": "Думаю...",
"decide_please": "Пожалуйста, введите задачу после команды 'decide'."
    },
    "de": {
        "start": """👋🏻 Hallo!

*Ich bin ein moderner smarter Rechner*, der entwickelt wurde, um eine breite Palette mathematischer Probleme zu lösen.

Mein System ist in der Lage, *sowohl elementare als auch komplexe analytische Berechnungen* durchzuführen und *genaue* und *vernünftige* Lösungen bereitzustellen. 🧮

*Geben Sie einen mathematischen Ausdruck oder eine Gleichung ein, und ich werde sofort die notwendigen Berechnungen durchführen und Ihnen eine zuverlässige Lösung bieten!* 😉

👥 Wenn Sie einen smarten Rechner in Ihrer Gruppe benötigen, fügen Sie mich einfach [hinzu](tg://resolve?domain=FireCalcTG_bot&startgroup=new), und ich werde in kürzester Zeit einsatzbereit sein! (Antworten Sie auf meine Nachricht mit Ihrem Ausdruck, und ich werde ihn lösen)""",
        "random_result": "Zufallszahl: *{}*",
        "currency": "Währungsumrechnung",
        "temperature": "Temperaturumrechnung",
        "result": "Ergebnis: *{}*",
        "error": "Fehler! 😞",
        "solve": "Gleichung lösen: *{}*",
        "plot": "Graph erzeugt: *{}*",
        "unknown_command": "Unbekannter Befehl oder Format!",
        "error_invalid_expression": "Fehler: Ungültiger Ausdruck!",
        "error_invalid_currency": "Fehler: Ungültige Währung!",
        "error_invalid_temperature": "Fehler: Ungültige Temperaturumrechnung!",
        "error_unknown_function": "Fehler: Unbekannte Funktion!",
        "help": """*Verfügbare Befehle*:

1. `/start` - Starten Sie den Bot und wählen Sie eine Sprache.
2. `/help` - Zeigen Sie diese Hilfemeldung an.
3. `solve <Gleichung>` - Lösen Sie eine mathematische Gleichung. Beispiel: `solve x^2 - 5 * x + 6 = 0`
4. `plot <Funktion>, <x_min>, <x_max>` - Zeichnen Sie eine Funktion in einem gegebenen Intervall. Beispiel: `plot x**3,-14,134` (Zeichen ^ = **)
5. `random <min>, <max>` - Erzeugen Sie eine Zufallszahl zwischen min und max. Beispiel: `random 1, 100`
6. `convert_currency <Betrag> <von_Währung> <zu_Währung>` - Währungsumrechnung. Beispiel: `convert_currency 100 USD EUR`. Bitte beachten Sie: Diese Funktion funktioniert noch nicht, aber der Entwickler behebt diesen Fehler bereits.
7. `kg_to_lb <kg>` - Kilogramm in Pfund umrechnen. Beispiel: `kg_to_lb(50)`
8. `lb_to_kg <Pfund>` - Pfund in Kilogramm umrechnen. Beispiel: `lb_to_kg(110)`
9. `c_to_f <c>` - Celsius in Fahrenheit umrechnen. Beispiel: `c_to_f(25)`
10. `f_to_c <f>` - Fahrenheit in Celsius umrechnen. Beispiel: `f_to_c(77)`
11. `c_to_k <c>` - Celsius in Kelvin umrechnen. Beispiel: `c_to_k(25)`
12. `k_to_c <k>` - Kelvin in Celsius umrechnen. Beispiel: `k_to_c(298)`
13. `decide <Problem>` – Lösen Sie ein mathematisches Textproblem. Beispiel: `decide dass Vanya und Petya zusammen 20 Bonbons haben. Vanya hat 4 Bonbons mehr als Petya. Wie viele Bonbons hat jeder von ihnen?`

*Hinweis*: Verwenden Sie einfache mathematische Ausdrücke wie `2 + 3 * 5` oder `10 / 2` für Berechnungen.

*Vollständige Dokumentation zur Verwendung des Bots (Englisch)*: https://telegra.ph/FireCalc--your-personal-math-assistant-in-Telegram-03-17

[Nutzungsbedingungen](https://telegra.ph/FireCalc-Terms-of-Use-03-21)
""",
        "cleared": "*Geklärt!* 🧹",
        "about": """*Über den Bot und seinen Entwickler*

*FireCalc* wurde entwickelt, um Benutzern zu helfen, eine Vielzahl von Aufgaben zu lösen — *von einfachen mathematischen Berechnungen bis hin zu Zufallszahlen, Graphen und vielen anderen Funktionen*. Mit einer benutzerfreundlichen Oberfläche und schneller Reaktionszeit wird es Ihr zuverlässiges Werkzeug für effektive Interaktion.

Der Bot unterstützt mehrere Sprachen, darunter Russisch und Englisch. *Egal, ob Sie ein einfaches Problem lösen oder komplexe Berechnungen durchführen möchten, dieser Bot ist bereit zu helfen*.

*Über den Entwickler*

Dieser Bot wurde von *Flarosoft* erstellt und unterstützt — einem unabhängigen Entwickler, der leidenschaftlich gerne programmiert und danach strebt, nützliche Werkzeuge für andere zu schaffen. Das Hauptziel von Flarosoft ist es, alltägliche Aufgaben für Benutzer weltweit einfacher und effizienter zu machen.

Als Open-Source-Entwickler strebt Flarosoft danach, der Tech-Community durch die Schaffung zugänglicher, anpassbarer und zuverlässiger Software beizutragen. Wenn Ihnen dieser Bot gefällt, hinterlassen Sie bitte *Feedback* (@flarosoft), um künftige Versionen zu verbessern.""",
"thinking": "Ich denke...",
"decide_please": "Bitte geben Sie die Aufgabe nach dem Befehl 'decide' ein."
    },
    "fr": {
        "start": """👋🏻 Bonjour!

*Je suis une calculatrice moderne et intelligente*, conçue pour résoudre un large éventail de problèmes mathématiques.

Mon système est capable de *réaliser des calculs élémentaires et analytiques complexes*, offrant des solutions *précises* et *raisonnées*. 🧮

*Entrez une expression ou une équation mathématique, et je réaliserai immédiatement les calculs nécessaires, en vous fournissant une solution fiable!* 😉

👥 Si vous avez besoin d'une calculatrice intelligente dans votre groupe, ajoutez-moi simplement [ici](tg://resolve?domain=FireCalcTG_bot&startgroup=new), et je serai prêt à travailler en un rien de temps! (Répondez à mon message avec votre expression, et je la résoudrai)""",
        "random_result": "Nombre aléatoire : *{}*",
        "currency": "Conversion de devises",
        "temperature": "Conversion de température",
        "result": "Résultat : *{}*",
        "error": "Erreur! 😞",
        "solve": "Résolution de l'équation : *{}*",
        "plot": "Graphique généré : *{}*",
        "unknown_command": "Commande ou format inconnu!",
        "error_invalid_expression": "Erreur : Expression invalide!",
        "error_invalid_currency": "Erreur : Devise invalide!",
        "error_invalid_temperature": "Erreur : Conversion de température invalide!",
        "error_unknown_function": "Erreur : Fonction inconnue!",
        "help": """*Commandes disponibles* :

1. `/start` - Démarrer le bot et choisir la langue.
2. `/help` - Afficher ce message d'aide.
3. `solve <équation>` - Résoudre une équation mathématique. Exemple : `solve x^2 - 5 * x + 6 = 0`
4. `plot <fonction>, <x_min>, <x_max>` - Tracer une fonction sur un intervalle donné. Exemple : `plot x**3,-14,134` (symbole ^ = **)
5. `random <min>, <max>` - Générer un nombre aléatoire entre min et max. Exemple : `random 1, 100`
6. `convert_currency <montant> <devise_à_partir> <devise_vers>` - Conversion de devises. Exemple : `convert_currency 100 USD EUR`. Remarque : cette fonction ne fonctionne pas encore, mais le développeur corrige déjà cette erreur.
7. `kg_to_lb <kg>` - Convertir les kilogrammes en livres. Exemple : `kg_to_lb(50)`
8. `lb_to_kg <livres>` - Convertir les livres en kilogrammes. Exemple : `lb_to_kg(110)`
9. `c_to_f <c>` - Convertir les Celsius en Fahrenheit. Exemple : `c_to_f(25)`
10. `f_to_c <f>` - Convertir les Fahrenheit en Celsius. Exemple : `f_to_c(77)`
11. `c_to_k <c>` - Convertir les Celsius en Kelvin. Exemple : `c_to_k(25)`
12. `k_to_c <k>` - Convertir les Kelvin en Celsius. Exemple : `k_to_c(298)`
13. `decide <problem>` - Résoudre un problème mathématique textuel. Exemple: `decide que Vanya et Petya ont ensemble 20 bonbons. Vanya a 4 bonbons de plus que Petya. Combien de bonbons chacun d'eux a-t-il`?

*Note*: Utilisez des expressions mathématiques simples comme `2 + 3 * 5` ou `10 / 2` pour les calculs.

*Documentation complète sur l'utilisation du bot (anglais)*: https://telegra.ph/FireCalc--your-personal-math-assistant-in-Telegram-03-17

[Conditions d'utilisation](https://telegra.ph/FireCalc-Terms-of-Use-03-21)
""",
        "cleared": "*Effacé!* 🧹",
        "about": """*À propos du bot et de son développeur*

*FireCalc* est conçu pour aider les utilisateurs à résoudre une large gamme de tâches — *des calculs mathématiques simples à la génération de nombres aléatoires, la création de graphiques et bien plus encore*. Avec une interface intuitive et des réponses rapides, il deviendra un outil fiable pour une interaction efficace.

Le bot prend en charge plusieurs langues, y compris le russe et l'anglais. *Que vous ayez besoin de résoudre une tâche simple ou d'effectuer des calculs plus complexes, ce bot est prêt à vous aider*.

*À propos du développeur*

Ce bot a été créé et est maintenu par *Flarosoft* — un développeur indépendant passionné par la programmation et qui s'efforce de créer des outils utiles pour les autres. L'objectif principal de Flarosoft est de rendre les tâches quotidiennes plus faciles et plus efficaces pour les utilisateurs du monde entier.

En tant que développeur open-source, Flarosoft cherche à contribuer à la communauté technologique en créant des logiciels accessibles, personnalisables et fiables. Si vous aimez utiliser ce bot, n'hésitez pas à *laisser des commentaires* (@flarosoft) pour aider à améliorer les versions futures.""",
"thinking": "Je pense...",
"decide_please": "Veuillez saisir la tâche après la commande 'decide'."
    },
    "es": {
        "start": """👋🏻 ¡Hola!

*Soy una calculadora inteligente y moderna*, diseñada para resolver una amplia gama de problemas matemáticos.

Mi sistema es capaz de *realizar cálculos elementales y complejos de análisis*, ofreciendo soluciones *precisas* y *razonadas*. 🧮

*¡Introduce una expresión matemática o una ecuación y realizaré de inmediato los cálculos necesarios para proporcionarte una solución confiable!* 😉

👥 Si necesitas una calculadora inteligente en tu grupo, solo [agrégame](tg://resolve?domain=FireCalcTG_bot&startgroup=new), ¡y estaré listo para trabajar en poco tiempo! (Responde a mi mensaje con tu expresión, ¡y la resolveré!)""",
        "random_result": "Número aleatorio: *{}*",
        "currency": "Conversión de divisas",
        "temperature": "Conversión de temperatura",
        "result": "Resultado: *{}*",
        "error": "¡Error! 😞",
        "solve": "Resolviendo la ecuación: *{}*",
        "plot": "Gráfico generado: *{}*",
        "unknown_command": "¡Comando o formato desconocido!",
        "error_invalid_expression": "¡Error: Expresión no válida!",
        "error_invalid_currency": "¡Error: Divisa no válida!",
        "error_invalid_temperature": "¡Error: Conversión de temperatura no válida!",
        "error_unknown_function": "¡Error: Función desconocida!",
        "help": """*Comandos disponibles*:

1. `/start` - Iniciar el bot y seleccionar un idioma.
2. `/help` - Mostrar este mensaje de ayuda.
3. `solve <ecuación>` - Resolver una ecuación matemática. Ejemplo: `solve x^2 - 5 * x + 6 = 0`
4. `plot <función>, <x_min>, <x_max>` - Graficar una función en un intervalo dado. Ejemplo: `plot x**3,-14,134` (símbolo ^ = **)
5. `random <min>, <max>` - Generar un número aleatorio entre min y max. Ejemplo: `random 1, 100`
6. `convert_currency <cantidad> <de_moneda> <a_moneda>` - Conversión de divisas. Ejemplo: `convert_currency 100 USD EUR`. Nota: esta función aún no funciona, pero el desarrollador ya está corrigiendo este error.
7. `kg_to_lb <kg>` - Convertir kilogramos a libras. Ejemplo: `kg_to_lb(50)`
8. `lb_to_kg <libras>` - Convertir libras a kilogramos. Ejemplo: `lb_to_kg(110)`
9. `c_to_f <c>` - Convertir Celsius a Fahrenheit. Ejemplo: `c_to_f(25)`
10. `f_to_c <f>` - Convertir Fahrenheit a Celsius. Ejemplo: `f_to_c(77)`
11. `c_to_k <c>` - Convertir Celsius a Kelvin. Ejemplo: `c_to_k(25)`
12. `k_to_c <k>` - Convertir Kelvin a Celsius. Ejemplo: `k_to_c(298)`
13. `decide <problema>` - Resolver un problema matemático de texto. Ejemplo: `decide que Vanya y Petya juntos tienen 20 caramelos. Vanya tiene 4 dulces más que Petya. ¿Cuántos dulces tiene cada uno de ellos?`

*Nota*: Usa expresiones matemáticas simples como `2 + 3 * 5` o `10 / 2` para los cálculos.

*Documentación completa sobre cómo utilizar el bot (en inglés)*: https://telegra.ph/FireCalc--your-personal-math-assistant-in-Telegram-03-17

[Condiciones de uso](https://telegra.ph/FireCalc-Terms-of-Use-03-21)
""",
        "cleared": "*¡Borrado!* 🧹",
        "about": """*Sobre el bot y su desarrollador*

*FireCalc* está diseñado para ayudar a los usuarios a resolver una amplia gama de tareas, desde *cálculos matemáticos simples hasta la generación de números aleatorios, gráficos y mucho más*. Con una interfaz fácil de usar y respuestas rápidas, se convertirá en una herramienta confiable para una interacción eficiente.

El bot admite varios idiomas, incluidos ruso e inglés. *Ya sea que necesites resolver una tarea simple o realizar cálculos más complejos, este bot está listo para ayudarte*.

*Sobre el desarrollador*

Este bot fue creado y es mantenido por *Flarosoft* — un desarrollador independiente apasionado por la programación y que trabaja para crear herramientas útiles para otros. El objetivo principal de Flarosoft es hacer que las tareas cotidianas sean más fáciles y eficientes para los usuarios de todo el mundo.

Como desarrollador de código abierto, Flarosoft busca contribuir a la comunidad tecnológica creando software accesible, personalizable y confiable. Si te gusta usar este bot, no dudes en *dejar comentarios* (@flarosoft) para ayudar a mejorar las versiones futuras.""",
"thinking": "Estoy pensando...",
"decide_please": "Por favor, introduzca la tarea después del comando 'decide'."
    },
}

def setlang(lang, id):
    with open(f"{id}_lang.txt", "w") as file:
        file.write(lang)

def readlang(id):
    try:
        with open(f"{id}_lang.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "en"

def bannedmsg(id):
    bot.send_message(
    id,
    "🚫 *Access permanently denied*\n\n"
    "You have been *banned for using offensive language*.\n"
    "If you believe this action was taken in error, you may contact the developer for clarification: @flarosoft",
    parse_mode="Markdown"
)

def kg_to_lb(kg): return kg * 2.20462
def lb_to_kg(lb): return lb / 2.20462
def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15

def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def solve(equation):
    try:
        if isinstance(equation, str):
            equation = equation.replace("^", "**")
            equation = equation.replace("=", "-(") + ")"
            x = sp.Symbol("x")
            result = sp.solve(sp.sympify(equation), x)

        elif isinstance(equation, list):
            variables = set(re.findall(r"[a-zA-Z]+", " ".join(equation)))
            symbols = {var: sp.Symbol(var) for var in variables}
            eqs = [sp.sympify(eq.replace("=", "-(") + ")", locals=symbols) for eq in equation]
            result = sp.solve(eqs, list(symbols.values()))

        else:
            result = "Equation error"

        logging.info(f"Equation solution: {equation} -> {result}")
        return result
    except Exception as e:
        logging.error(f"Equation solving error: {e}")
        return messages[readlang(id)]["error_invalid_expression"]

def plot(func, x_min, x_max):
    try:
        x = np.linspace(x_min, x_max, 1000)
        y = [eval(func, {"x": val, "math": math}) for val in x]

        plt.plot(x, y)
        plt.title(f"Graph of {func}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        path = "plot.png"
        plt.savefig(path)
        plt.close()

        logging.info(f"Graph plot generated: {func}")
        return path
    except Exception as e:
        logging.error(f"Graph plotting error: {e}")
        return messages[readlang(id)]["error_unknown_function"]

allowed_names = {
    **{name: getattr(math, name) for name in dir(math) if not name.startswith("_")},
    **{name: getattr(cmath, name) for name in dir(cmath) if not name.startswith("_")},
    "random": lambda x, y: random.uniform(x, y),
    "kg_to_lb": kg_to_lb, "lb_to_kg": lb_to_kg,
    "c_to_f": c_to_f, "f_to_c": f_to_c, "c_to_k": c_to_k, "k_to_c": k_to_c,
    "now": now, "solve": solve, "plot": plot
}

def secure_eval(expression, user_id):
    try:
        if not re.match(r"^[\d\.\+\-\*/\%\(\)\s\^,a-zA-Z_=\[\]]+$", expression):
            return messages[readlang(user_id)]["error_invalid_expression"]
        expression = expression.replace("^", "**")

        if expression in ["+", "-", "/", "*", "%", "^"]:
            return messages[readlang(user_id)]["error_invalid_expression"]

        result = eval(expression, {"__builtins__": None}, allowed_names)

        logging.info(f"Expression result: {expression} -> {result}")
        return result
    except Exception as e:
        logging.error(f"Error in computation: {e}")
        return messages[readlang(user_id)]["error_invalid_expression"]

def get_username(message):
    """Get user's username if available"""
    username = message.from_user.username
    return f"@{username}" if username else ""

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.chat.id
    username = get_username(message)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🇬🇧 English")
    item2 = types.KeyboardButton("🇷🇺 Русский")
    item3 = types.KeyboardButton("🇩🇪 Deutsch")
    item4 = types.KeyboardButton("🇫🇷 Français")
    item5 = types.KeyboardButton("🇪🇸 Español")
    if not os.path.isfile(f"{user_id}_firecalc_banned.txt"):
        markup.add(item1, item2, item3, item4, item5)

    logging.info(f"User {user_id} {username} started interaction with bot")

    if not os.path.isfile(f"{user_id}_firecalc_banned.txt"):
        bot.send_message(
        user_id,
        "🇬🇧 Please choose your language / 🇷🇺 Пожалуйста, выберите язык / 🇩🇪 Bitte wählen Sie eine Sprache aus /🇫🇷 Veuillez sélectionner une langue / 🇪🇸 Por favor seleccione un idioma:",
        reply_markup=markup
    )
    else:
        bannedmsg(user_id)


def setlang(lang, id):
    with open(f"{id}_lang.txt", "w") as file:
        file.write(lang)

def readlang(id):
    try:
        with open(f"{id}_lang.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "en"  # Default to English if no language file exists

@bot.message_handler(func=lambda message: message.text in ["🇬🇧 English", "🇷🇺 Русский", "🇩🇪 Deutsch", "🇫🇷 Français", "🇪🇸 Español"])
def set_language(message):
    user_id = message.chat.id
    username = get_username(message)

    if message.text == "🇬🇧 English":
        setlang("en", user_id)
    elif message.text == "🇷🇺 Русский":
        setlang("ru", user_id)
    elif message.text == "🇩🇪 Deutsch":
        setlang("de", user_id)
    elif message.text == "🇫🇷 Français":
        setlang("fr", user_id)
    elif message.text == "🇪🇸 Español":
        setlang("es", user_id)

    logging.info(f"User {user_id} {username} selected language: {readlang(user_id)}")

    markup = types.ReplyKeyboardRemove()
    invite_link = "tg://resolve?domain=FireCalcTG_bot&startgroup=new"
    bot.send_message(
        user_id,
        messages[readlang(user_id)]["start"],
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['clear'])
def clear_chat(message):
    chat_id = message.chat.id
    message_id = message.message_id
    username = get_username()

    logging.info(f"User {chat_id} {username} started clearing the chat")

    while message_id > 0:
        try:
            bot.delete_message(chat_id, message_id)
            message_id -= 1
        except Exception:
            break

    confirmation = bot.send_message(chat_id, messages[readlang(chat_id)]["cleared"], parse_mode="Markdown")
    time.sleep(2.5)
    bot.delete_message(chat_id, confirmation.message_id)

@bot.message_handler(commands=["help"])
def help(message):
    user_id = message.chat.id
    username = get_username(message)
    if not os.path.isfile(f"{user_id}_firecalc_banned.txt"):
        logging.info(f"User {user_id} {username} opened the help menu")
        bot.send_message(user_id, messages[readlang(user_id)]["help"], parse_mode="Markdown")
    else:
        bannedmsg(user_id)

@bot.message_handler(commands=["about"])
def about(message):
    user_id = message.chat.id
    username = get_username(message)
    if os.path.isfile(f"{user_id}_firecalc_banned.txt") == False:
      logging.info(f"User {id} {username} opened the 'about' menu")
      bot.send_message(user_id, messages[readlang(user_id)]["about"], parse_mode="Markdown")
    else:
        bannedmsg(user_id)


def check_message(text, id, un):
    # Bad words, that the bot bans
    words = ['даун', 'пидор', 'чушпан', 'сука', 'еба', 'ёба', 'еб', 'ёб', 'задрот', 'чушпан', 'дрочить', 'бляхамуха', 'бляха-муха', 'бляха', 'пиздюлка', 'пиздюлька', 'пиздюли', 'пиздюлей', 'пиздюлями', 'пиздочка', 'бляха муха', 'хуй', 'хер', 'бля', 'блять', 'блядь', 'охуеть', 'ахуеть', 'говно', 'пидорас', 'еблан', 'ебать', 'ахуел', 'охуел', 'ахуела', 'охуела', 'охуело', 'ахуело', 'гондон', 'гандон', 'нахуй', 'пенис', 'член', 'пизда', 'хуйня', 'жопа', 'жопочка', 'жопонька', 'жопо', 'ненавижу', 'ненависть', 'сучка', 'далбаеб', 'далбаёб', 'долбаёб', 'долбаеб', 'ахуевший', 'охуевший', 'хуйло', 'пиздеть', 'пиздеж', 'пиздишь', 'пиздел', 'пиздело', 'пиздела', 'тварюка', 'неновижу',  'залупа', 'пиздец', 'наеб', 'наёб', 'гавно', 'говняное', 'говняный', 'говновоз', 'анал', 'секс', 'сексик', 'говнян', 'говняная', 'гавнян', 'пися', 'писюлька', 'писечка', 'писька', 'пипка', 'пипипка', 'скатина', 'скотино', 'скотина', 'скатино', 'ебись', 'соси', 'сиськи', 'сиська', 'сиси', 'сисечки', 'down', 'fag', 'chump', 'bitch', 'eba', 'nerd', 'chump', 'wank', 'fuck-fly', 'pizdyulka', 'pizdyuli', 'pizdyulei', 'pizdyuliami', 'cunt', 'fuck fly', 'dick', 'cock', 'fuck', 'slut', 'oh-fucking-fuck', 'aw-shucks', 'faggot', 'moron', 'oh-fucking-fuck', 'ahuelo', 'condom', 'fuck', 'penis', 'dick', 'pussy', 'ass', 'I hate', 'hatred', 'dumbass', 'fucking', 'to lie', 'bullshit', 'shit', 'shitty', 'shit truck', 'anal', 'sex', 'sexy', 'pussy', 'pipka', 'pipipka', 'scum', 'cattle', 'scum', 'suck', 'tits', 'tit', 'boobs', 'boob']

    words_in_text = re.findall(r'\b\w+\b', text.lower())

    for word in words_in_text:
        if word in words:
            blocked_user = open(f"{id}_firecalc_banned.txt", "w")
            blocked_user.write(f"User {id} {un} was blocked for insults: {text}")
            blocked_user.close()
            return True
    return False

TRIGGERS = ['пасиб', 'благодар', 'крут', 'топ', 'имба', 'шедевр', 'вау', 'круто', 'люблю', 'любить', 'любил', 'идеал', 'огонь', 'афигеть', 'офигеть', 'ого', 'золотце', 'золото', 'лучш', 'легенда', 'кайф', 'балдеж', 'балдёж', 'оболдеть', 'абалдеть', 'офигенно', 'афигенно', 'офигенна', 'афигенна', 'восторг', 'блест', 'блеск', 'чемпион', 'бомба', 'космос', 'обожаю', 'обожать', 'обожал', 'титан', 'сочн', 'классно', 'классна', 'класно', 'класна', '🤩', '😍', '🥰', '😻', '🥹', '😱', '😮', '😯', '😲', '👏', '🙌', '🫶', '👍', '👌', '🤌', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '💖', '💗', '💓', '💞', '💕', '💘', '💝', '🌟', '✨', '🎉', '💫', '💥', '🔥', '🚀', '👑', '🧠💥']

def set_reaction(chat_id, message_id, emoji):
    url = f'https://api.telegram.org/bot{TOKEN}/setMessageReaction'
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [{"type": "emoji", "emoji": emoji}]
    }
    response = requests.post(url, json=payload)
    return response.json()

@bot.message_handler(func=lambda message: any(trigger in message.text.lower() for trigger in TRIGGERS) and not message.text.lower().startswith("decide"))
def react(message):
    set_reaction(message.chat.id, message.message_id, "❤️")

client = AI21Client(api_key="YOUR_AI21_API_KEY")

def solve_task(user_input: str) -> str:
    response = client.chat.completions.create(
        model="jamba-large-1.6",
        messages=[
            ChatMessage(
                role="system",
                content=("Ты умеешь решать только математические задачи (не делай ничего другого), которые тебе введёт пользователь."
                         "Разговаривай вежливо, на Вы, грамотно."
                         "Всегда пиши без форматирования Markdown и дробей (их заменяй на Unicode-символы), а другие LaTeX символы, кроме дробей, пиши."
                         "Ты разработан разработчиком Flarosoft (Telegram-канал: https://t.me/flarosoftdev) и используешься в его Telegram-боте FireCalc (ссылка: https://t.me/flarosoftdev). GitHub разработчика: https://github.com/flarosoftdev. Сайт разработчика: https://flarosoft.pages.dev")
            ),
            ChatMessage(
                role="user",
                content=user_input
            )
        ],
        documents=[],
        tools=[],
        n=1,
        max_tokens=2048,
        temperature=0,
        top_p=1,
        stop=[],
        response_format=ResponseFormat(type="text"),
    )

    answer = response.choices[0].message.content.strip()
    return answer

def translate_text(text, lang):
    translator = GoogleTranslator(source='auto', target=lang)
    return translator.translate(text)

def escape_markdown(text):
    text = re.sub(r'([*_])(?=\S)(.*?)(?<=\S)\1', r'\2', text)
    text = re.sub(r'`(?=\S)(.*?)(?<=\S)`', r'\1', text)
    text = re.sub(r'^\s*#+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*>\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'(~~)(?=\S)(.*?)(?<=\S)\1', r'\2', text)

    replacements = {
        'cdot': '⋅',
        'dots': '…',
        'sqrt{': '√',
        'log_2': 'log₂',
        'log_10': 'log₁₀',
        '{X}': 'X',
        '{Y}': 'Y',
        '{Z}': 'Z',
        'pm': '±',
        'times': '×',
        'div': '÷',
        'frac{1}{2}': '½',
        'frac{1}{3}': '⅓',
        'frac{2}{3}': '⅔',
        'frac{1}{4}': '¼',
        'frac{3}{4}': '¾',
        'frac{1}{5}': '⅕',
        'frac{2}{5}': '⅖',
        'frac{3}{5}': '⅗',
        'frac{4}{5}': '⅘',
        'frac{1}{6}': '⅙',
        'frac{5}{6}': '⅚',
        'frac{1}{8}': '⅛',
        'frac{3}{8}': '⅜',
        'frac{5}{8}': '⅝',
        'frac{7}{8}': '⅞',
        'alpha': 'α',
        'beta': 'β',
        'gamma': 'γ',
        'delta': 'δ',
        'epsilon': 'ε',
        'zeta': 'ζ',
        'eta': 'η',
        'theta': 'θ',
        'iota': 'ι',
        'kappa': 'κ',
        'lambda': 'λ',
        'mu': 'μ',
        'nu': 'ν',
        'xi': 'ξ',
        'pi': 'π',
        'rho': 'ρ',
        'sigma': 'σ',
        'tau': 'τ',
        'upsilon': 'υ',
        'phi': 'φ',
        'chi': 'χ',
        'psi': 'ψ',
        'omega': 'ω',
        'Gamma': 'Γ',
        'Delta': 'Δ',
        'Theta': 'Θ',
        'Lambda': 'Λ',
        'Xi': 'Ξ',
        'Pi': 'Π',
        'Sigma': 'Σ',
        'Upsilon': 'Υ',
        'Phi': 'Φ',
        'Psi': 'Ψ',
        'Omega': 'Ω',
        'neq': '≠',
        'leq': '≤',
        'geq': '≥',
        'approx': '≈',
        'sim': '∼',
        'cong': '≅',
        'propto': '∝',
        'infty': '∞',
        'sum': '∑',
        'prod': '∏',
        'int': '∫',
        'oint': '∮',
        'partial': '∂',
        'nabla': '∇',
        'forall': '∀',
        'exists': '∃',
        'emptyset': '∅',
        'in': '∈',
        'notin': '∉',
        'ni': '∋',
        'cap': '∩',
        'cup': '∪',
        'subset': '⊂',
        'supset': '⊃',
        'subseteq': '⊆',
        'supseteq': '⊇',
        'perp': '⊥',
        'parallel': '∥',
        'angle': '∠',
        'triangle': '△',
        'therefore': '∴',
        'because': '∵',
        'lceil': '⌈',
        'rceil': '⌉',
        'lfloor': '⌊',
        'rfloor': '⌋',
    }

    for latex, symbol in replacements.items():
        text = re.sub(r'\\+' + re.escape(latex), symbol, text)

    return text

@bot.message_handler(func=lambda message: message.text.startswith("decide"))

def handle_message(message):
    un = get_username(message)
    id = message.chat.id
    user_input = message.text[len("decide"):].strip()
    logging.info(f"Received request from {id} {un}: {user_input}")
    if user_input:
        bot.send_message(id, messages[readlang(id)]["thinking"])
        answer = solve_task(user_input).replace("$", "`")
        answer = answer[:4996] + "..." if len(answer) > 4996 else answer
        answer = escape_markdown(answer)
        logging.info(f"({id} {un}) Problem solved: {answer}")
        try:
            bot.send_message(id, answer)
        except Exception as e:
            e_translated = translate_text(e, readlang(id))
            bot.send_message(id, messages[readlang(id)]["error"]+f"\n{e_translated}")
    else:
        bot.send_message(id, messages[readlang(id)]["decide_please"])


@bot.message_handler(func=lambda message: True)
def calculate(message):
    expr = message.text.strip()
    user_id = message.chat.id
    username = get_username(message)
    language = readlang(user_id)

    logging.info(f"Received request from {user_id} {username} ({language}): {expr}")

    if check_message(expr, user_id, username) == False and not os.path.isfile(f"{user_id}_firecalc_banned.txt"):
        try:
            if expr.startswith("solve"):
                equation = expr[6:].strip()
                if equation.startswith("[") and equation.endswith("]"):
                    equation = eval(equation)
                result = solve(equation)
                bot.send_message(user_id, messages[language]["solve"].format(result), parse_mode="Markdown")

            elif expr.startswith("plot"):
                parts = expr[5:].split(",")
                func, x_min, x_max = parts[0].strip(), float(parts[1]), float(parts[2])
                plot_path = plot(func, x_min, x_max)
                if plot_path != "Error":
                   bot.send_photo(user_id, open(plot_path, "rb"))
                else:
                    bot.send_message(user_id, messages[language]["error"])

            elif expr.startswith("random"):
                numbers = expr.split(",")
                result = random.uniform(float(numbers[0][7:]), float(numbers[1]))
                bot.send_message(user_id, messages[readlang(user_id)]["random_result"].format(int(result)), parse_mode="Markdown")

            else:
                result = secure_eval(expr, user_id)
                bot.send_message(user_id, messages[language]["result"].format(result), parse_mode="Markdown")

        except Exception as e:
            logging.error(f"Calculation error: {e}")
            bot.send_message(user_id, messages[language]["error"])

    else:
        bannedmsg(user_id)
def restart_bot():
    logging.info("Restarting the bot...")
    time.sleep(5)
    os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    while True:
        try:
            logging.info("Starting the bot...")
            bot.polling(none_stop=True, timeout=60)
        except (Exception, OSError, ConnectionError) as e:
            logging.error(f"An error occurred: {e}. The bot will be restarted")
            restart_bot()
        except KeyboardInterrupt:
            logging.info("Bot manually stopped. Exiting...")
            break
