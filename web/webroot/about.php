<?php

include(__DIR__.'/config.php');

$roo['title'] = "About";

$roo['header'] .= '<span class="siteslogan">About RavensGRIB.</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">RavensGRIB about</p>';

$roo['main'] = <<<EOD

<p>...</p>
<p>...</p>

<p></p>
<p></p>
<p>Questions please contact kawe14@eee.se</p>
<p>.: :.</p>
EOD;

$roo['footer'];

include(ROO_THEME_PATH);