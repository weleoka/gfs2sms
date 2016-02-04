<?php
/**
 * This is the Roo pagecontroller.
 *
 */
// Include the essential config-file which also creates the $roo variable with its defaults.
include(__DIR__.'/config.php');

// Do it and store it all in variables in the Roo container.
$roo['title'] = "SiteNav";

$roo['main'] = <<<EOD

<a href="index.php" class="mobileNavLink">Home</a>
<a href="setup.php" class="mobileNavLink">Setup</a>
<a href="about.php" class="mobileNavLink">About</a>
<a href="documentation.php" class="mobileNavLink">Documentation</a>

EOD;


$roo['footer'];


// Finally, leave it all to the rendering phase of roo.
include(ROO_THEME_PATH);