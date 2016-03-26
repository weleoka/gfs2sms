<?php
include(__DIR__.'/config.php');

    isset($res) ? $res = $res : $res = "nothing";

    $redis = new Predis\Client(array(
        "scheme" => "tcp",
        "host" => "127.0.0.1",
        "port" => 6379,
        "password" => "",
        "database" => 10,
        "persistent" => "0"));

    // Initial database set-up
    !$redis->exists('usercount') ? $redis->set("usercount", 0) : $res .= " (usercount: " . $redis->get("usercount") . ").";

    

if(isset($_POST['signup'])) {

    $username = $_POST['username'];
    $fullname = $_POST['username'];
    $email = $_POST['username'];
    $password = $_POST['password'];
    $profile = $_POST['username'];

    $newUserID = $redis->get("usercount");
    $key_user = "userID:" . $newUserID; // Note the semi-colon.

    // Hash and salt the new password.
    $password_hash = $password;

    // Register the new username and corresponding ID in userlist.
    $res = $redis->hmset("userlist", [
        $username => $newUserID,
    ]);

    $res = $redis->hmset($key_user, [
        'username' => $username,
        'fullName' => $fullname,
        'email' => $email,
        'password' => $password_hash,
        'profile' => $profile,
    ]);

    // Increment the usercount.
    $redis->incr("usercount");

} else if (isset($_GET['viewAccounts'])) {
    $arList = $redis->keys("*");
    echo "Stored keys in redis:: ";
    print_r($arList);
    Dump($redis->hgetall("userlist"));
}


$roo['title'] = "Sign-up";

$roo['header'] .= '<span class="siteslogan">Sign up for Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Sign-Up</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
<h2>RavensGRIB sign up dev.</h2>
REDIT: $res
<form method="POST" action="account.php">
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
        <a href="account.php?viewAccounts">Need help?</a><br>
    </div>
</form>

</div>

EOD;

$roo['footer'];

include(ROO_THEME_PATH);







