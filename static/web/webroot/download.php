<?php

include(__DIR__.'/config.php');

$roo['title'] = "Download";

$roo['header'] .= '<span class="siteslogan">Find and Download</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Ardeidae Download</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
    <a href="https://github.com/weleoka/ardeidae.git">
        <li data-src="img/gitlogo02.png" class="decoration"></li>
    <a>
    <h3>Source on git</h3>
    <p>The <a href='https://github.com/weleoka/ardeidae_home'> Ardeidae Website</a></p>
    <p></p>
</div>

<div class="articleSegment">
    <h3>Direct download</h3>
    <p>Download a ready zip file straight from here by clicking link below.</p>
    <a href='ardeidae_home.zip'><img src='img/download.png' id='download'></a>
    <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp:. . . . . . complete zip archive.</p>
</div>


<div class="articleSegment">
    <p></p>
    <p>Now rock the web.</p>
</div>

EOD;


$roo['footer'];

include(ROO_THEME_PATH);







