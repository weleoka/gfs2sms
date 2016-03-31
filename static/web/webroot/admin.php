<?php

include(__DIR__.'/config.php');

$feedback = isset($_SESSION['user-feedback']) ? $_SESSION['user-feedback'] : "nothing";

$user = new \Weleoka\Users\UserRedis();

if (isset($_POST['viewAccounts'])) {
    Dump($user->keys("*"));
    Dump($user->hgetall("userlist"));
    // Dump($redis->hgetall("userID:0"));    
}

    Dump($user->keys("*"));
    Dump($user->hgetall("userlist"));
    // Dump($redis->hgetall("userID:0")); 

$roo['title'] = "Admin";
$roo['header'] .= '<span class="siteslogan">Administrator Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Administrate Ravensgrib</p>';
$roo['main'] = <<<EOD

<div class="articleSegment">
<h2>RavensGRIB admin dev.</h2>
<br>
UserRedis class: $feedback
<a href="admin.php?viewAccounts">View accounts</a><br>
</div>

EOD;

$roo['footer'];

include(ROO_THEME_PATH);







