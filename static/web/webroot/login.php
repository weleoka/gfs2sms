<?php

include(__DIR__.'/config.php');

$feedback = isset($_SESSION['user-feedback']) ? $_SESSION['user-feedback'] : "nothing";

$user = new Weleoka\UserRedis();
$form = new Weleoka\CLogin();

if(isset($_POST['login'])) {
    $username = isset($_POST['username']) ? $_POST['username'] : "alarmNoUsrLogin";
    $password = isset($_POST['password']) ? $_POST['password'] : "alarmNoPwdLogin";
    $user->login($username, $password);
}

$roo['title'] = "Login";

$roo['header'] .= '<span class="siteslogan">Sign up for Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Sign-Up</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
<h2>RavensGRIB login dev.</h2>
REDIT: $res
<br>
UserRedis class: $feedback
<br>
$form
<form method="POST" action="login.php">
    <h3>Login form</h3>
    <div>
        Username
        <input type="text" placeholder="" value="" required="" name="username" />
    </div>
    <div>
        Password
        <input type="text" placeholder="" value="" required="" name="password" />
    </div>
    <div>
        <input type="submit" value="Log in" name="login" /><br>
        <input type="reset" value="Reset"><br>
    </div>
</form>

</div>

EOD;

$roo['footer'];

include(ROO_THEME_PATH);
