<?php

include(__DIR__.'/config.php');

// Dump($user->keys("*"));
// Dump($userlist);
// Dump($user->hgetall("userID:14"));


$feedback = isset($_SESSION['user-feedback']) ? $_SESSION['user-feedback'] : "nothing";

$user = new \Weleoka\Users\UserRedis();
$userlist = $user->hgetall("userlist");
$HTML = "";

foreach ($userlist as $name => $userID) {
	$arr = $user->getUser($userID);
	$view =  "<p>"
		. "<br>Active: " 	. $arr['active']
		. "<br>Full name :" . $arr['fullname']
		. "<br>Username: " 	. $arr['username']
		. "<br>email :" 	. $arr['email']
		. "<br>profile :" 	. $arr['profile']
		. "<br>created :" 	. $arr['created']
		. "<br>latestIp :" 	. $arr['latestIp']
		. "<br>firstIp :" 	. $arr['firstIp']
		. "</p>";
	$HTML .= $view;
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







