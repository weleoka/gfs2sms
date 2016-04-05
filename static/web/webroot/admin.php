<?php
// Dump($user->keys("*"));
// Dump($userlist);
// Dump($user->hgetall("userID:14"));

include(__DIR__.'/config.php');

$feedback = isset($_SESSION['user-feedback']) ? $_SESSION['user-feedback'] : "nothing";

$user = new \Weleoka\Users\UserRedis();
$HTML = "";

if ($user->isAdmin()) {
    $userlist = $user->hgetall("userlist");

    foreach ($userlist as $name => $userID) {
        $HTML .= $user->getUserHTML($userID);
    }

} else {
    header("Location: index.php");
    // header('Refresh: 3; URL=' . __DIR__ .'/index.php');
}


$roo['title'] = "Admin";
$roo['header'] .= '<span class="siteslogan">Administrator Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Administrate Ravensgrib</p>';
$roo['main'] = <<<EOD

<div class="articleSegment">
<h2>RavensGRIB admin dev.</h2>
<br>
$HTML;

<a href="admin.php?viewAccounts">View accounts</a><br>
</div>

EOD;

$roo['footer'];

include(ROO_THEME_PATH);







