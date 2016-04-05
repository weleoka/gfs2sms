<?php

include(__DIR__.'/config.php');

$form = new \Weleoka\HTMLForm\CLogin();
$form->check();
$formHTML = $form->getHTML();
// $feedback = $user->getFeedback();

$roo['title'] = "Login";
$roo['header'] .= '<span class="siteslogan">Sign up for Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Sign-Up</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
    <h2>RavensGRIB login dev.</h2>
    $formHTML
</div>

EOD;

$roo['footer'];

include(ROO_THEME_PATH);
