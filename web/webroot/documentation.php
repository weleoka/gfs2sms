<?php

include(__DIR__.'/config.php');

$my_text = file_get_contents('../README.md');


use \Michelf\Markdown;
$my_html = Markdown::defaultTransform($my_text);

$roo['title'] = "Recources";

$roo['header'] .= '<span class="siteslogan">Useful links and recources</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Ardeidae Docs</p>';

$roo['main'] = <<<EOD

$my_html

EOD;


$roo['footer'] .= <<<EOD

<nav>Validators:
  <a href='http://validator.w3.org/check/referer'>HTML5</a>
  <a href='http://jigsaw.w3.org/css-validator/check/referer?profile=css3'>CSS3</a>
  <a href='http://validator.w3.org/unicorn/check?ucn_uri=referer&amp;ucn_task=conformance'>Unicorn</a>
  <a href='http://csslint.net/'>CSS-lint</a>
  <a href='http://jslint.com/'>JS-lint</a>
</nav>
 <br>
<nav>Tools:
  <a href='http://dbwebb.se/forum'>forum</a>
  <a href='http://dbwebb.se/style'>style</a>
  <a href='http://jsfiddle.net/'>jsfiddle</a>
  <a href='http://jsfiddle.net/user/weleoka/fiddles/'>fiddles/weleoka</a>
  <a href='http://pastebin.com/'>pastebin</a>
  <a href='https://gist.github.com/'>gist</a>
  <a href='http://www.quirksmode.org/compatibility.html'>quirksmode</a>
  <a href='http://caniuse.com/'>when can I use</a>
  <a href='http://www.workwithcolor.com/hsl-color-schemer-01.htm'>colors</a>
</nav>
 <br>
<nav>Manuals:
  <a href='http://www.w3.org/2009/cheatsheet'>Cheatsheet</a>
  <a href='http://www.w3.org/'>W3C</a>
  <a href='http://dev.w3.org/html5/spec/spec.html'>HTML5</a>
  <a href='http://www.w3.org/TR/CSS2'>CSS2</a>
  <a href='http://www.w3.org/Style/CSS/current-work#CSS3'>CSS3</a>
  <a href='https://developer.mozilla.org/en/JavaScript/Reference'>JS Core</a>
  <a href='https://developer.mozilla.org/en/Gecko_DOM_Reference'>JS DOM</a>
  <br>
  <a href='https://developer.mozilla.org/en/DOM/DOM_event_reference'>JS DOM Events</a>
  <a href='http://php.net/manual/en/index.php'>PHP</a>
  <a href='http://api.jquery.com/'>jQuery</a>
  <a href='http://lesscss.org/'>LESS</a>
  <a href='https://developer.mozilla.org/'>Mozilla DN</a>
  <a href='http://developer.apple.com/library/safari/navigation/'>Apple DN</a>
  <a href='http://www.w3schools.com/'>w3schools</a>
</nav>

EOD;


include(ROO_THEME_PATH);







