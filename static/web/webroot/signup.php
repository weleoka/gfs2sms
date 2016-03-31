<?php

include(__DIR__.'/config.php');

$feedback = isset($_SESSION['user-feedback']) ? $_SESSION['user-feedback'] : "nothing";

$user = new Weleoka\UserRedis();
$form = new Weleoka\CSignup();

if(isset($_POST['signup'])) {
    $username = isset($_POST['username']) ? $_POST['username'] : "alarmNoUsrSignup";
    $password = isset($_POST['password']) ? $_POST['password'] : "alarmNoPwdSignup";
    $user->signup();
}

$roo['title'] = "Sign-up";

$roo['header'] .= '<span class="siteslogan">Sign up for Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Sign-Up</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
<h2>RavensGRIB sign up dev.</h2>
REDIT: $res
<br>
UserRedis class: $feedback
<br>
$form

<br>
<form method="POST" action="signup.php">
    <h3>Sign up form</h3>
    <div>
        Username
        <input type="text" placeholder="" value="" required="" name="username" />
    </div>
    <div>
        Full name
        <input type="text" placeholder="" value="" required="" name="fullname" />
    </div>
    <div>
        Profile
        <input type="text" placeholder="" value="" required="" name="profile" />
    </div>
    <div>
        Password
        <input type="text" placeholder="" value="" required="" name="password" />
    </div>
    <div>
        <input type="submit" value="Sign up" name="signup" /><br>
        <input type="reset" value="Reset"><br>
    </div>
</form>

</div>

EOD;

$roo['footer'];

include(ROO_THEME_PATH);
