<?php

// Do:
// (new composer hook for weleoka/cform.)
// Check cform saveInSession for re-populating failed form.

include(__DIR__.'/config.php');

$form = new \Weleoka\HTMLForm\CSignup();
// if ($_SERVER["REQUEST_METHOD"] == "POST")

$form->check();
$formHTML = $form->getHTML();

$roo['title'] = "Sign-up";

$roo['header'] .= '<span class="siteslogan">Sign up for Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Sign-Up</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
    <h2>RavensGRIB sign up dev.</h2>
    $formHTML
</div>

EOD;


$roo['footer'];

include(ROO_THEME_PATH);