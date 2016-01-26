<?php
include(__DIR__.'/config.php');

$roo['title'] = "Setup";

$roo['header'] .= '<span class="siteslogan">Install and setup documentation.</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Ardeidae Setup</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
    <a href="#">
    <li data-src="img/node02.png" class="decoration"></li>
    </a>


    <!-- <img id="imgNode" class="decoration" data-src="img/node02.png"> -->
    <h3>Header</h3>
    <p>Text and text.</p>
    <p></p>
</div>

<div class="articleSegment">
    <h3>Header</h3>
    <p></p>
    <p></p>

    <p>Text and text.</p>
</div>


EOD;

$roo['footer'];

include(ROO_THEME_PATH);







